# mysite/urls.py

from django.contrib import admin
from django.urls import path
from farmsupport import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', views.chatbot_view, name='chatbot'),  # Link to chatbot view
]





