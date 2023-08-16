from django.urls import path
from . import views
urlpatterns = [
    path('notes/',views.NotesListView.as_view(),name='NotesList'),
    path('notes/<int:pk>',views.NotesDetailView.as_view(),name='notesDetails'),
    path('notes/<int:pk>/edit',views.NotesUpdateView.as_view(),name='notesUpdate'),
    path('notes/<int:pk>/delete',views.NotesDeleteView.as_view(),name='notesDelete'),
    path('notes/new',views.NotesCreateView.as_view(),name='newNotes'),
    
]
