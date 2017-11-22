from django.shortcuts import render
from .models import Topic, Title

def index(request):
    return render(request, 'ppblog/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'ppblog/topics.html', context)

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    titles = topic.title_set.order_by('-date_added')
    context = {'topic': topic, 'titles': titles}
    return render(request,'ppblog/topic.html')

def titles(request):
    titles = Title.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'ppblog/titles.html', context)

def title(request, title_id):
    title = Title.objects.get(id=title_id)
    entries = title.entry_set.order_by('-date_added')
    context = {'title': title, 'entries': entries}
    return  render(request, 'ppblog/title.html', context)
