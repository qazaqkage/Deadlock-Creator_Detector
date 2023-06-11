from threading import Thread
from threading import Barrier
import sys

processes1 = []
processes2 = []

def main():
    a = object()
    b = object()

    barrier = Barrier(2)

    def thread1():
        nonlocal processes1
        nonlocal processes2
        with a:
            print("Enter no. of processes: ", end="")
            size = int(input())
            processes1 = [[0 for _ in range(size)] for _ in range(size)]
            print("Enter matrix -->")
            for i in range(size):
                for j in range(size):
                    processes1[i][j] = int(input())
            try:
                barrier.wait() # sync
            except Exception as e:
                raise e
            with b:
                print("Now catch B")

    def thread2():
        nonlocal processes1
        nonlocal processes2
        with b:
            print("Enter no. of processes: ", end="")
            size = int(input())
            processes2 = [[0 for _ in range(size)] for _ in range(size)]
            print("Enter matrix -->")
            for i in range(size):
                for j in range(size):
                    processes2[i][j] = int(input())
            try:
                barrier.wait() # sync
            except Exception as e:
                raise e
            with a:
                print("Now catch A")

    t1 = Thread(target=thread1)
    t2 = Thread(target=thread2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Deadlock detected!")


if __name__ == "__main__":
    main()