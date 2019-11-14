import re

import kivy
kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

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

class calculatorApp(App):

    def build(self):
        return CalcGridLayout()

CALCR = calculatorApp()
CALCR.run()