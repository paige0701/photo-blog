from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


# User model, abstracUser 를 상속받아서 사용한ㄷㅏ
class User(AbstractUser):
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_active = models.BooleanField(
        _('active'),
        default=False,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )