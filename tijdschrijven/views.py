from django.shortcuts import render
from .forms import GeeksForm
from django.forms import formset_factory


def geeks(request):
    context = {}

    # creating a formset and 5 instances of GeeksForm
    GeeksFormSet = formset_factory(GeeksForm, extra=3)
    formset = GeeksFormSet(request.POST or None)

    # print formset data if it is valid
    if formset.is_valid():
        for form in formset:
            print(form.cleaned_data)

    # Add the formset to context dictionary
    context['formset'] = formset
    return render(request, "geeks.html", context)
