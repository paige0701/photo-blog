from django.contrib.auth.forms import UserCreationForm

from photoblog.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','username')

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user