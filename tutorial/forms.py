from django import forms

from .models import AddMainTopic

class AddTopicForm(forms.Form):
    CHOICES = (('maintopic', 'Main Topic'),('subtopic', 'Sub Topic'),)
    topictype = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'class':'inputbox', 'onchange':"select_item(this)"}))
    mts = AddMainTopic.objects.all()
    chs = (("Select main topic", "Select main topic"),)
    for mt in mts:
        print(dir(mt))
        tn = mt.topicname
        tt = ((tn, tn))
        chs += (tt,)
    maintopic = forms.CharField(widget=forms.Select(choices=chs, attrs={'class':'inputbox'}))
    lgs = (("cplusplus", "C++"), ("python", "Python"), ("c", "C"), ("shell", "Shell Script"),)
    language = forms.CharField(widget=forms.Select(choices=lgs, attrs={'class':'inputbox'}))

    topicname =  forms.CharField(required=True, max_length=1000,widget=forms.TextInput(attrs={'autocomplete':'off', 'id':'topicname','class': "inputbox"}))
    description = forms.CharField(max_length=10000, required=False, widget=forms.Textarea(attrs={'class': "textareabox"}))
    syntax = forms.CharField(max_length=10000, required=False, widget=forms.Textarea(attrs={'class': "textareabox"}))
    example = forms.CharField(max_length=10000, required=False, widget=forms.Textarea(attrs={'class': "textareabox"}))
    output = forms.CharField(max_length=10000, required=False, widget=forms.Textarea(attrs={'class': "textareabox"}))
    images = forms.FileField(required=False, widget=forms.FileInput(attrs={"multiple":True, "accept":'image/x-png,image/gif,image/jpeg', 'onchange':"selected_files(this, 'displayimages')"}))
