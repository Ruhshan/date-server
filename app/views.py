from django.http import JsonResponse
import datetime

# Create your views here.
def current_date(request):
    print("Received request")
    return JsonResponse({"date": datetime.datetime.now().astimezone().strftime("%a %b %d %I:%M:%S %Z %Y")})
