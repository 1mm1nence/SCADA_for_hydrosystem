from components.singleton import SingletonMeta
from opcua import Client

#Адреси нодів відповідних змінних
Y1_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.Y1"
YN1_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.YN1"
X1_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.X1"
X_1_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.X_1"
X_N1_NODE_STRING = "ns=4;s=|var|CODESYS Control Win V3.Application.PLC_PRG.X_N1"

class Cylinder_1(metaclass=SingletonMeta):
    """
    Клас першого циліндру. 
    Атрибутами класу є відповідні імена керуючих змінних у мікроконтролері.
    """

    def __init__(self, client: Client) -> None:
        self.client = client
        self.read_and_refresh()
    
    
    def read_and_refresh(self):
        """
        Отримання актуальних даних стану системи.
        """
        self.Y1 = self.__get_value_from_node(Y1_NODE_STRING)
        self.YN1 = self.__get_value_from_node(YN1_NODE_STRING)
        self.X1 = self.__get_value_from_node(X1_NODE_STRING)
        self.X_1 = self.__get_value_from_node(X_1_NODE_STRING)
        self.X_N1 = self.__get_value_from_node(X_N1_NODE_STRING)


    def __get_value_from_node(self, node_string):
        """
        Отримання актуальних даних для окремої змінної.
        """
        node = self.client.get_node(node_string)
        value = node.get_value()
        return value
    