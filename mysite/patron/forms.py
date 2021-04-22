from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User #might as well change it back to newuserform


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username', 'email', 'password1', 'password2')
    
    def clean_password1(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

    def clean_password2(self, request, user):
        # Check that the two password entries match
        password = self.cleaned_data.get("password")
        password_2 = self.cleaned_data.get("password_2")
        if password and password_2 and password != password_2:
            raise forms.ValidationError("Passwords don't match")
        return password_2
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

        