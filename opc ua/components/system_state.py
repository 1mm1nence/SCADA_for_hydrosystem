from components.singleton import SingletonMeta
from opcua import Client

#Адреси нодів відповідних змінних
XAUTO_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XAUTO"
XNEXT_AUTO_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XNEXT_AUTO"
XPAUSE_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XPAUSE"
XRESET_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XRESET"
XRUN_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XRUN"
XSTEP_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XSTEP"


class ControlSystem(metaclass=SingletonMeta):
    """
    Клас для зберігання стану системи. 
    Атрибутами класу є відповідні імена керуючих змінних у мікроконтролері.
    """

    def __init__(self, client: Client) -> None:
        self.client = client
        self.read_and_refresh()
    
    
    def read_and_refresh(self):
        """
        Отримання актуальних даних стану системи.
        """
        self.XAUTO = self.__get_value_from_node(XAUTO_NODE_STRING)
        self.XNEXT = self.__get_value_from_node(XNEXT_AUTO_NODE_STRING)
        self.XPAUSE = self.__get_value_from_node(XPAUSE_NODE_STRING)
        self.XRESET = self.__get_value_from_node(XRESET_NODE_STRING)
        self.XRUN = self.__get_value_from_node(XRUN_NODE_STRING)
        self.XSTEP = self.__get_value_from_node(XSTEP_NODE_STRING)


    def __get_value_from_node(self, node_string):
        """
        Отримання актуальних даних для окремої змінної.
        """
        node = self.client.get_node(node_string)
        value = node.get_value()
        return value
    
    def change_to_desired(self, data: dict) -> None:
        xpause_node = self.client.get_node(XPAUSE_NODE_STRING)
        self.client.set_values([ xpause_node ], [ True ])
        print("set.")