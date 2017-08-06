from django.shortcuts import render, get_object_or_404
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """The home page for learning logs, request"""
    topics = Topic.objects.all()
    return render(request, 'learninglogs/index.html', {'topics': topics})

def topic_entries(request, pk):
    """Page with topic's entries"""
    #topic = Topic.objects.get(pk=pk)
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'learninglogs/show_entries.html', {'topic': topic})

def topic_new(request):
    """Form to add new topics"""
    form = TopicForm
    return render(request, 'learninglogs/topic_new.html', {'form': form})