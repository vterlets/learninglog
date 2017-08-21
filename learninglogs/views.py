from django.shortcuts import render, get_object_or_404, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.utils import timezone

# Create your views here.

def index(request):
    """The home page for learning logs, request"""
    topics = Topic.objects.all()
    return render(request, 'learninglogs/index.html', {'topics': topics})

def topic_entries(request, pk):
    """Page with topic's entries"""
    topic = get_object_or_404(Topic, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.topic_id = pk # learninglogs_entry.topic_id may not be NULL
            entry.date_added = timezone.now()
            entry.save()
            return redirect('learninglogs:topic_entries', pk=topic.pk)
    else:
        form = EntryForm()
    return render(request, 'learninglogs/show_entries.html', {'topic': topic, 'form': form})

def topic_new(request):
    """For to add new topics"""
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.date_added = timezone.now()
            topic.save()
            return redirect('learninglogs:topic_entries', pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'learninglogs/topic_new.html', {'form': form})

# def entry_new(request):
#     """For to add new entries for topic"""
#     if request.method == "POST":
#         form = EntryForm(request.POST)
#         if form.is_valid():
#             entry = form.save(commit=False)
#             entry.date_added = timezone.now()
#             entry.save()
#             return redirect('learninglogs:topic_entries', pk=topic.pk)
#     else:
#         form = EntryForm()
#     return render(request, 'learninglogs/entry_new.html', {'form': form})
