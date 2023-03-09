from django.shortcuts import render
from .models import gallery as model_gallery
from appgallery.forms import GalleryForm

# Create your views here.
def gallery(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = GalleryForm()
    images = model_gallery.objects.all()
    return render(request, 'gallery/index.html',{'form': form,'images': images})