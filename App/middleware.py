from django.http import HttpResponseForbidden

class RestrictSettingsAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if '.py' in request.path.lower():
            return HttpResponseForbidden("Access is restricted.")
        return self.get_response(request)