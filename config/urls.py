from django.contrib import admin
from django.urls import path
from blog.views import post_list, post_edit, post_detail, post_delete
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list, name='post_list'),
    path('detail/<uuid:id>/', post_detail, name='post_detail'),
    path('edit/<uuid:id>/', post_edit, name='post_edit'),
    path('delete/<uuid:id>/', post_delete, name='post_delete'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
]