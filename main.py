from tkinter import Button, Label, Tk
import tkinter.font as font
from tkinter import messagebox

turn = "X"

def reset(winner):

	if winner == "D":
		messagebox.showinfo("", "Draw, nobody is winner!")
	else:
		messagebox.showinfo("", f"{winner} is winner!")

	global turn
	turn = "X"
	field1.config(text="")
	field2.config(text="")
	field3.config(text="")

	field4.config(text="")
	field5.config(text="")
	field6.config(text="")

	field7.config(text="")
	field8.config(text="")
	field9.config(text="")

	info.config(fg="red")
	info.config(text=turn)

def changeTurn():
	global turn
	if turn == "X": turn = "O"
	elif turn == "O": turn = "X"

	if turn == "X": info.config(fg="red")
	elif turn == "O": info.config(fg="blue")

	info.config(text=turn)
def checkFields():
	#X
	if field1.cget("text") == "X" and field2.cget("text") == "X" and field3.cget("text") == "X": reset("X")
	elif field4.cget("text") == "X" and field5.cget("text") == "X" and field6.cget("text") == "X": reset("X")
	elif field7.cget("text") == "X" and field8.cget("text") == "X" and field9.cget("text") == "X": reset("X")

	elif field1.cget("text") == "X" and field4.cget("text") == "X" and field7.cget("text") == "X": reset("X")
	elif field2.cget("text") == "X" and field5.cget("text") == "X" and field8.cget("text") == "X": reset("X")
	elif field3.cget("text") == "X" and field6.cget("text") == "X" and field9.cget("text") == "X": reset("X")

	elif field1.cget("text") == "X" and field5.cget("text") == "X" and field9.cget("text") == "X": reset("X")
	elif field3.cget("text") == "X" and field5.cget("text") == "X" and field7.cget("text") == "X": reset("X")

	#O
	elif field1.cget("text") == "O" and field2.cget("text") == "O" and field3.cget("text") == "O": reset("O")
	elif field4.cget("text") == "O" and field5.cget("text") == "O" and field6.cget("text") == "O": reset("O")
	elif field7.cget("text") == "O" and field8.cget("text") == "O" and field9.cget("text") == "O": reset("O")

	elif field1.cget("text") == "O" and field4.cget("text") == "O" and field7.cget("text") == "O": reset("O")
	elif field2.cget("text") == "O" and field5.cget("text") == "O" and field8.cget("text") == "O": reset("O")
	elif field3.cget("text") == "O" and field6.cget("text") == "O" and field9.cget("text") == "O": reset("O")

	elif field1.cget("text") == "O" and field5.cget("text") == "O" and field9.cget("text") == "O": reset("O")
	elif field3.cget("text") == "O" and field5.cget("text") == "O" and field7.cget("text") == "O": reset("O")

	#OX
	elif field1.cget("text") != "" and field2.cget("text") != "" and field3.cget("text") != "" and field4.cget("text") != "" and field5.cget("text") != "" and field6.cget("text") != "" and field7.cget("text") != "" and field8.cget("text") != "" and field9.cget("text") != "":
		reset("D")

def changeOwner(field):
	global turn

	if field == 1 and field1.cget("text") == "": 
		if turn == "X": field1.config(fg="red")
		elif turn == "O": field1.config(fg="blue")
		field1.config(text=turn)
		changeTurn()
		checkFields()
	if field == 2 and field2.cget("text") == "": 
		if turn == "X": field2.config(fg="red")
		elif turn == "O": field2.config(fg="blue")
		field2.config(text=turn)
		changeTurn()
		checkFields()
	if field == 3 and field3.cget("text") == "": 
		if turn == "X": field3.config(fg="red")
		elif turn == "O": field3.config(fg="blue")
		field3.config(text=turn)
		changeTurn()
		checkFields()

	if field == 4 and field4.cget("text") == "": 
		if turn == "X": field4.config(fg="red")
		elif turn == "O": field4.config(fg="blue")
		field4.config(text=turn)
		changeTurn()
		checkFields()
	if field == 5 and field5.cget("text") == "": 
		if turn == "X": field5.config(fg="red")
		elif turn == "O": field5.config(fg="blue")
		field5.config(text=turn)
		changeTurn()
		checkFields()
	if field == 6 and field6.cget("text") == "": 
		if turn == "X": field6.config(fg="red")
		elif turn == "O": field6.config(fg="blue")
		field6.config(text=turn)
		changeTurn()
		checkFields()

	if field == 7 and field7.cget("text") == "": 
		if turn == "X": field7.config(fg="red")
		elif turn == "O": field7.config(fg="blue")
		field7.config(text=turn)
		changeTurn()
		checkFields()
	if field == 8 and field8.cget("text") == "": 
		if turn == "X": field8.config(fg="red")
		elif turn == "O": field8.config(fg="blue")
		field8.config(text=turn)
		changeTurn()
		checkFields()
	if field == 9 and field9.cget("text") == "": 
		if turn == "X": field9.config(fg="red")
		elif turn == "O": field9.config(fg="blue")
		field9.config(text=turn)
		changeTurn()
		checkFields()


window = Tk()
window.title('Tic Tac Toe')

info1 = Label(window, text="Turn:", font=font.Font(size=16), width=10, height=1)
info1.grid(columnspan=2, rowspan=2, column=2, row=2, padx=10, pady=1, sticky='S')

info = Label(window, text="X", font=font.Font(size=16), width=10, height=1, fg="red")
info.grid(columnspan=2, rowspan=2, column=2, row=3, padx=10, pady=1, sticky='S')

field1 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(1))
field1.grid(columnspan=2, rowspan=2, column=4, row=2, padx=5, pady=5)
field2 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(2))
field2.grid(columnspan=2, rowspan=2, column=6, row=2, padx=5, pady=5)
field3 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(3))
field3.grid(columnspan=2, rowspan=2, column=8, row=2, padx=5, pady=5)

field4 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(4))
field4.grid(columnspan=2, rowspan=2, column=4, row=4, padx=5, pady=5)
field5 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(5))
field5.grid(columnspan=2, rowspan=2, column=6, row=4, padx=5, pady=5)
field6 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(6))
field6.grid(columnspan=2, rowspan=2, column=8, row=4, padx=5, pady=5)

field7 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(7))
field7.grid(columnspan=2, rowspan=2, column=4, row=6, padx=5, pady=5)
field8 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(8))
field8.grid(columnspan=2, rowspan=2, column=6, row=6, padx=5, pady=5)
field9 = Button(window, text="", font=font.Font(size=16), width=10, height=4, command=lambda: changeOwner(9))
field9.grid(columnspan=2, rowspan=2, column=8, row=6, padx=5, pady=5)

window.resizable(False, False)
window.mainloop()