from django import forms
from .models import Topic, Thread

class NewTopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['name', 'description']

class NewThreadForm(forms.ModelForm):
    # initial thread post message
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'A message'}
        ),
        max_length=2000,
        help_text='The max length of the message is 2000 characters')

    class Meta:
        model = Thread
        fields = ['name', ]