from lib.common import get_token, get_user, get_refresh_token

class AssignUser(object):
    def __init__(self, get_response):
        """
        One-time configuration and initialisation.
        """
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before the view (and later
        middleware) are called.
        """
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        Called just before Django calls the view.
        """
        access_token = get_token(request)
        refresh_token = get_refresh_token(request)
        user = get_user(access_token)
        print(user)
        # if not user['is_authenticated'] and refresh_token:
        #     access_token = refresh_access_token(refresh_token)
        #     user = get_user(access_token)
        if user['is_authenticated']:
            request.user = user
            request.token = access_token
        else:
            request.user = user
            request.token = ''
        return None