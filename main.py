from kivy.app import App
from kivy.lang import Builder


from kivy.properties import NumericProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock

Window.size = (720, 1280)
Builder.load_file('design.kv')

class ListWidget(RecycleView):
    def update(self):
        self.data = [{'text':str(item)}for item in self.items]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.items = []

class MainWidget(BoxLayout):
    number = NumericProperty()
    hour = NumericProperty()
    minute = NumericProperty()
    labeltask = ObjectProperty()
    new_task_btn = ObjectProperty()
    task_input = ObjectProperty()
    outputcontent = ObjectProperty()
    value = 0
    startPressed = False
    endPressed = False

    def add_item(self):
        if self.task_input.text != "":
            self.currentNumber = round(self.number)
            self.currentMinute = self.minute
            self.currenthour = self.hour
            self.value += 1 
            formatted = f'\n {self.value}) {self.task_input.text}   {self.currenthour}:{self.currentMinute}:{self.currentNumber}'
            self.outputcontent.items.append(formatted)
            self.outputcontent.update()
            self.task_input.text = ""
            

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       
        if self.startPressed == True:
            Clock.schedule_interval(self.increment_time, .1)
            self.increment_time(0)
        
        
    def gethour(self):
        if self.minute > 60:
            self.minute = 0
            self.hour += 1
        return self.hour
    def getminute(self):
        if self.number > 60:
            self.number = 0
            self.minute += 1
        return self.minute

    # To increase the time / count
    def increment_time(self, interval):
        self.number += .1
        
       
    # To start the count
    def start(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, .1)
        
        self.startPressed = True
 
    # To stop the count / time
    def stop(self):
        Clock.unschedule(self.increment_time)
        self.endPressed = True
        self.startPressed = False
        
        
    def set_task(self):
        self.labeltask.text = self.task_input.text
    def delete_task(self):
        self.labeltask.text = 'Нет задач'
    def forDisableBtn(self):
        self.stop()
        self.add_item()
        self.delete_task()
        self.number = 0
    def forStartBtn(self):
        self.start()
        self.set_task()
    def ifEndBtn(self):
        self.new_task_btn.text = ('Начать задачу' if self.endPressed else 'Продолжить')
 
# Create the App class
class TimeApp(App):
    def build(self):
        return MainWidget()
 
# Run the App
if __name__ == '__main__':
    TimeApp().run()
