from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.popup import Popup


class StudentListButton(RecycleDataViewBehavior, Button):
    index = None

class StudentDB(BoxLayout):

    first_name_input = ObjectProperty()
    last_name_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_students(self):
        pass

    def delete_student(self):
        pass

    def replace_student(self):
        pass

class StudentDBApp(App):

    def build(self):
        return StudentDB()

sdb = StudentDBApp()
sdb.run()