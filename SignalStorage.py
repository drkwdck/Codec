class SignalStorage:
    storage = []
    writed = 0

    @staticmethod
    def write(num):
        SignalStorage.storage.append(num)
        SignalStorage.writed = SignalStorage.writed + 1

    @staticmethod
    def read():
        SignalStorage.storage.pop()