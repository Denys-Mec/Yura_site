from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import FormView

from django.urls import reverse
from django.views import generic
# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Author, Article
from .forms import FormUpdateArticle

from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ArticleView(APIView):
    def get(self, request):
        output = [
            {
                "name" : output.name,
                "author" : Author.objects.get(pk=output.author),
                "content" : output.content,
                "date" : output.date
            } for output in Article.objects.all()
        ]
        return Response(output)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return(serializer.data)

def Myadmin(request):
    template = loader.get_template("myadmin.html")
    return HttpResponse(template.render(None, request))

def show_all(request):

    # list = Article.objects.all()
    # list = list[:4]
    # for i in list:
    #     if len(i.content)>150:
    #         i.content = i.content[:147] + '...'
    template = loader.get_template("news/show.html")
    context = {
    "list" : Article.objects.all(),
    }
    return HttpResponse(template.render(context, request))

def show_item(request, id:int):

    print("id:" + id)
    item = Article.objects.get(id=id)

    template = loader.get_template("news/show-item.html")
    context = {
    "item" : item,
    }
    return HttpResponse(template.render(context, request))

# def edit_article(request, article:Article):
#     if request.method == 'POST':
#         print(request.POST)
#         name = request.POST['name']
#         author = request.POST['author']
#         content = request.POST['content']
#         date = request.POST['date']
#         article = Article(
#                 name = name,
#                 author = author,
#                 content = content,
#                 date = date,
#             )
#         print(Article)
#     context ={}

#     # create object of form
#     form = FormUpdateArticle(instance=article)

#     # check if form data is valid
#     if form.is_valid():
#         # save the form data to model
#         form.save()

#     context['form']= form
#     return render(request, "news/editor.html", context)

# def update_article(request, id:int):
#     return edit_article(request, Article.objects.get(pk=id))

# def add_new_article(request):
#     return edit_article(request, Article())


class UpdateArticleView(UpdateView): # new
    model = Article
    form_class = FormUpdateArticle
   
    # fields = ["name", "author", "content", "date"]
    template_name = 'news/editor.html'
    success_url = reverse_lazy('news')

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'news/delete.html'
    success_url = reverse_lazy('news')

class CreateArticleView(CreateView):
    model = Article
    form_class = FormUpdateArticle
    # fields = '__all__'
    template_name = 'news/editor.html'
    success_url = reverse_lazy('news')

#########################################################################
#
# class FormUpdateArticleView(generic.CreateView):
#     def post(self, request):
#         form_class = FormUpdateArticle
#         # form_class.instance = Article.objects.all()[0]
#         template_name = "editor.html"
#         login_url = 'login'
#         success_url = "/"
#         success_message = "Your blog has been created"




# class ArticleDetailView(DetailView, FormView):
#     """Article detail view."""
#
#     # model = Article
#     form_class = CommentForm
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["form"] = CommentForm()
#         context["comments"] = self.get_object().comments.all()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form = CommentForm(request.POST, request.FILES)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.article = self.get_object()
#             comment.save()
#         success_url = reverse("article-detail", kwargs={"pk": self.get_object().id})
#         return HttpResponseRedirect(success_url)
