from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user and redirect
            user = form.save()

            # You may log in the user here if needed
            # login(request, user)

            # Redirect to the articles list after successful signup
            return redirect('articles:list')
    else:
        # If the request method is GET, display the form
        form = UserCreationForm()

    # Render the signup form template with the form
    return render(request, 'accounts/signup.html', {'form': form})
def login_view(request):
        if request.method == 'POST':
             form = AuthenticationForm(data=request.POST)
             if form.is_valid():
                   user = form.get_user()
                #    login(request, user)
                   return redirect('articles:list')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', { 'form': form })