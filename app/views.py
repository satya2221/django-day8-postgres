from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Note

# Create your views here.
class NoteListView(ListView):
    model = Note
    template_name = "index.html"
    context_object_name = "notes"

class NoteDetailView(DetailView):
    model = Note
    template_name = "preview.html"
    context_object_name = "note"

class NoteCreateView(View):
    def get(self, request):
        return render(request, "form.html")
    
    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        Note.objects.create(title=title, content=content)
        return redirect("index")