from django.forms import ModelForm
from .models import CLUB

class ProjectForm(ModelForm):
    class Meta:
        model = CLUB
        fields = ['name','Student_ID','Student_Mail','Phone_Number','Preferred_Club',
                  'tags','Reason_behind_joinning_club','Image',]