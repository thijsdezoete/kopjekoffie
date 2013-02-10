from models import Article
from django.forms import ModelForm


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ('link', 'name', 'tags')
    #subject = forms.CharField(max_length=100)
    #message = forms.CharField()
    #sender = forms.EmailField()
    #cc_myself = forms.BooleanField(required=False)
