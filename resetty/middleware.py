class ResetPasswordMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # here your process_request middleware
        print("Hola mundo")
        response = self.get_response(request)
        return response

