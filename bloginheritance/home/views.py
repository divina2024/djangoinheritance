from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Article
from .forms import form1 
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import form1
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError


def index(request):
    articles = Article.objects.all()  # Assuming you have an Article model with title, body, link_url, image_url fields
    return render(request, 'index.html', {'articles': articles})

def about_me(request):
    return render(request, 'about-me.html')


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})

def article_detail(request, id):
    # Retrieve the article based on the ID or return a 404 error if not found
    article = get_object_or_404(Article, id=id)
    return render(request, 'article.html', {'article': article})


def add_posts(request):
    form = form1()
    return render(request, 'add_posts.html',{'form': form})




def form_view(request): 
    if request.method == 'POST':
        form = form1(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = form1()
    return render(request, "add_posts.html", {'form': form}) 




def edit_article(request, article_id):
    # Retrieve the article object
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        # Retrieve form data
        title = request.POST.get('title')
        body = request.POST.get('body')
        
        # Handle image upload
        if 'image' in request.FILES:
            image = request.FILES['image']
            article.image = image
        
        # Update article fields
        article.title = title
        article.body = body
        article.save()

        return redirect('/')
           
    return render(request, 'edit_article.html', {'article': article})




 
def delete_article(request, article_id):

    dele= get_object_or_404(Article, id=article_id)
    dele.delete()
    return redirect('/')
