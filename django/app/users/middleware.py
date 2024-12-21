from django.utils.deprecation import MiddlewareMixin
from .utils import check_cookie, set_cookie


class CookieMiddleware(MiddlewareMixin):
    max_age = 60

    def process_response(self, request, response):
        if not check_cookie(request):
            set_cookie(request, response, self.max_age)
        return response
