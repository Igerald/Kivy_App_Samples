import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.pagelayout import PageLayout

# Separating Presentation Layer from Logic Layer

class KivyAppBackendApp(App):

    def build(self):
        return Label()

#############################################################################################

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

#############################################################################################

class FloatingApp(App):

    def build(self):
        return FloatLayout()

#############################################################################################.

class GridApp(App):

    def build(self):
        return GridLayout()

#############################################################################################.

class BoxApp(App):

    def build(self):
        return BoxLayout()

#############################################################################################.

class StackApp(App):

    def build(self):
        return StackLayout()

#############################################################################################.

class PageApp(App):

    def build(self):
        return PageLayout()

#############################################################################################.

TestKivy = PageApp()

TestKivy.run()
