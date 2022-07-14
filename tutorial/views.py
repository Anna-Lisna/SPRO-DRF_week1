from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

from rest_framework.status import HTTP_201_CREATED
from rest_framework.views import APIView
from tutorial.models import Store
from tutorial.serializers import StoreSerializer


@api_view(['GET'])
def show_date(request):
    date = datetime.now()
    return Response({'date': date.strftime('%m/%d/%Y'), 'year': date.year, 'month': date.month, 'day': date.day})


@api_view(['GET'])
def show_msg(request):
    return Response({'msg': 'Hello World'})


@api_view(['GET'])
def show_my_name(request):
    name = request.query_params
    return Response({'name': name['name_of_hacker']})


@api_view(['POST'])
def calculator(request):
    data = request.data
    options = {
        'plus': lambda a, b: (a + b),
        'minus': lambda a, b: (a - b),
        'divide': lambda a, b: (a / b),
        'multiply': lambda a, b: (a * b)
    }

    number1 = data['number1']
    number2 = data['number2']
    option = data['option']
    if option not in options:
        result = 'Enter option from plus, minus, divide, multiply'
    elif (type(number1) != int) or (type(number2) != int):
        result = 'Not a number. Enter a number'
    elif option == 'divide' and number2 == 0:
        result = 'Division for 0 not allowed'
    else:
        result = options[option](int(number1), int(number2))
    return Response({"result": result})


class Stores(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response({'stores': serializer.data})

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_201_CREATED, data=serializer.data)
