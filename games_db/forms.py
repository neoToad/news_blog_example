from django.forms import ModelForm
from .models import Contact, EmailList


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class EmailListForm(ModelForm):
    class Meta:
        model = EmailList
        fields = '__all__'