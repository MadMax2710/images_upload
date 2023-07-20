from django.shortcuts import render,redirect
from .form import ImageForm
from .models import Image
import os

# Create your views here.
def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        # перевірка чи форма для картинки правильна
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"index.html",{"obj":obj})
    else:
        form=ImageForm()
        img=Image.objects.all()
    return render(request,"index.html",{"img":img,"form":form})
def preview(request, pk):
    image = Image.objects.get(id=int(pk[0]))
    return render(request,"preview.html", {
        "caption" : image.caption,
        "type" : image.__format__,
        "image" : image.image.url,
        "id" : pk,
    } )
def delete_img(request, pk):
    image = Image.objects.get(id=pk)
    if len(image.image) > 0:
        # видалення з папки
        os.remove(image.image.path)
    # видалити зміну
    image.delete()
    return redirect("home")