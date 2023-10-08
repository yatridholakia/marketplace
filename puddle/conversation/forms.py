from django import forms
from .models import ChatMessage

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ("content",)
        labels = {
            "content" : "Message"
        }
        widgets = {
            "content" : forms.Textarea(attrs={
                "class" : "mt-2 w-full p-4 rounded-xl border h-20"
            })
        }