#%%
import torch
from .sct import screenshot
from multiprocessing import Process, Queue

# Model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def yolo():
    while True:
        img = screenshot(monitor_number = 2,output="sct.png")
        results = model(img)
        return result_tolist(results)

def result_tolist(results):
    rpd = results.pandas().xyxy[0]
    rpd.iloc[:,:4] = rpd.iloc[:,:4].astype('int')
    return rpd.values.tolist()

def yolo_loop(q:Queue):
    while True:
        res = yolo()
        q.put(res)
