from django.shortcuts import render
from django.views import View
from opcuaAPI.models import MainCylinderStateModel, AuxiliaryCylinderStateModel, SystemStateModel


class SupervisoryControl(View):
    def get(self, request):
        cyl_context = self.__get_cyl_data_from_db()
        sys_context = self.__get_sys_data_from_db()
        context = cyl_context | sys_context
        return render(request, "control/control_page.html", context)


    def __get_cyl_data_from_db(self) -> dict:
        try:
            cyl_1 = MainCylinderStateModel.objects.get(id=1)
            cyl_1_data = {
                "X1": cyl_1.x1,
                "Y1": cyl_1.y1,
                "YN1": cyl_1.yn1,
            }
        except MainCylinderStateModel.DoesNotExist:
            cyl_1_data = {
                "X1": "NaN",
                "Y1": "NaN",
                "YN1": "NaN",
            }

        try:
            cyl_2 = AuxiliaryCylinderStateModel.objects.get(id=1)
            cyl_2_data = {
                "X2": cyl_2.x2,
                "XN2": cyl_2.xn2,
                "Y2": cyl_2.y2
            }
        except AuxiliaryCylinderStateModel.DoesNotExist:
            cyl_2_data = {
                "X2": "NaN",
                "XN2": "NaN",
                "Y2": "NaN",
            }
        
        cylinders_data = cyl_1_data | cyl_2_data
        return cylinders_data
    
    def __get_sys_data_from_db(self) -> dict:
        try:
            sys_state = SystemStateModel.objects.get(id=1)
            sys_state_data = {
                "XAUTO": sys_state.xauto,
                "XNEXT": sys_state.xnext,
                "XPAUSE": sys_state.xpause,
                "XRESET": sys_state.xreset,
                "XRUN": sys_state.xrun,
                "XSTEP": sys_state.xstep
            }
        except SystemStateModel.DoesNotExist:
            sys_state_data = {
                "XAUTO": "NaN",
                "XNEXT": "NaN",
                "XPAUSE": "NaN",
                "XRESET": "NaN",
                "XRUN": "NaN",
                "XSTEP": "NaN"
            }
        return sys_state_data
    

