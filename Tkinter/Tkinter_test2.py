# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:03:47 2016

@author: Jesus
"""

"""
ZetCode Tkinter tutorial

In this script, we lay out images
using absolute positioning.

Author: Jan Bodnar
Last modified: November 2015
Website: www.zetcode.com
"""

from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH
from ttk import Frame, Style

class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
        
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = 0#(sw)/2
        y = 0#(sh)/2
        self.parent.geometry('%dx%d+%d+%d' % (sw, sh, x, y))

        
    def initUI(self):
      
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")
        
        bard = Image.open("alphonse.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)
        
        rot = Image.open("charmander.jpg")
        rotunda = ImageTk.PhotoImage(rot)
        label2 = Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)        
#        
        minc = Image.open("Pokeball.png")
        mincol = ImageTk.PhotoImage(minc)
        label3 = Label(self, image=mincol)
        label3.image = mincol
        label3.place(x=170, y=50)        
#              

def main():
  
    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main()  