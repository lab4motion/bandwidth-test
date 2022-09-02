class Config:
    _instance = None

    def __init__(self, config_provider):
        self.__class__._instance = config_provider

    @classmethod
    def instance(cls):
        if cls._instance:
            return cls._instance
        raise SystemExit(
            'Please set config. You need to call Config constructor'
        )
