from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render
from users.forms import LoginForm


def user_login(request):
    """
    View function for user login

    Accepts POST requests with valid user credentials, authenticates the user,
    and logs the user in if they are active.

    Args:
        request: HTTP request object

    Returns:
        HTTP response with success or error message
    """

    if request.method == 'POST':
        # If the form was submitted
        form = LoginForm(request.POST)

        if form.is_valid():
            # If the form data is valid
            cd = form.cleaned_data
            print(cd)

            # If authentication the user
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'],
                                )

            if user is not None:
                # If authentication was successful
                if user.is_active:
                    # if the user account is active, log them in
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    # If the user account is disabled
                    return HttpResponse('Disable account')
            else:
                # If authentication failed
                return HttpResponse('Invalid login')
    else:
        # If the form was not submitted, create a new form
        form = LoginForm()

    # render the login page with the form
    return render(request, 'user/login.html', {'form': form})
