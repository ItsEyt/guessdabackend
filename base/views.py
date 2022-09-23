from django.http import JsonResponse
from .models import image, folder
from .serializers import folderSer, imageSer

# Create your views here.

from django.http import JsonResponse

def index(req):
    return JsonResponse('hello', safe=False)

def getFolder(req, id=-1):
    if id > -1:
        return JsonResponse(folderSer(folder.objects.get(id = id)).data,safe=False)

def getImage(req, id=-1):
    if id > -1:
        return JsonResponse(imageSer(image.objects.get(id = id)).data,safe=False)