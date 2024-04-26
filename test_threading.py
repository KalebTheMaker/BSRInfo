from infinitetimer import InfiniteTimer
import time

def tick():
    print("slow tick")

if __name__ == "__main__":
    t = InfiniteTimer(1, tick)
    t.start()

    while True:
        print("Fast Tick")
        time.sleep(.1)