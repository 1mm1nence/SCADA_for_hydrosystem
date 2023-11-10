import sys
from opcua import Client
import time
import requests
import json

from components.сylinder_1 import Cylinder_1
from components.сylinder_2 import Cylinder_2
from components.system_state import ControlSystem


OPC_SERVER_URL = "opc.tcp://DESKTOP-C68B7SK:4840"
HREF_SEND = "http://vladslyzhuk.pythonanywhere.com/api/post"
HREF_GET = "http://vladslyzhuk.pythonanywhere.com/api/get_desired"
HREF_CLEAR_DESIRED = "http://vladslyzhuk.pythonanywhere.com/api/clear_desired"

#TODO добавити окремий урл для повідомлення про потенційні загрози
    
def form_json(cyl_1: Cylinder_1, cyl_2: Cylinder_2, ctrl_sys: ControlSystem) -> dict:
    """
    Формування словнику, у якому зберігатимуться дані для звіту стану системи.
    """
    data = {
        'Y1': cyl_1.Y1,
        'YN1': cyl_1.YN1,
        'X1': cyl_1.X1,
        'X_1': cyl_1.X_1,
        'X_N1': cyl_1.X_N1,

        'Y2': cyl_2.Y2,
        'X2': cyl_2.X2,
        'XN2': cyl_2.XN2,

        'XAUTO': ctrl_sys.XAUTO,
        'XNEXT': ctrl_sys.XNEXT,
        'XPAUSE': ctrl_sys.XPAUSE,
        'XRESET': ctrl_sys.XRESET,
        'XRUN': ctrl_sys.XRUN,
        'XSTEP': ctrl_sys.XSTEP,
        
        'initial': False
    }
    print(data)
    print(f"formed json: X1: {cyl_1.X1}, Y2: {cyl_2.Y2}, XN2: {cyl_2.XN2}, XRUN: {ctrl_sys.XSTEP}")
    return data

def desired_checkout() -> dict:
    # Отримання даних з API.
    desired_state = requests.get(HREF_GET)
    print(desired_state)
    if desired_state.status_code == 200:
        # Розкодування JSON відповіді у Python словник.
        data_dict = json.loads(desired_state.text)
        print(data_dict)
        return data_dict
    else:
        print("Під час виконання запиту сталась помилка. Статус:", desired_state.status_code)
        return None

def clear_desired() -> None:
    # Надсилання на сервер повідомлення про те, що керуючі змінні було змінено
    # відповідно до бажаного користувачем стану. 
    data_to_send = {
        'desired_done': True
    }
    r = requests.post(HREF_CLEAR_DESIRED, data_to_send)



if __name__ == '__main__':

    # Підключення до клієнта
    try:
        client = Client(OPC_SERVER_URL)
        client.connect()
        print("Connected to opc ua sever.")
    except Exception as err:
        #TODO надіслати на сервер сповіщення з проблемою.
        print('err', err)
        sys.exit(1)

    cyl_1 = Cylinder_1(client)
    cyl_2 = Cylinder_2(client)
    ctrl_sys = ControlSystem(client)

    # count = 0
    last_json = {}
    initial_flag = False
    desired_state = None
    

    while True:
        desired_state = desired_checkout()
        if desired_state['data']['xpause_desired'] == True:
            ctrl_sys.change_to_desired(desired_state)
            clear_desired()
            desired_state = None

        cyl_1.read_and_refresh()
        cyl_2.read_and_refresh()
        ctrl_sys.read_and_refresh()

        json_to_send = form_json(cyl_1, cyl_2, ctrl_sys)

        # Перевірка на перший запуск системи.
        if json_to_send['XRUN'] and not initial_flag:
            initial_flag = True
            json_to_send['initial'] = True
        if not json_to_send['XRUN'] and initial_flag:
            initial_flag = False

        if json_to_send != last_json:
            r = requests.post(HREF_SEND, json_to_send)
            print(f"Data sent. X1: {json_to_send['X1']}, Y2: {json_to_send['Y2']}")
        last_json = json_to_send
        
        time.sleep(0.1)

        # count += 1
        # if count > 1000:
        #     break

    client.disconnect()

