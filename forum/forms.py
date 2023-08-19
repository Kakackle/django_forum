from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['name', 'description']