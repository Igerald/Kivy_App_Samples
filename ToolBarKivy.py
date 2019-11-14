import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class SampGridLayout(GridLayout):
    pass

class toolbarApp(App):

    def build(self):
        return SampGridLayout()

tba = toolbarApp()
tba.run()