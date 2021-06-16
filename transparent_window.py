# %%
import tkinter
import time
from multiprocessing import Queue


def tk_preload():
    root = tkinter.Tk()
    root.wm_attributes("-transparentcolor", "snow")
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.attributes('-fullscreen', True)
    root.attributes('-topmost', True)
    canvas = tkinter.Canvas(root, width=w, height=h, bg="snow")
    canvas.place(x=0, y=0)
    return root, canvas

def transparent_window(q:Queue):
    root, canvas = tk_preload()
    
    while True:
        result = q.get()
        
        for i ,res in enumerate(result):
            x1,y1,x2,y2 = res[0],res[1],res[2],res[3]
            conf = res[4]
            cls = res[6]
                        
            n = canvas.create_rectangle(
            x1,y1,x2,y2, tags='o', outline="red", width=3)
            canvas.create_text(
            x1-20, y1-20, text=f"{cls}:{str(conf)[:4]}", font=('MS Gothic', 20, "bold"),fill="red", tags='o'
        )
        
        canvas.pack()
        canvas.update()
        if q.empty():
            time.sleep(0.1)
        canvas.delete('o')

