from django.shortcuts import render, redirect
from .forms import UserFormDataForm


def user_form_view(request):
    if request.method == 'POST':
        form = UserFormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page or another view
    else:
        form = UserFormDataForm()
    return render(request, 'form.html', {'form': form})