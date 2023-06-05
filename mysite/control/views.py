from django.shortcuts import render
from django.views import View
from opcuaAPI.models import MainCylinderStateModel, AuxiliaryCylinderStateModel

# from analysis.models import MainStateHistory, AuxiliaryStateHistory

class SupervisoryControl(View):
    def get(self, request):
        cyl_context = self.__get_cyl_data_from_db()
        # count_context = self.__get_history_data_from_db()
        context = cyl_context # | count_context
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
    
    # def __get_history_data_from_db(self) -> dict:
    #     try:
    #         last_record_1 = MainStateHistory.objects.latest('time')
    #         history_1_data = {
    #             "x_1_count": last_record_1.x_1_count,
    #             "x_n1_count": last_record_1.x_n1_count,
    #             "y1_count": last_record_1.y1_count,
    #             "yn1_count": last_record_1.yn1_count
    #         }
    #     except MainStateHistory.DoesNotExist:
    #         history_1_data = {
    #             "x_1_count": "NaN",
    #             "x_n1_count": "NaN",
    #             "y1_count": "NaN",
    #             "yn1_count": "NaN"
    #         }
    #     try:
    #         last_record_2 = AuxiliaryStateHistory.objects.latest('time')
    #         history_2_data = {
    #             "x2_count": last_record_2.x2_count,
    #             "xn2_count": last_record_2.xn2_count,
    #             "y2_count": last_record_2.y2_count
    #         }
    #     except AuxiliaryStateHistory.DoesNotExist:
    #         history_2_data = {
    #             "x2_count": "NaN",
    #             "xn2_count": "NaN",
    #             "y2_count": "NaN"
    #         }
    #     history_data = history_1_data | history_2_data
    #     return history_data

