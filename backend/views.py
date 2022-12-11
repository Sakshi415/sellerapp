from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Create 
from .seriallizers import CreateSerializer 

# Create your views here.

def index(request):
    return HttpResponse("Seller app Created")


class Summary_created(APIView):
# Get information about all the created jobs
    def get(self, request, format=None):
        a = Create.objects.all()
        serializer = CreateSerializer(a, many=True)
        return Response(serializer.data) 