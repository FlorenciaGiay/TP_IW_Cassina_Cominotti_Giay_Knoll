from django import forms
from users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # def __init__(self, **kwargs):
    #     super(UserRegisterForm, self).__init__(self, **kwargs)
    #     selected_choices = [(str(i), str(i)) for i in User.Role if str(i) != "ADMIN"]
    #     # print(selected_choices)
    #     # print([(k, v) for k, v in selected_choices if v != "ADMIN"])
    #     # self.fields['role'] = ((k, v) for k, v in selected_choices if v != "ADMIN")
    #     self.fields['role'] = forms.ChoiceField(
    #         label='Role',
    #         choices=selected_choices,
    #         initial='CLIENT',
    #     )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']