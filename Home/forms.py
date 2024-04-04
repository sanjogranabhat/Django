from django import forms
from .models import Student
from .models import Parent


class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll','city']
        
class UpdateStudentForm (forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','city']
        
        
class ParentCreationForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields =['name','address','age']

        
        
        
    