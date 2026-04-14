from django import forms  
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email', 'date_of_birth', 'course']
    

    # first_name = forms.CharField(max_length=200)  
    # last_name = forms.CharField(max_length=200)
    # age = forms.IntegerField()
    # email = forms.EmailField(Unique=True)
    # date_of_birth = forms.DateField()
    # course = forms.CharField(max_length=40)

