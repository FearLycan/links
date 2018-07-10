from django.shortcuts import render, redirect
from app.models.forms import LinkForm


def index(request):
    model = LinkForm()

    if request.method == 'POST':
        model = LinkForm(request.POST)
        if model.is_valid():
            form = model.save(commit=False)
            form.author = request.user
            form.hash = form.random_hash()
            form.save()

            return redirect('app:homepage')

    return render(request, 'homepage/index.html', {
        'form': model
    })
