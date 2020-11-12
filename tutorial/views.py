from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import AddTopicForm
from .models import AddMainTopic, AddSubTopic, Image

def index(request):
    template = loader.get_template('tutorial/index.html')
    return HttpResponse(template.render({}, request))

def cplusplus(request):
    topics = AddMainTopic.objects.filter(language="cplusplus")
    template = loader.get_template('tutorial/cplusplus.html')
    for topic in topics:
        print(topic.addsubtopic_set.all())
    return HttpResponse(template.render({'topics':topics}, request))

def addtopic(request):
    if request.method == "POST":
        form = AddTopicForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            Data = form.data
            topictype = Data['topictype']
            topicname = Data['topicname']
            description = Data['description']
            syntax = Data['syntax']
            example = Data['example']
            output = Data['output']
            if topictype == "maintopic":
                print("maintopic")
                mt = AddMainTopic.objects.filter(topicname = topicname)
                if not mt:
                    info = AddMainTopic(language="cplusplus", topicname=topicname, topictype=topictype, description=description, syntax=syntax, example=example, output=output)
                    if info:
                        info.save()
                else:
                    print("coming ro")
            elif topictype == "subtopic":
                maintopic = Data["maintopic"]
                mt = AddMainTopic.objects.filter(topicname = maintopic)
                if mt:
                    sr = AddSubTopic.objects.filter(topicname = topicname)
                    if not sr:
                        info = AddSubTopic(maintopic = mt.first(), topicname=topicname, topictype=topictype, description=description, syntax=syntax, example=example, output=output)
                        if info:
                            info.save()
        return HttpResponseRedirect("/addtopic/")

    else:
        form = AddTopicForm()
        topics = AddMainTopic.objects.all()
        subtopics = AddSubTopic.objects.all()
    
    template = loader.get_template('tutorial/addtopic.html')
    return HttpResponse(template.render({"form":form, "topics":topics, "subtopics":subtopics}, request))
