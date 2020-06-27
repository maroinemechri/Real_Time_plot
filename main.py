"""Real time plotting of Microphone level using kivy
"""
import json
import requests
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.garden.graph import MeshLinePlot
from kivy.clock import Clock
from threading import Thread
data_list=[1,2,3,4,5,6,7,8,9,10]


class Logic(BoxLayout):
    def __init__(self, **kwargs):
        super(Logic, self).__init__(**kwargs)
        self.plot = MeshLinePlot(color=[1, 0, 0, 1])

    def start(self):
        self.ids.graph.add_plot(self.plot)
        Clock.schedule_interval(self.get_value, 0.1)

    def stop(self):
        Clock.unschedule(self.get_value)

    def get_value(self, dt):
#########################################
        request = requests.get('https://realtime-e92c4.firebaseio.com/.json' + '?auth=' + 'DBO8mFEDOHovsVJ2utaoqHsvUTI115VUux6Q0qCx')
        data=request.json()
        Ax=data["Employee"]["Gyroscope"]["Ax"] 
        data_list.append(Ax)
        if len(data_list)>=100:
              del data_list[0]
        print(data_list)
#########################################

        self.plot.points = [(i, j) for i, j in enumerate(data_list)]

class RealTimeGraph(App):
    def build(self):
        return Builder.load_file("look.kv")
if __name__ == "__main__":
    RealTimeGraph().run()
    
	
