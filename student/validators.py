# yourapp.validators.py

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_domainonly_email(value):
    """
    Let's validate the email passed is in the domain "yourdomain.com"
    """
    if not "akirachix.com" in value:
      raise ValidationError("your email must have akirachix.com as your domain")
    return value

# def validate_minimum_age(value):
#     {% if value < 17 %}
#         raise ValidationError("You need to be above 17 years old to register")
#     {% endif %}
#     return value