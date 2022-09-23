from .models import folder, image
from rest_framework.serializers import ModelSerializer

class folderSer(ModelSerializer):
    class Meta:
        model = folder
        fields = '__all__'

class imageSer(ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'