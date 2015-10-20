from django import forms

class CommentForm(forms.Form):
    #match
    #user
    content = forms.TextField(label='Escribe un mensaje', max_length=500)