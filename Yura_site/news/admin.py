from django.contrib import admin
from .models import *
from django import forms

from ckeditor.widgets import CKEditorWidget
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Author)


class articleAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Article, articleAdmin)
# Register your models here.
#
# class PostAdminForm(forms.ModelForm):
#     content = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Blog
#
# class PostAdmin(admin.ModelAdmin):
#     form = PostAdminForm
#     admin.site.register(Blog, PostAdmin)
