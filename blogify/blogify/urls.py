from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', views.news_page, name='news_page'),
    path('news/detail/<int:post_id>/', views.news_detail_page, name='news_detail_page'),
    path('', views.news_page, name='home_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
