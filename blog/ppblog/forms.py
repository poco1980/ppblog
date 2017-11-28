from django import forms
from .models import Topic, Title

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class TitleForm(forms.ModelForm):
    class Meta:
        model = Title
        fields = ['text']
        labels = {'text': ''}
