from django.shortcuts import render


def user_main(request):
    return render(request, 'users/user_main.html')
