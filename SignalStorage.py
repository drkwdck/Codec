class SignalStorage:
    storage = []

    @staticmethod
    def write(num):
        SignalStorage.storage.append(num)

    @staticmethod
    def read():
        SignalStorage.storage.pop()