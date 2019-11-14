import re

import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.screenmanager import ScreenManager , Screen

kv_txt = '''
MainScreenManager:
    HomeScreen:
    CalcScreen:
    TxtScreen:

<CustButton@Button>:
    font_size: 32

<HomeScreen>:
    name: 'HOME'
    BoxLayout:
        id: base
        rows: 2
        BoxLayout:
            CustButton:
                text: "Calculator"
                on_release: app.root.current = 'CALC'
        BoxLayout:
            CustButton:
                text: "Text Dragger"
                on_release: app.root.current = 'TXT'

<CalcScreen>:
    name: 'CALC'
    CalcGridLayout:
        id: calculator
        display: entry
        rows: 7
        padding: 10
        spacing: 10
        BoxLayout:
            TextInput:
                id:entry
                font_size: 48
                multiline: False
                text: "0"
        BoxLayout:
            spacing: 10
            CustButton:
                text: "7"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "8"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "9"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "+"
                on_press: entry.text = calculator.setup(entry.text, self.text)
        BoxLayout:
            spacing: 10
            CustButton:
                text: "4"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "5"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "6"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "-"
                on_press: entry.text = calculator.setup(entry.text, self.text)
        BoxLayout:
            spacing: 10
            CustButton:
                text: "1"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "2"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "3"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "*"
                on_press: entry.text = calculator.setup(entry.text, self.text)
        BoxLayout:
            spacing: 10
            CustButton:
                text: "."
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "0"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "^"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "/"
                on_press: entry.text = calculator.setup(entry.text, self.text)  
        BoxLayout:
            spacing: 10
            CustButton:
                id: clear
                text: "AC"
                on_press: entry.text = "0"
            CustButton:
                text: "("
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: ")"
                on_press: entry.text = calculator.setup(entry.text, self.text)
            CustButton:
                text: "="
                on_press: entry.text = calculator.calculate(entry.text)
        BoxLayout:
            CustButton:
                text: "Home"
                on_release: app.root.current = 'HOME'

<TxtScreen>:
    name: "TXT"
    TxtLayout:
        id: Txtcls
        display: nuetxt
        rows: 3
        padding: 10
        spacing: 10
        BoxLayout:
            size_hint_y: .15
            TextInput:
                id:nuetxt
                font_size: 32
                multiline: False
                text: "Type Text Here"
        BoxLayout:
            Scatter:
                Label:
                    id: target
                    text: "test"
                    font_size: 150
                    pos: .5, .5
                    color: 0,1,200,1
        BoxLayout:
            size_hint_y: .15
            CustButton:
                text: "Submit"
                on_press: target.text = Txtcls.ChangeText(nuetxt.text)
            CustButton:
                text: "Home"
                on_release: app.root.current = 'HOME'

'''

class HomeScreen(Screen):
    pass 

class CalcScreen(Screen):
    pass        

class TxtScreen(Screen):
    pass

class MainScreenManager(ScreenManager):
    pass

class CalcGridLayout(GridLayout):

    def setup(self, otxt, ntxt):
        if otxt == "ERROR" or otxt=="0" or ("=" in otxt and ntxt not in "/*-+^"):
            otxt = ntxt
        elif (otxt[-1] in "/*-+^") and (ntxt[0] in "/*-+^"):
            pass
        else:
            otxt += ntxt
        return otxt.replace("= ",'')
    
    def calculate(self, equations):
        section = re.split('[()]',equations)
        csig = ""
        for equation in section:
            try:
                nums = map(float,re.split('[-/*+^]',equation))
                signs = iter([sig for sig in equation if not sig.isdigit()])
                if csig == "":
                    ans = next(nums)
                else:
                    cnum = next(nums)
                    ans = ans+cnum if csig=="+" else ans-cnum if csig=="-" else ans*cnum if csig=="*" else ans/cnum if csig=="/" else ans**cnum
                try:
                    while True:
                        cnum, csig = next(nums), next(signs)
                        ans = ans+cnum if csig=="+" else ans-cnum if csig=="-" else ans*cnum if csig=="*" else ans/cnum if csig=="/" else ans**cnum
                except StopIteration:
                    try:
                        csig = next(signs)
                    except StopIteration:
                        pass
            except ValueError:
                return "ERROR"
        return "= " + (str(ans) if divmod(ans,1)[1] != 0 else str(int(ans)))

class TxtLayout(GridLayout):

    def ChangeText(self, txt):
        return txt

class MainApp(App):

    def build(self):
        app = Builder.load_string(kv_txt)
        return app

BASE = MainApp()

if __name__ == "__main__":
    BASE.run()