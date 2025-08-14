from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    # Define choices for the category field
    CATEGORY_CHOICES = [
        ('', 'Select a category'),
        ('Biodegrable', 'Biodegradable'),
        ('Non biodegrable', 'Non-Biodegradable'),
    ]

    # Update the category field to use a ChoiceField with the defined choices
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)

    class Meta:
        model = Todo
        fields = ['latitude', 'longitude', 'category', 'place']







    



    
