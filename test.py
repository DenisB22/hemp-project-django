def logout_user(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login_user')


class LogoutUser(View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, 'You are logged out.')
        return redirect('login_user')


'''
https://dev.to/dennisivy11/easily-convert-django-function-based-views-to-class-based-views-3okb
'''