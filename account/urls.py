from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from shop import views as v

urlpatterns = [
 path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('', v.product_list, name='product_list'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
