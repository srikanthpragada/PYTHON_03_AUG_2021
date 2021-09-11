import threading
from threading import Thread

print(threading.main_thread())
print(threading.current_thread())


def print_numbers(start, stop):
    for n in range(start, stop):
        print(f"Child2 {n}")


class PrintThread(Thread):
    def run(self):
        for n in range(1, 11):
            print(f"Child1 {n}")


ct1 = PrintThread()
ct1.start()

ct2 = Thread(target=print_numbers, args=(100, 111))
ct2.start()

print(f"Thread count = {threading.active_count()}")

for n in range(1, 11):
    print(f"Main {n}")
