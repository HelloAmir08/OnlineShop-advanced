from django.shortcuts import render, redirect
from .forms import ContactMessageForm

def about_us_view(request):
    return render(request, 'core/about.html')

def contact_us_view(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            print("message has successfully sent")
            return redirect("contact_us")
        else:
            print("something is wrong")
    else:
        form = ContactMessageForm()


    return render(request, 'core/contact.html', {'form': form})