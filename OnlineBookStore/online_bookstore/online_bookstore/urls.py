from django.contrib import admin
from django.urls import path, include
from bookstore.views import home, login_page,review_page,shopping_page,fiction_page,book_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookstore/', include('bookstore.urls')),
    path('', home, name='home'),
    path('login/', login_page, name='login'), 
    path('review/', review_page, name='review'), 
    path('shopping/', shopping_page, name='shopping'),
    path('fiction/', fiction_page, name='fiction'),
    path('search/', book_search, name='search_results'),
   
    # URL pattern for login.html
]
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
