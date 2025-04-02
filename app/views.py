from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, View
from .models import Note
from .tasks import task_do_something

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

        task_do_something() # contoh proses panjang, hanya masuk queue lom diexec
        Note.objects.create(title=title, content=content, user=request.user)
        return redirect("index")