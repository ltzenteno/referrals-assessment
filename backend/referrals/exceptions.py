from rest_framework.exceptions import APIException


class EmailAlreadyExistsError(APIException):
    status_code = 409
    default_detail = "A referral with this email already exists."
    default_code = "email_conflict"
