#%%
import mss
import mss.tools

def screenshot(monitor_number = 0,output="sct.png"):
    with mss.mss() as sct:
        output = sct.shot(mon=monitor_number, output=output)
        
    return output