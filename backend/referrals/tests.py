import uuid
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from rest_framework.test import APIClient
from .models import Referral

# Create your tests here (optional for this assessment)

def make_referral(**kwargs):
    defaults = dict(
        first_name='Test',
        last_name='User',
        email='test@example.com',
        last_sent_at=timezone.now(),
    )
    defaults.update(kwargs)
    return Referral.objects.create(**defaults)


class EmailUniquenessTest(TestCase):
    def test_email_stored_lowercase(self):
        r = make_referral(email='Test@Example.com')
        self.assertEqual(r.email, 'test@example.com')

    def test_duplicate_email_different_case_returns_409(self):
        make_referral(email='test@example.com')
        client = APIClient()
        response = client.post('/api/referrals/', {
            'first_name': 'Another',
            'last_name': 'User',
            'email': 'TEST@EXAMPLE.COM',
        })
        self.assertEqual(response.status_code, 409)

    def test_duplicate_email_same_case_returns_409(self):
        make_referral(email='test@example.com')
        client = APIClient()
        response = client.post('/api/referrals/', {
            'first_name': 'Another',
            'last_name': 'User',
            'email': 'test@example.com',
        })
        self.assertEqual(response.status_code, 409)

    def test_email_whitespace_trimmed(self):
        client = APIClient()
        response = client.post('/api/referrals/', {
            'first_name': 'Test',
            'last_name': 'User',
            'email': '  test@example.com  ',
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Referral.objects.first().email, 'test@example.com')


class ResendCooldownTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_resend_rejected_within_30_seconds(self) -> None:
        r = make_referral(last_sent_at=timezone.now())
        response = self.client.post(f'/api/referrals/{r.id}/resend/')
        self.assertEqual(response.status_code, 400)
        self.assertIn('30 seconds', response.data['detail'])

    def test_resend_allowed_after_30_seconds(self) -> None:
        r = make_referral(last_sent_at=timezone.now() - timedelta(seconds=31))
        response = self.client.post(f'/api/referrals/{r.id}/resend/')
        self.assertEqual(response.status_code, 200)

    def test_resend_updates_last_sent_at(self) -> None:
        old_time = timezone.now() - timedelta(seconds=31)
        r = make_referral(last_sent_at=old_time)
        self.client.post(f'/api/referrals/{r.id}/resend/')
        r.refresh_from_db()
        self.assertGreater(r.last_sent_at, old_time)

    def test_resend_non_invitation_sent_status_returns_400(self) -> None:
        r = make_referral(last_sent_at=timezone.now() - timedelta(seconds=31))
        r.status = Referral.Status.JOINED
        r.save()
        response = self.client.post(f'/api/referrals/{r.id}/resend/')
        self.assertEqual(response.status_code, 400)


class TokenTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_token_generated_on_creation(self) -> None:
        r = make_referral()
        self.assertIsNotNone(r.token)

    def test_resend_rotates_token(self) -> None:
        r = make_referral(last_sent_at=timezone.now() - timedelta(seconds=31))
        old_token = r.token
        self.client.post(f'/api/referrals/{r.id}/resend/')
        r.refresh_from_db()
        self.assertNotEqual(r.token, old_token)

    def test_old_token_returns_404_after_rotation(self) -> None:
        r = make_referral(last_sent_at=timezone.now() - timedelta(seconds=31))
        old_token = r.token
        self.client.post(f'/api/referrals/{r.id}/resend/')
        response = self.client.get(f'/api/referrals/lookup/?token={old_token}')
        self.assertEqual(response.status_code, 404)

    def test_token_stops_working_after_status_advances(self) -> None:
        r = make_referral()
        token = r.token
        r.status = Referral.Status.JOINED
        r.save()
        response = self.client.get(f'/api/referrals/lookup/?token={token}')
        self.assertEqual(response.status_code, 410)

    def test_unknown_token_returns_404(self) -> None:
        response = self.client.get(f'/api/referrals/lookup/?token={uuid.uuid4()}')
        self.assertEqual(response.status_code, 404)