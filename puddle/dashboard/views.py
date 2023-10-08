from django.shortcuts import render
from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    items = Item.objects.filter(created_by = request.user)
    return render(request, "dashboard.html", {
        'items' : items,
    })