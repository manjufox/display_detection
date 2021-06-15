import time
from multiprocessing import Process, Queue

from transparent_window import transparent_window
from AI.yolo_recognition import yolo_loop

def main():
    q = Queue()
    p1 = Process(target=yolo_loop, args=(q,))
    p2 = Process(target=transparent_window, args=(q,))
    p1.start()
    while q.empty():
        time.sleep(0.1)
    p2.start()
    p1.join()
    p2.join()
# %%
if __name__ == '__main__':
    main()