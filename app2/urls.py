from django.urls import path
from . import views
urlpatterns = [
    path('devops/',views.renderHtml)
]
