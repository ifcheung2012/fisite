import os

class ifcheung:
    def __init__(self,string):
           """docstring for gethello"""
           # TODO: write code...
           self.text= string
    def printit(self):
           print 'new line'
           print 'new line' + self.text
           print 'new line'


member = ifcheung("hello world")
print member.printit()
