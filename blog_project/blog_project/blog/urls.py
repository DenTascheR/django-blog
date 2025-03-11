from django.urls import path
from .views import home, article_detail, add_comment, CreateArticleView

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:pk>/', article_detail, name='article_detail'),
    path('article/<int:pk>/comment/', add_comment, name='add_comment'),
    path('article/create/', CreateArticleView.as_view(), name='create_article'),
]
