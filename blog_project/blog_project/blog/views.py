from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from .models import Article, Comment, Category

def home(request):
    articles = Article.objects.filter(status='published').order_by('-created_at')
    return render(request, 'blog/home.html', {'articles': articles})

@login_required
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

@login_required
def add_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(article=article, author=request.user, content=content)
            messages.success(request, 'Коментар додано!')
    return redirect('article_detail', pk=pk)

class CreateArticleView(View):
    def get(self, request):
        return render(request, 'blog/create_article.html')
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        category_id = request.POST.get('category')
        status = request.POST.get('status')
        category = get_object_or_404(Category, id=category_id)
        Article.objects.create(title=title, content=content, category=category, status=status, author=request.user)
        return redirect('home')
