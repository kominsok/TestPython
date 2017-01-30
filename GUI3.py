from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename

def doNew():
    compose_text.delete(1,END)
    compose_text.edit_reset()

def doOpen():
    filepath=askopenfilename()
    if filepath!=None and filepath!="":
        with open(filepath,encoding="utf-8") as f:
            fileContents=f.read()
            compose_text.delete(1.0,"end")
            compose_text.insert(1.0,fileContents)
            compose_text.edit_modified(False)
            ile_path=filepath

def doSave():
    filepath=asksaveasfilename(filetypes=(('Text files','*.txt'),
                                          ('Python Files','*.pyw'),
                                          ('All Files','*.*')))
    try:
        with open(filepath,'wb') as f:
            text=compose_text.get(1.0,'end-1c')
            f.write(bytes(text,'UTF-8'))
            return 'saved'
    except FileNotFoundError:
        print('FileNotFoundError')
        return 'Cancelled'

root=Tk()
menubar=Menu(root)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="New",command=doNew)
filemenu.add_command(label="Opem",command=doOpen)
filemenu.add_command(label="Save",command=doSave)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.quit)
filemenu.add_command(label="File",command=filemenu)

if __name__=="__main__":
    compose_text=Text(root)
    compose_text.pack()
    root.config(menu=menubar)
    root.mainloop()
