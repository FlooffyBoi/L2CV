import tkinter as tk
import numpy as np
import threading
class BoundsControls:
    def __init__(self):
        self.mainthread = None
        self.lower_bound = np.array([160,15,229])
        self.higher_bound = np.array([179,255,255])
        # Дом, кухня: [160,15,229]; [179,255,255]
        # 101 кабинет: [0,100,176]; [109,255,255]
        self.window = None

    


    def windowStart(self):
        self.window = tk.Tk()
        self.window.title("Bounds controls")
        
        # Hue low slider
        labelHL = tk.Label(self.window, text="Hue low")
        labelHL.pack(pady=2)
        hueLow_Slider = tk.Scale(self.window,
                                from_=0,
                                to=179,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.lower_bound_setter(x,0))
        hueLow_Slider.set(self.lower_bound[0])  # Set initial value
        hueLow_Slider.pack(pady=2)

        # Hue high slider
        labelHH = tk.Label(self.window, text="Hue high")
        labelHH.pack(pady=2)
        setterHBH = lambda x: self.higher_bound[0]
        hueHigh_Slider = tk.Scale(self.window,
                                from_=0,
                                to=179,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.high_bound_setter(x,0))
        hueHigh_Slider.set(self.higher_bound[0])  # Set initial value
        hueHigh_Slider.pack(pady=2)

        # Saturation low slider
        labelSL = tk.Label(self.window, text="Saturation low")
        labelSL.pack(pady=2)
        saturationLow_Slider = tk.Scale(self.window,
                                from_=0,
                                to=255,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.lower_bound_setter(x,1))
        saturationLow_Slider.set(self.lower_bound[1])  # Set initial value
        saturationLow_Slider.pack(pady=2)

        # Saturation high slider
        labelSH = tk.Label(self.window, text="Saturation high")
        labelSH.pack(pady=2)
        saturationHigh_Slider = tk.Scale(self.window,
                                from_=0,
                                to=255,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.high_bound_setter(x,1))
        saturationHigh_Slider.set(self.higher_bound[1])  # Set initial value
        saturationHigh_Slider.pack(pady=2)

        # Value low slider
        labelVL = tk.Label(self.window, text="Value low")
        labelVL.pack(pady=2)
        valueLow_Slider = tk.Scale(self.window,
                                from_=0,
                                to=255,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.lower_bound_setter(x,2))
        valueLow_Slider.set(self.lower_bound[2])  # Set initial value
        valueLow_Slider.pack(pady=2)

        # Value high slider
        labelVH = tk.Label(self.window, text="Value high")
        labelVH.pack(pady=2)
        valueHigh_Slider = tk.Scale(self.window,
                                from_=0,
                                to=255,
                                orient=tk.HORIZONTAL,
                                length=200,
                                command=lambda x:self.high_bound_setter(x,2))
        valueHigh_Slider.set(self.higher_bound[2])  # Set initial value
        valueHigh_Slider.pack(pady=2)
        self.window.mainloop()

    def high_bound_setter(self,value,id):
        self.higher_bound[id]=value

    def lower_bound_setter(self,value,id):
        self.lower_bound[id]=value

    def mainloop(self):
        self.mainthread = threading.Thread(target=self.windowStart)
        self.mainthread.start()


    