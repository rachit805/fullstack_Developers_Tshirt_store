from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Django React Web app', 'name': "Rachit" })