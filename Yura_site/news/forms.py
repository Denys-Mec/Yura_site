from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Article


class FormUpdateArticle(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Article
        fields = "__all__"
        
        # exclude = ('date',)
        # widgets = {
        #     'foo': SummernoteWidget(),
        #     'bar': SummernoteInplaceWidget(),
        # }
