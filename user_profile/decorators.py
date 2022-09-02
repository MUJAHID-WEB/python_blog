from django.shortcuts import redirect


def not_logged_in_required(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_function(request, *args, **kwargs)

    return wrapper