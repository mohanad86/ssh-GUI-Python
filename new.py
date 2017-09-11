from tkinter import *

fields = 'Machine Name', 'Root User', 'Hostname Or IP', 'Port Number', 'User', 'Copy ssh-id', 'Root ssh-id'


def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 


def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=20, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries


def clicked():
    Input = entry1.get()
    FileName = str("filepath" + Input + ".txt")
    TextFile = open(FileName,"w")


if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   button1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   button1.pack(side=LEFT, padx=5, pady=5)
   button2 = Button(root, text='Quit', command=root.quit)
   button2.pack(side=LEFT, padx=5, pady=5)
   button3 = Button(root, text='Quit', command=clicked)
   button3.pack(side=LEFT, padx=5, pady=5)	
   entry1 = Entry(root)
   button1 = Button(root,text="Press to create text file", command = clicked)
   entry1.pack()
   button1.pack()


   root.mainloop()




