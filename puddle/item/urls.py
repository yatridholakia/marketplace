from django.urls import path
from .views import detail, new_item, delete_item, edit_item, browse

app_name = "item"

urlpatterns = [
    path("", view=browse, name="browse"),
    path("<int:pk>/", view=detail, name="detail"),
    path("new-item/", view=new_item, name="new_item"),
    path("delete/<int:pk>/", view=delete_item, name="delete_item"),
    path("edit/<int:pk>/", view=edit_item, name="edit_item"),

]