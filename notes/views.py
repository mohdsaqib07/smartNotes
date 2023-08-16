from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.shortcuts import render,HttpResponse,redirect
from django.http import Http404, HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Notes
from django.views.generic import ListView , DetailView , CreateView ,UpdateView
from django.views.generic.edit import DeleteView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
class NotesUpdateView(UpdateView):
    model = Notes 
    form_class = NotesForm 
    success_url = '/smart/notes'

class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title','notes']
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())



# ListView is used for displaying a list of items from the model .
class NotesListView(LoginRequiredMixin,ListView):
    model = Notes 
    # default model object name is page_obj 
    context_object_name = 'notes'
    # if the template name is following the standard name as class based view we don't need to send the name also 
    # template_name = './notes/display_notes.html'    
    login_url = '/login'

    def get_queryset(self):
        # queryset = super().get_queryset()
        # queryset = Notes.objects.filter(user=self.request.user)
        # return queryset
        return self.request.user.notes.all()


# Used for displaying details of a single item from the model 
class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/detail.html'
    # we don't need to handle the exception in class based view it will be automatically createad for us 

# def notes_details(request,pk):
#     try:
#         note = Notes.objects.get(sno=pk)
#     except Notes.DoesNotExist:
#         raise Http404('Notes Does note exist')
    
#     return render(request,'notes/detail.html',{'note':note})
    

