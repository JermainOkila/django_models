from django.shortcuts import render
from .forms import StudentForm


# Create your views here.
def contact(request):
    return render(request, 'contact.html')

def contact2(request):
    context= {}
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success_message'] = "Form submitted successfully"
    else:
        context['error_message'] = "Please correct the error below. Form submission failed."
        context['form'] = form
    return render(request, 'contact2.html', context)