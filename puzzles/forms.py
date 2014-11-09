from django import forms

class QuestionForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    level = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))
    image = forms.FileField(label ='choose an image')
    answer = forms.CharField(widget=forms.TextInput(attrs={'class' : 'key-text'}))

class AnswerForm(forms.Form):	
	key = forms.CharField(required=True,widget=forms.TextInput(attrs={'id':'answer-id', 'name':'user_answer'}))