from django.forms import ModelForm
from details.models import detail
class TestForm(ModelForm):
    class Meta:
        model=detail

