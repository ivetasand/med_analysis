from django import forms

class MyLoginForm(forms.Form):
    login = forms.CharField(max_length=50, label='Логин')
    password = forms.CharField(label='Пароль')
    choices = [('option1', 'ДНКОМ'), ('option2', 'Гемотест'), ('option3', 'Option 3')]
    select = forms.ChoiceField(choices=choices, label='Выбор лаборатории')