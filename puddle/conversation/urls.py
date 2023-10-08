from django.urls import path
from . import views

app_name = "chat"

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("new/<int:item_pk>", views.new_chat, name="new"),
    path("chat/<int:pk>", views.chat, name="chat"),
]