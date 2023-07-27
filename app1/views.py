from django.shortcuts import render
from .models import Model1, Model2, Model3
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Model1Serializer

# Create your views here.
def fun1(request):
    # inner join between model2 and model3
    data1 = Model3.objects.select_related('field10').all()

    # left outer join between model2 and model3
    data2 = Model2.objects.prefetch_related('model3_set').all()
    return HttpResponse(data1[0].field10.field7)

# creating function based postapi just to perform the django validation
@api_view(['POST'])
def create_model1(request):
    serializer = Model1Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(status=400)
