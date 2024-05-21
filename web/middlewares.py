from lib.common import get_user

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
        access_token = request.COOKIES.get('access_token', '')
        refresh_token = request.COOKIES.get('refresh_token', '')
        user = get_user(access_token)
        # if not user['is_authenticated'] and refresh_token:
        #     access_token = refresh_access_token(refresh_token)
        #     user = get_user(access_token)
        if access_token:
            request.api_headers = {
                'Authorization' : f"Bearer {access_token}"
            }
        else:
            request.api_headers = {}
        if user['is_authenticated']:
            request.token = access_token
        else:
            request.token = ''
        request.user = user
        return None