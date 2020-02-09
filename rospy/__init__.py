from time import sleep as _sleep


class Publisher:
    def __init__(self, name, state, queue_size=4):
        self.name, self.state, self.queue_size = name, state, queue_size

    def publish(self, state):
        print(f"publishing {state} to {self.name}")


def init_node(name, anonymous=True):
    print(f"initializing node {name} with anonymous={anonymous}")


def sleep(t):
    print("sleeping for %.2f seconds" % t)
    _sleep(t)


class Rate:
    def __init__(self, td):
        self.td = td

    def sleep(self, count):
        sleep(self.td * count)
