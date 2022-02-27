class SignalStorage:
    storage = []
    writed = 0

    @staticmethod
    def write(num):
        if num == 5184:
            print('123')
        SignalStorage.storage.append(num)
        SignalStorage.writed = SignalStorage.writed + 1

    @staticmethod
    def read():
        SignalStorage.storage.pop()