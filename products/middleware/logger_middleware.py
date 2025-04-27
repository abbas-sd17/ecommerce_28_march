import logging


class LoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"➡️ Incoming request path: {request.path}")
        response = self.get_response(request)
        print(f"⬅️ Outgoing response status: {response.status_code}")
        logger = logging.getLogger(__name__)
        logger.info(f"➡️ Incoming request path: {request.path}")
        return response

