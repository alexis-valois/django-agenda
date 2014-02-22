from django.shortcuts import render
from forms import UserCreateForm
from django.http import HttpResponseRedirect

def create_account(request):
    if request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/succes/')
    else:
        form = UserCreateForm()
    return render(request,'user/create.html', {'form':form})

