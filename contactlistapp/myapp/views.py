from django.shortcuts import render, redirect
from .models import ContactModel

def home_page(request):
    contacts = ContactModel.objects.order_by("name")
    if request.method == 'POST':
        search_input = request.POST['search-area']
        contacts = ContactModel.objects.filter(name__icontains = search_input)
        return render(request, 'myapp/index.html', {'contact':contacts, 'search_input':search_input})
    return render(request, 'myapp/index.html', {'contact':contacts, 'search_input':''})

def addContact(request):
    if request.method == 'POST':
        name = request.POST['fullname']
        relation = request.POST['relationship']
        phone = request.POST['phone-number']
        address = request.POST['address']
        email = request.POST['email']
        contact_obj = ContactModel(name = name, relationship = relation, email = email, phone_number = phone, address = address)
        contact_obj.save()
        return redirect('/')
    return render(request, 'myapp/new.html')

def contactDetails(request, id):
    details = ContactModel.objects.get(id = id)
    return render(request, 'myapp/contact-details.html', {'details':details})

def editContact(request, id):
    contact = ContactModel.objects.get(id = id)
    if request.method == 'POST':
        contact.name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.email = request.POST['email']
        contact.save()
        return redirect('/contact-details/' + str(id))
    return render(request, 'myapp/edit.html', {'contact':contact})

def deleteContact(request, id):
    contact = ContactModel.objects.get(id = id)
    contact.delete()
    return redirect('/')




