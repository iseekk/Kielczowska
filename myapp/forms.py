from django import forms
from myapp.models import Purchase, Comment
from django.contrib.auth import forms as auth_forms
from bootstrap_datepicker_plus import DatePickerInput


class CustomAuthForm(auth_forms.AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "validate",
                                                       "placeholder": "Username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"type": "password",
                                                            "placeholder": "Password"}))

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ("author", "item", "price", "date")

        widgets = {
            "item": forms.TextInput(),
            "price": forms.NumberInput(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)

        widgets = {
            "text": forms.Textarea(),
        }
