from django import forms


class Password_gen_form(forms.Form):
    length = forms.IntegerField(min_value=5, max_value=20, initial=8, label='Password length')
    
