from django import forms
from django.forms import Textarea
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Article


class FormUpdateArticle(forms.ModelForm):
	# name = forms.CharField(
 #        max_length=255,
 #        null=True,
 #        blank=True,
 #        help_text="Use puns liberally",
 #    )
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Article
        fields = ["name", "content"]
        # widgets = {
        #     "name": forms.CharField(max_lenght = 255),
        # }
        #exclude = ('date',)
        # widgets = {
        #     'foo': SummernoteWidget(),
        #     'bar': SummernoteInplaceWidget(),
        # }
