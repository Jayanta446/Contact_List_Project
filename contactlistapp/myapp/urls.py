from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('addcontact/', views.addContact, name='add-contact'),
    path('contact-details/<int:id>/', views.contactDetails, name = 'contact-details'),
    path('edit-contact/<int:id>/', views.editContact, name = 'edit-contact'),
    path('delete-contact/<int:id>/', views.deleteContact, name = 'delete-contact'),
]






