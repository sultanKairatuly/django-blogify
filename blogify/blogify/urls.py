from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path
from blogs import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>/', views.movie_detail_page, name='movies_detail'),
    path('', views.movies_page, name='home_page'),
    path('signup/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_page'),
    path('top/', views.top_page, name='top_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
