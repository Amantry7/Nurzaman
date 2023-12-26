from django.shortcuts import render
from apps.base import models
from apps.secondary.models import Slide, Parthers, Explanation,Gallery,Advantages1,Advantages2
from apps.contact.models import Contact
# Create your views here.
def index(request):
    settings = models.Settings.objects.latest('id')
    adres = models.Adres.objects.latest('id')
    slide = Slide.objects.latest('id')
    about = models.About.objects.latest('id')
    partners = Parthers.objects.all()
    explanation = Explanation.objects.all()
    galleru = Gallery.objects.all()
    advantages_1 = Advantages1.objects.all()
    advantages_2 = Advantages2.objects.all()
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact = Contact.objects.create(name = name, email = email, phone = phone)
    return render(request, 'base/index.html', locals())