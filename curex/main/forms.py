from django import forms

from .services import CHOICES


class ExchangeForm(forms.Form):
    amount = forms.IntegerField(label="Количество",
                                widget=forms.NumberInput(attrs={'placeholder': 'Введите сумму', 'class': ''}))
    give = forms.ChoiceField(choices=CHOICES, label="Отдаете", initial='USD', widget=forms.Select(attrs={'class': ''}))
    receive = forms.ChoiceField(choices=CHOICES, label="Получаете", initial='BYN',
                                widget=forms.Select(attrs={'class': ''}))
