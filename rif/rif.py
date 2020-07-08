from tkinter import *
from tkinter import messagebox
text = ''
text1 = ''
bbc = []
ar =''
br = ''
def test():
	bal = 0
	bal1 = 0
	bl = 0
	black = []
	rept = ''
	file = open('data.txt', 'r')
	text1 = file.read()
	file.close()
	bbc = text1.split(' ')
	for i in range(len(bbc)):
		b = bbc[i]
		bal = 0
		bal1 = 0
		text = message.get()
		aa = list(text)
		bb = list(b)
		if len(aa) > len(bb):
			prtt = len(bb)
		else:
			prtt = len(aa)
		for i in range(prtt):
			ar = aa[i]
			br = bb[i]
			if ar == br:
				bal = bal + 1
		bal1 = prtt / 2
		if bal == bal1 or bal > bal1:
			bl = 0
			for i in range(len(black)):
				if black[i] == b:
					bl = 1
			if bl == 0:
				black.append(b)
				rept = rept + ' ' + b
	messagebox.showinfo("RESULTS", rept)
root = Tk()
root.title("RIF")
root.geometry("300x250")
 
message = StringVar()
 
message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, anchor="c")
 
message_button = Button(text="Search", command=test, background="#555", foreground="#ccc", width=20, height=5)
message_button.place(relx=.5, rely=.5, anchor="c")
 
root.mainloop()