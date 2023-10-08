from django.shortcuts import render, redirect, get_object_or_404
from .forms import ChatMessageForm
from item.models import Item
from .models import Chat
from django.contrib.auth.decorators import login_required

@login_required
def new_chat(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect("dashboard:dashboard")

    chats = Chat.objects.filter(item=item).filter(members__in=[request.user.id])

    if chats:
        return redirect("chat:chat", pk=chats.first().id)

    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat = Chat.objects.create(item=item)
            chat.members.add(request.user)
            chat.members.add(item.created_by)
            chat.save()

            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            return redirect("chat:chat", pk=chat.id)
    else:
        form = ChatMessageForm()

    return render(request, "new_chat.html", {"form":form, "item_id" : item_pk, "item": item})

@login_required
def inbox(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    return render(request, "inbox.html", {"chats" : chats})
    
@login_required
def chat(request, pk):
    chat = Chat.objects.filter(members__in=[request.user.id]).get(pk=pk)
        
    if request.method == "POST":
        form = ChatMessageForm(request.POST)

        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.chat = chat
            chat_message.created_by = request.user
            chat_message.save()

            chat.save()

            return redirect("chat:chat", pk=pk)
    else:
        form = ChatMessageForm()

    return render(request, "chat.html", {
        "chat" : chat,
        "form" : form,
    })