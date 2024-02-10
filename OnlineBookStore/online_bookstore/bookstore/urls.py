from django.urls import path
from . import views

app_name = 'bookstore'

urlpatterns = [
    path('', views.home, name='home'),  # Map the root URL to the home view
    path('login/', views.login_page, name='login'),
    path('review/', views.review_page, name='review'),
    path('shopping/', views.shopping_page, name='shopping'),
    path('fiction/', views.fiction_page, name='fiction'),
    path('search/', views.book_search, name='search_results'),
    
    # Add more paths for other views
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
