def user(request):
    if hasattr(request, 'user'):
        return {'user':request.user }
    return {}

def user_authenticated(request):
    if hasattr(request, 'user'):
        if request.user.is_authenticated():
            return {'user_authenticated':True}
        else:
            return {'user_authenticated':False}
    return {{'user_authenticated':False}}