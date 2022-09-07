from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        # All the fields below are defined by default in the User model from django.contrib.auth.
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

# The lines below are used to change the default labels for every field in the form and customize them as we want:
    def __init__(self, *args, **kwargs) -> None:
        # The line below call the UserCreationForm
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Display Name"
        self.fields['email'].label = "Email Address"