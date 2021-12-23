import ctypes, sys, os, random

'''
Module which allows you to work with GUI and UI in python.
For example, you can call MsgBox() to create a new
Message-box with buttons, title, text and style.
'''

def mb(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    ##  Styles:
    ##  0 : OK
    ##  1 : OK | Cancel
    ##  2 : Abort | Retry | Ignore
    ##  3 : Yes | No | Cancel
    ##  4 : Yes | No
    ##  5 : Retry | No 
    ##  6 : Cancel | Try Again | Continue

class MsgBox():
    def __init__(self, title, text, style:int=0):
        self.title = title
        self.text = text
        self.style = style
    
    def Call(self):
        mb(self.text, self.title, self.style)