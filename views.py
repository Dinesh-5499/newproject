from django.shortcuts import redirect, render
from .forms import CamForm
from .models import Camera


# Create your views here.
def add_detail(request):
    if request.method == 'POST':
        form = CamForm(request.POST)
        if form.is_valid():
            form.save()
             
            return redirect('add_detail')


        return render(request,'CamApp/add_detail.html',{'form':form})

    else:
        form = CamForm()
        context = {'form':form}
        return render(request,'CamApp/add_detail.html',context)

def all_cams(request):
    context = Camera.objects.all()
    return render(request,'CamApp/all_cams.html',{'context':context})