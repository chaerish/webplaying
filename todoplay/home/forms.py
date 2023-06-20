from django import forms
from .models import User


class UserForm(forms.ModelForm):

    def is_valid(self):
        valid = super(UserForm, self).is_valid()

        if valid:
            if User.objects.filter(nickname = self.cleaned_data.get('nickname')).exists():
                self.add_error('nickname', 'nickname is already exists.')
                valid = False

        return valid
    class Meta:
        model = User
        fields = ("username", "nickname")
