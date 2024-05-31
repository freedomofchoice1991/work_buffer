class Singleton:
    """@class: Singleton implementation of singleton pattern
    """
    __instance = None

    def __new__(cls):
        """_init_deco decorator which should be used for inherited class __init__ method
        @param: cls Class
        @return: instance
        """
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        instance = cls.__instance
        return instance

    # staticmethod - needed to exclude warning highlight from IDE
    @staticmethod
    def _init_deco(init_func):
        """_init_deco decorator which should be used for inherited class __init__ method
        @param: init_func __init__ pointer.
        @return: wrapped method pointer
        """

        def wrapper(*args):
            obj = args[0]

            # TODO fix duplication
            if not hasattr(obj, '_initialized'):
                init_func(*args)
                obj._initialized = True
            elif not obj._initialized:
                init_func(*args)
                obj._initialized = True
            elif obj._initialized:
                # singleton is created and already initialized
                pass
            else:
                message = f'not expected state of singleton object'
                raise ValueError(message)

        return wrapper

    def __init__(self):
        """__init__ dummy for safety reason to check that child class override method
        @param: self The object pointer.
        @return: None
        """
        raise NotImplementedError


if __name__ == "__main__":
    raise NotImplementedError("this module is not self independent")
