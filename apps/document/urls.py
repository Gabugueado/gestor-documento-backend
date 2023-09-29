from django.urls import path
from .views import DocumentListView,  DocumentCreateView, DocumentDeleteView, DocumentUpdateView, DocumentBase64View

app_name = 'docs'

urlpatterns = [
    path('list/', DocumentListView.as_view(), name='document-list'),
    path('detail/<int:document_id>/', DocumentBase64View.as_view(), name='document-base64'),
    path('create/', DocumentCreateView.as_view(), name='document-create'),
    path('delete/<int:pk>/', DocumentDeleteView.as_view(), name='document-delete'),
    path('update/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),


]