from cProfile import label
from socket import fromshare
from django import forms


class CreateList(forms.Form):

    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

