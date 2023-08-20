import functools
from django.shortcuts import redirect
from django.contrib import messages

def login_required(view_func, redirect_url="/user/login/"):
    """
        this decorator ensures that a user is not logged in,
        if a user is logged in, the user will get redirected to 
        the url whose view name was passed to the redirect_url parameter
    """
    @functools.wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        print(request.user)
        if not request.user['is_authenticated']:
            return redirect(redirect_url)
        else:
            return view_func(self, request,*args, **kwargs)
    return wrapper