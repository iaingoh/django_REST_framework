from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DataSerializer
from .models import JsonDataPoint
import json
import os


def load_json_file(request):
    with open('expose_data/resources/doctype_data.json') as f:
        data = json.load(f)

    for object in data:
        x = JsonDataPoint.objects.create(name=object['name'], total_docs=object['total_docs'])
        x.save()

    return HttpResponse('<h3>The view is loaded</h3>')


# pipenv install djangorestframework
# List all data
# call_data/

class DataList(APIView):

    def get(self, request):
        data_point = JsonDataPoint.objects.all()
        serializer = DataSerializer(data_point, many=True)
        return Response(serializer.data)



