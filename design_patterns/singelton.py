# The Gang of Four’s implementation

class Logger:
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance


# logger = Logger.instance()
# logger_two = Logger.instance()
# print(logger)
# print(logger_two)
# print(logger == logger_two)
# print(logger is logger_two)

# Pythonic implementation

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


logger = Logger()
logger_two = Logger()

# print(logger)
# print(logger_two)



