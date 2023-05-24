from django.shortcuts import render
from django.views import View
from opcuaAPI.models import MainCylinderStateModel, AuxiliaryCylinderStateModel

class SupervisoryControl(View):
    def get(self, request):
        context = self.__get_data_from_db()
        return render(request, "control/control_page.html", context)


    def __get_data_from_db() -> dict:
        try:
            cyl_1 = MainCylinderStateModel.objects.get(id=1)
            cyl_2 = AuxiliaryCylinderStateModel.objects.get(id=1)
        except MainCylinderStateModel.DoesNotExist or AuxiliaryCylinderStateModel.DoesNotExist:
            context = {
                "X1": "NaN",
                "Y1": "NaN",
                "YN1": "NaN",
                "X2": "NaN",
                "XN2": "NaN",
                "Y2": "NaN"
            }
            return context
        
        context = {
            "X1": cyl_1.x1,
            "Y1": cyl_1.y1,
            "YN1": cyl_1.yn1,
            "X2": cyl_2.x2,
            "XN2": cyl_2.xn2,
            "Y2": cyl_2.y2
        }
        return context