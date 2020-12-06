from django import forms
from .models import Pizza, Size, Toppings, Types, UserForm

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping 1', max_length=100)
#     topping2 = forms.CharField(label='Topping 2', max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

class PizzaForm(forms.ModelForm):
    class Meta:
            model = Pizza
            fields = ['toppings','size','types']

class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=6)

class FormUserForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['user_toppings','user_size']
