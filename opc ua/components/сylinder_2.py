from components.singleton import SingletonMeta
from opcua import Client

#Адреси нодів відповідних змінних
Y2_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.Y2"
X2_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.X2"
XN2_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.XN2"

class Cylinder_2(metaclass=SingletonMeta):
    """
    Клас другого циліндру. 
    Атрибутами класу є відповідні імена керуючих змінних у мікроконтролері.
    """
    def __init__(self, client: Client) -> None:
        self.client = client
        self.read_and_refresh()


    def read_and_refresh(self):
        """
        Отримання актуальних даних стану системи.
        """
        self.Y2 = self.__get_value_from_node(Y2_NODE_STRING)
        self.X2 = self.__get_value_from_node(X2_NODE_STRING)
        self.XN2 = self.__get_value_from_node(XN2_NODE_STRING)


    def __get_value_from_node(self, node_string):
        """
        Отримання актуальних даних для окремої змінної.
        """
        node = self.client.get_node(node_string)
        value = node.get_value()
        return value