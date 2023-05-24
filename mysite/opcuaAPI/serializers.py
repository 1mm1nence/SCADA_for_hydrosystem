from rest_framework import serializers
from .models import MainCylinderStateModel, AuxiliaryCylinderStateModel

class MainCylinderStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCylinderStateModel
        fields = ('id', 'x1', 'x_1', 'x_n1', 'y1', 'yn1')

class AuxiliaryCylinderStateModel(serializers.ModelSerializer):
    class Meta:
        model = AuxiliaryCylinderStateModel
        fields = ('id', 'x2', 'xn2', 'y2')
