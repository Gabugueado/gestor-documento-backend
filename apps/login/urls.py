from django.urls import path

from .views import UserInfoView

app_name='login'

urlpatterns = [
    # Otras rutas de tu aplicación
    path('userinfo/', UserInfoView.as_view(), name='userinfo'),
]
