class SignalWriter:
    storage = []

    @staticmethod
    def write(num):
        SignalWriter.storage.append(num)
