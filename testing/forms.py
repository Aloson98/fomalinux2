from django.forms import ModelForm
from testing.models import *

class adding_goods(ModelForm):
    class Meta:
        model = goods
        fields = '__all__'