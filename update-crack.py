print("select .AUIF File")
import os, tkinter, tkinter.filedialog,tkinter.messagebox
root = tkinter.Tk()
root.withdraw()
fTyp = [("",".AUIF")]
iDir = "c://"
file = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
s = open(file,"r",encoding="utf-8")
s = s.read()
d = open("DOS.py","w",encoding="utf-8")
d.write(s)
d.close()
