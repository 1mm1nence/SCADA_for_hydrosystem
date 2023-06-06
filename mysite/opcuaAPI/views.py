from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .models import MainCylinderStateModel, AuxiliaryCylinderStateModel, SystemStateModel, DesiredStateModel
from .serializers import MainCylinderStateSerializer, AuxiliaryCylinderStateSerializer, SystemStateSerializer, DesiredStateSerializer
from analysis.models import Cyl1_X1, Cyl1_XN1, Cyl1_Y1, Cyl1_YN1, Cyl2_X2, Cyl2_XN2, Cyl2_Y2, SystemStateTrack
from django.shortcuts import redirect

def get_or_none(model: models.Model):
    try:
        instance = model.objects.get(id=1)
    except model.DoesNotExist:
        instance = None
    return instance

def get_last_or_none(model: models.Model):
    try:
        instance = model.objects.order_by('-time_switch').first()
    except model.DoesNotExist:
        instance = None
    return instance

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

        xauto = request.data.get('XAUTO')
        xnext = request.data.get('XNEXT')
        xpause = request.data.get('XPAUSE')
        xreset = request.data.get('XRESET')
        xrun = request.data.get('XRUN')
        xstep = request.data.get('XSTEP')

        initial = request.data.get('initial')

        # Оновлення існуючих даних або створитворення екземплярів при їх відсутності.
        main_instance = get_or_none(MainCylinderStateModel)
        auxiliary_instance = get_or_none(AuxiliaryCylinderStateModel)
        system_instance = get_or_none(SystemStateModel)

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
            auxiliary_instance.save()
        else:
            auxiliary_instance = AuxiliaryCylinderStateModel.objects.create(x2=x2, xn2=xn2, y2=y2)

        if system_instance:
            system_instance.xauto = xauto
            system_instance.xnext = xnext
            system_instance.xpause = xpause
            system_instance.xreset = xreset
            system_instance.xrun = xrun
            system_instance.xstep = xstep
            system_instance.save()
        else:
            system_instance = SystemStateModel.objects.create(xauto=xauto, xnext=xnext, xpause=xpause, 
                                                            xreset=xreset, xrun=xrun, xstep=xstep)
        
        # Збереження історії для подальшого аналізу.
        pre_x1 = get_last_or_none(Cyl1_X1)
        if pre_x1 != x_1 and not initial:
            x1_track = Cyl1_X1.objects.create(state=x_1, initial=initial)

        pre_xn1 = get_last_or_none(Cyl1_XN1)
        if pre_xn1 != x_n1 and not initial:
            xn1_track = Cyl1_XN1.objects.create(state=x_n1, initial=initial)

        pre_y1 = get_last_or_none(Cyl1_Y1)
        if pre_y1 != y1 and not initial:
            xn1_track = Cyl1_Y1.objects.create(state=y1, initial=initial)
        
        pre_yn1 = get_last_or_none(Cyl1_YN1)
        if pre_yn1 != yn1 and not initial:
            yn1_track = Cyl1_YN1.objects.create(state=yn1, initial=initial)
        
        pre_x2 = get_last_or_none(Cyl2_X2)
        if pre_x2 != yn1 and not initial:
            yn1_track = Cyl2_X2.objects.create(state=x2, initial=initial)
        
        pre_xn2 = get_last_or_none(Cyl2_XN2)
        if pre_xn2 != yn1 and not initial:
            xn2_track = Cyl2_XN2.objects.create(state=xn2, initial=initial)
        
        pre_y2 = get_last_or_none(Cyl2_Y2)
        if pre_y2 != yn1 and not initial:
            y2_track = Cyl2_Y2.objects.create(state=y2, initial=initial)
        
        pre_xrun = get_last_or_none(SystemStateTrack)
        if pre_xrun != xrun:
            xrun_track = SystemStateTrack.objects.create(state=xrun)

        # Повернення відповіді з серіалізованими даними для оновлених/створених екземплярів моделей.
        serializer1 = MainCylinderStateSerializer(main_instance)
        serializer2 = AuxiliaryCylinderStateSerializer(auxiliary_instance)
        serializer3 = SystemStateSerializer(system_instance)

        serializer_list = [serializer1.data, serializer2.data, serializer3.data]
        response_content = {
            'status': 1, 
            'responseCode' : status.HTTP_200_OK, 
            'data': serializer_list,
        }

        return Response(response_content)
    

class ShareData(APIView):
    def get(self, request):
        main_instance = get_or_none(MainCylinderStateModel)
        auxiliary_instance = get_or_none(AuxiliaryCylinderStateModel)
        state_instance = get_or_none(SystemStateModel)

        # Підготовка серіалізаторів для актуальних даних з циліндрів.
        serializer1 = MainCylinderStateSerializer(main_instance)
        serializer2 = AuxiliaryCylinderStateSerializer(auxiliary_instance)
        serializer3 = SystemStateSerializer(state_instance)
        serializer_list = [serializer1.data, serializer2.data, serializer3.data]

        # Формування словнику, який надішлесться як JSON.
        response_content = {
            'status': 1, 
            'responseCode' : status.HTTP_200_OK, 
            'data': serializer_list,
        }

        return Response(response_content)

def stop_button(request):
    desired_instance = get_or_none(DesiredStateModel)
    if desired_instance:
            desired_instance.xpause_desired = True
    else:
        desired_instance = DesiredStateModel.objects.create(xpause_desired=True)
    return redirect('control:main')

class ShareDesired(APIView):
    def get(self, request):
        desired_state = get_or_none(DesiredStateModel)

        serializer = DesiredStateSerializer(desired_state)
        # if desired_state:
        #     serializer = DesiredStateSerializer(desired_state)
        # else:
        #     serializer = None
        serializer_data = serializer.data
        response_content = {
            'status': 1, 
            'status_code' : status.HTTP_200_OK, 
            'data': serializer_data
        }
        return Response(response_content)
    
    # def get(self, request):
    #     desired_done = request.desired_done
    #     if desired_done:
    #         desired_state = DesiredStateModel.objects.get(id=1)
    #         desired_state.delete()


class ClearDesired(APIView):
    def post(self, request):
        desired_done = request.desired_done
        if desired_done:
            desired_state = DesiredStateModel.objects.get(id=1)
            desired_state.delete()

        response_content = {
            'status': 1, 
            'status_code' : status.HTTP_200_OK, 
        }
        return Response(response_content)
    # def post(self, request):
    #     desired_state = get_or_none(DesiredStateModel)
    #     if desired_state:
    #         serializer = DesiredStateSerializer(desired_state)
    #     else:
    #         serializer = None
    #     response_content = {
    #         'status': 1, 
    #         'status_code' : status.HTTP_200_OK, 
    #         'data': serializer,
    #     }
    #     return Response(response_content)