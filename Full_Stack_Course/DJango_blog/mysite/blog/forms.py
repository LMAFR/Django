from django import forms
from blog.models import Comment, Post

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author", "title", "text")

        widgets = {
            # The class key we will call in the lines belows have css classes as values: 
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            # In the line below the attributes are the same than in PostForm (excepting postcontent which is more suitable for Post only):
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
