from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import StateModel
from .serializers import StateSerializer

# Create your views here.
def show_data(request):
    try:
        state = StateModel.objects.get(id=1)
    except StateModel.DoesNotExist:
        return render(request, 'opcuaAPI/index.html', {'y1': 'no value', 'yn1': 'no value'})
    context = {
        'y1': state.y1,
        'yn1': state.yn1
    }
    return render(request, 'opcuaAPI/index.html', context)


class Data(APIView):
    def post(self, request):
        y1 = request.data.get('Y1')
        yn1 = request.data.get('YN1')

        #write to db:
        try:
            my_model_instance = StateModel.objects.get(id=1)
        except StateModel.DoesNotExist:
            my_model_instance = None

        # Update the existing instance or create a new one if it doesn't exist
        if my_model_instance:
            my_model_instance.y1 = y1
            my_model_instance.yn1 = yn1
            my_model_instance.save()
        else:
            my_model_instance = StateModel.objects.create(y1=y1, yn1=yn1)

        # Return a response with the serialized data for the updated/created model instance
        serializer = StateSerializer(my_model_instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


