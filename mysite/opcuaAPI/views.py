from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MainCylinderStateModel, AuxiliaryCylinderStateModel
from .serializers import MainCylinderStateSerializer, AuxiliaryCylinderStateSerializer

# def show_data(request):
#     try:
#         state = StateModel.objects.get(id=1)
#     except StateModel.DoesNotExist:
#         return render(request, 'opcuaAPI/index.html', {'y1': 'no value', 'yn1': 'no value'})
#     context = {
#         'y1': state.y1,
#         'yn1': state.yn1
#     }
#     return render(request, 'opcuaAPI/index.html', context)


class GetData(APIView):
    def post(self, request):
        x1 = request.data.get('X1')
        x_1 = request.data.get('X_1') 
        x_n1 = request.data.get('X_N1')
        y1 = request.data.get('Y1')
        yn1 = request.data.get('YN1')

        x2 = request.data.get('X2')
        xn2 = request.data.get('XN2')
        y2 = request.data.get('Y2')

        # Оновлення існуючих даних або створитворення екземплярів при їх відсутності.
        try:
            main_instance = MainCylinderStateModel.objects.get(id=1)
        except MainCylinderStateModel.DoesNotExist:
            main_instance = None

        try:
            auxiliary_instance = AuxiliaryCylinderStateModel.objects.get(id=1)
        except AuxiliaryCylinderStateModel.DoesNotExist:
            auxiliary_instance = None

        if main_instance:
            main_instance.x1 = x1
            main_instance.x_1 = x_1
            main_instance.x_n1 = x_n1
            main_instance.y1 = y1
            main_instance.yn1 = yn1
            main_instance.save()
        else:
            main_instance = MainCylinderStateModel.objects.create(x1=x1, x_1=x_1, x_n1=x_n1, y1=y1, yn1=yn1)
        
        if auxiliary_instance:
            auxiliary_instance.x2 = x2
            auxiliary_instance.xn2 = xn2
            auxiliary_instance.y2 = y2
        else:
            auxiliary_instance = AuxiliaryCylinderStateModel.objects.create(x2=x2, xn2=xn2, y2=y2)


        # Повернення відповіді з серіалізованими даними для оновлених/створених екземплярів моделей.
        serializer1 = MainCylinderStateSerializer(main_instance)
        serializer2 = AuxiliaryCylinderStateSerializer(auxiliary_instance)
        serializer_list = [serializer1.data, serializer2.data]
        response_content = {
            'status': 1, 
            'responseCode' : status.HTTP_200_OK, 
            'data': serializer_list,
        }

        return Response(response_content)
    



