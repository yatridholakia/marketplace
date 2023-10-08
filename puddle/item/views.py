from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from item.models import Item, Category
from .forms import NewItemForm, EditItemForm
from django.contrib.auth.decorators import login_required

def browse(request):
    query = request.GET.get("query", "")
    category_id = request.GET.get("category", 0)
    order = request.GET.get("order", "")
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    
    if order:
        items = items.order_by(order)

    return render(request, "browse.html", {
        "items" : items,
        "query" : query,
        "categories" : categories,
        "category_id" : int(category_id),
        "order" : order,
        })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, "detail.html", {
        "item" : item,
        "related_items" : related_items,
    })

@login_required
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect("item:detail", pk=item.id)
    form = NewItemForm()
    return render(request, "item_form.html", {
        "form": form,
        "title": "New Item",
        })

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()

            return redirect("item:detail", pk=item.id)
    form = EditItemForm(instance=item)
    return render(request, "item_form.html", {
        "form": form,
        "title": "Edit Item",
        })

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:dashboard")