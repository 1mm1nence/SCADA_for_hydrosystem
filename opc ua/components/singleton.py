class SingletonMeta(type):
    """
    Метаклас для кожного циліндра, який гарантує
    створення лише одного екземпляру на кожен клас.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Імплементація патерну проектування "Одиночка".
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]