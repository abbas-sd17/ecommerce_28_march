from django.http import JsonResponse

class GeoBlockingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        print(f"Incoming IP: {ip_address}")

        # Allow only localhost
        if ip_address != '127.0.0.1':
            return JsonResponse({"error": "Access Denied from your location."}, status=403)

        response = self.get_response(request)
        return response
