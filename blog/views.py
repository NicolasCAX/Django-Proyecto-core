from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View,UpdateView,DeleteView
from .forms import PostCretaForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class blogListViews(View):
    def get(self, request, *agrs, **kagrs):
        posts = Post.objects.all()
        context={
            "posts":posts
        }
        return render(request, "blog_list.html", context)


class CreatePostView(View):
    def get(self, request, *agrs, **kagrs):
        form = PostCretaForm()
        context={
            "form":form
        }
        return render(request, "blog_create.html",context)
    def post(self, request, *agrs, **kagrs):
        if request.method=="POST":
            form = PostCretaForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get("title")
                content = form.cleaned_data.get("content")
                p, created = Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect("blog:home")
        context={

        }
        return render(request, "blog_create.html",context)


class blogDetalleView(View):
    def get(self,request,pk, *agrs, **kagrs):
        post = get_object_or_404(Post, pk=pk)
        context={
            "post":post
        }
        return render(request, "blog_detalle.html",context)

class blogUpdateView(UpdateView):
    model=Post
    fields=["title","content"]
    template_name="blogupdate.html"
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detalle',kwargs={"pk":pk})

class blogdelete(DeleteView):
    model=Post
    template_name="blogdelete.html"
    success_url=reverse_lazy("blog:home")

    