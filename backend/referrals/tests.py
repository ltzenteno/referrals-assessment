from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
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