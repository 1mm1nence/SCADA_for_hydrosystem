from rest_framework import serializers
from .models import MainCylinderStateModel, AuxiliaryCylinderStateModel, SystemStateModel

class MainCylinderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCylinderStateModel
        fields = ('id', 'x1', 'x_1', 'x_n1', 'y1', 'yn1')

class AuxiliaryCylinderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryCylinderStateModel
        fields = ('id', 'x2', 'xn2', 'y2')

class SystemStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemStateModel
        fields = ('id', 'xauto', 'xnext', 'xpause', 'xreset', 'xrun', 'xstep')