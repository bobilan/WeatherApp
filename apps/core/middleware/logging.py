from apps.weather.logging import Logging
from config.settings.base import BASE_DIR
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin

logging = Logging(str(BASE_DIR / "logs" / "req_res_logs.txt")) # Changed here


def simple_logging_middleware(get_response):
    def middleware(request):
        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers['Content-Type']
        user_agent = request.headers['User-Agent']
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"

        if request.POST:
            post_data = request.POST
            msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent} searched: {post_data['search_bar']}"
        # post_data = request.get_post_data()

        # msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        logging.info(msg)

        response = get_response(request)

        return response
    return middleware


class ViewExecutionTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = timezone.now()

        response = self.get_response(request)

        total_time = timezone.now() - start_time

        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()

        msg = f" EXECUTION TIME 2  {total_time} >> {http_method} | {host_port}{url}"

        logging.info(msg)

        return response


class ViewExecutionTimeSecondMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = timezone.now()

    def process_response(self, request, response):
        total_time = timezone.now() - request.start_time

        http_method = request.method
        url = request.get_full_path()
        host_port = request.get_host()

        msg = f" EXECUTION TIME {total_time} >> {http_method} | {host_port}{url}"

        logging.info(msg)

        return response
