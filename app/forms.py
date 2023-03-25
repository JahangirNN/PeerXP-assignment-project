from django.forms import ModelForm

from app.models import Expense
class TODOForm(ModelForm):
    class Meta:
        model = Expense
        fields = ['name' , 'category' , 'description', 'ammount']