from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import random
from time import sleep
import socket
import os
import threading 
import pickle
import time

MAXLEN = 1024

folderNumber = str(random.randint(1,1000))

HOME = os.getcwd()+'/clientfiles'+folderNumber+'/'
if os.path.isdir(HOME) == False:
	os.mkdir(HOME)




print("Home Directory for the client is ->"+ HOME +"\n")

def local_edit(textpad, file_name, message):
	print("Current operation in localEdit: ",message)
	file_name = os.path.join(HOME, file_name)
	try:
		if message[0] == 'I':
			ins_char = message[1]
			row_n = message[2] - 1 
			col_n = message[3]
			f =  open(file_name, 'r')
			lines = f.readlines()
			f.close()
			if(row_n >= len(lines)):
				while row_n >=len(lines):
					lines.append("\n")
			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()	


		elif message[0] == 'B':           
			dlt_char = message[1]
			row_n = message[2] - 1
			col_n = message[3]
			f = open(file_name, 'r')
			lines = f.readlines()
			f.close()
			for i in range(len(lines)):
				if row_n >= i:
					break
			lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()

		elif message[0] == 'D':           
			dlt_char = message[1]
			row_n = message[2] - 1
			col_n = message[3]
			f = open(file_name, 'r')
			lines = f.readlines()
			f.close()
			for i in range(len(lines)):
				if row_n >= i:
					break
			lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()

		elif message[0] == 'S':
 			ins_char = ' '
 			row_n = message[2] - 1 
 			col_n = message[3]
 			f =  open(file_name, 'r')
 			lines = f.readlines()
 			f.close()
 			if row_n >= len(lines):
 				while row_n >=len(lines):
 					lines.append("\n")
 			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
 			f = open(file_name, 'w')
 			for i in range(len(lines)):
 				f.write(lines[i])	
 			f.close()

		elif message[0] == 'N':
			ins_char = '\n'
			row_n = message[2] - 1 
			col_n = message[3]
			f =  open(file_name, 'r')
			lines = f.readlines()
			f.close()
			if(row_n >= len(lines)):
				while row_n >=len(lines):
					lines.append("\n")
			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()

	except Exception as e:		
		print("Exception occured : ",e)

def remoteEdit(textpad, message, file_name):
	print("Current operation in remoteEdit: ",message)
	if message[4] == "QUIT" or message[4] == "Terminated":
		return
	if message[4] != file_name:
		return
	file_name = os.path.join(HOME, file_name)
	try:
		if message[0] == 'I':
			ins_char = message[1]
			row_n = message[2] - 1 
			col_n = message[3]
			f =  open(file_name, 'r')
			lines = f.readlines()
			f.close()
			if(row_n >= len(lines)):
				while row_n >=len(lines):
					lines.append("\n")
			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()	


		elif message[0] == 'B':           
			dlt_char = message[1]
			row_n = message[2] - 1
			col_n = message[3]
			f = open(file_name, 'r')
			lines = f.readlines()
			f.close()
			for i in range(len(lines)):
				if row_n >= i:
					break
			lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()

		elif message[0] == 'D':           # for delete or backspace event
			dlt_char = message[1]
			row_n = message[2] - 1
			col_n = message[3]
			f = open(file_name, 'r')
			lines = f.readlines()
			f.close()
			for i in range(len(lines)):
				if row_n >= i:
					break
			lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()

		elif message[0] == 'S':
 			ins_char = ' '
 			row_n = message[2] - 1 
 			col_n = message[3]
 			f =  open(file_name, 'r')
 			lines = f.readlines()
 			f.close()
 			if row_n >= len(lines):
 				while row_n >=len(lines):
 					lines.append("\n")
 			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
 			f = open(file_name, 'w')
 			for i in range(len(lines)):
 				f.write(lines[i])	
 			f.close()

		elif message[0] == 'N':
			ins_char = '\n'
			row_n = message[2] - 1 
			col_n = message[3]
			f =  open(file_name, 'r')
			lines = f.readlines()
			f.close()
			if(row_n >= len(lines)):
				while row_n >=len(lines):
					lines.append("\n")
			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
			f = open(file_name, 'w')
			for i in range(len(lines)):
				f.write(lines[i])	
			f.close()
		f = open(os.path.join(HOME, file_name), 'r')
		content = f.read()	
		textpad.area.text.delete(1.0, END)
		textpad.area.text.insert(1.0, content)
		f.close()

	except Exception as e:		
		print("Exception occured : ",e)

def ReceiveEditionsFromServer(tpad, socket, file):
	message = ["\n","","","",""]
	while message[4] != "3" or message[4] != "QUIT" or message[4] != "Terminated" or message[0]!="":
		data = socket.recv(1024)
		message = pickle.loads(data)
		print("Received remote edit\n")
		print("->"+str(message))
		if message is None:
			continue
		if message[4] == "QUIT" or message[4] == "Terminated" or len(message)>5 or message[0]=="":
			break

		elif message[4] == file:
			print("Executing remote edit")
			remoteEdit(tpad, message, file)
	print("Thread ended")



class TextArea:
	def __init__(self, root):
		frame = Frame(root)
		frame.pack()
		frame.configure(background='black')
		self.textPad(frame)
	def textPad(self,frame):
		tPad = Frame(frame)
		self.text = Text(tPad, height = 30, width = 50, fg = 'white')
		scrollbar = Scrollbar(tPad)
		self.text.configure(yscrollcommand=scrollbar.set, bg='black', insertbackground = 'white')
		self.text.pack(side=LEFT)
		scrollbar.pack(side=RIGHT,fill=Y)
		tPad.pack(side=TOP)

class GUIEditor:
	def __init__(self, root, socket):
		self.area = TextArea(root)
		self.area.text.bind('<Key>', self.inputEvent)
		self.area.text.bind('<BackSpace>', self.backspaceEvent)
		self.area.text.bind('<Return>', self.newLineEvent)
		self.area.text.bind('<Delete>', self.deleteEvent)
		self.area.text.bind('<space>', self.spaceEvent)
		self.filename = None
		self.socket = socket
		self.root = root

	def inputEvent(self, event):
		if self.filename == None:
			return
		position = self.area.text.index(INSERT)
		row, col = position.split('.')
		char = event.char
		possibleChar = ['`','~','!','@','#','$','%','^','&','*','(',')','-','=','+','\\']
		possibleChar = possibleChar + ['.',',','_','|','[',']','{','}',':',';','"','\'','\t','<','>','?']
		if char in possibleChar or char.isalnum():
			message = ['I', char, int(row), int(col), self.filename]
			print(message)
			local_edit(self.area.text, self.filename, message)
			data=pickle.dumps(message)
			self.socket.sendall(data)
		else:
			pass

	def backspaceEvent(self, event):
		if self.filename == None:
			return
		try:
			position = self.area.text.index(INSERT)
			row, col = position.split('.')
			if int(row) == 1 and int(col) == 0:
				return
			char = repr(event.char)
			message = ['B', char, int(row), int(col)-1, self.filename]
			print(message)
			local_edit(self.area.text, self.filename, message)
			data=pickle.dumps(message)
			self.socket.sendall(data)
		except Exception as e:
			print("Backspace not allowed on empty document")

	def newLineEvent(self, event):
		if self.filename == None:
			return
		try:
			position = self.area.text.index(INSERT)
			row, col = position.split('.')
			char = '\n'
			message = ['N', char, int(row), int(col), self.filename]
			print(message)
			local_edit(self.area.text, self.filename, message)
			data=pickle.dumps(message)
			self.socket.sendall(data)
		except Exception as e:
			print("Enter Exception")

	def deleteEvent(self, event):
		if self.filename == None:
			return
		try:
			position = self.area.text.index(INSERT)
			row, col = position.split('.')
			char = repr(event.char)
			message = ['D', char, int(row), int(col), self.filename]
			print(message)
			local_edit(self.area.text, self.filename, message)
			data=pickle.dumps(message)
			self.socket.sendall(data)
		except Exception as e:
			print("Deletion Exception")

	def openfile(self):
		print("OPEN CLICK\n")
		if self.filename is not None: #end previous connection
			strr = ["" , "" , "", "", "Terminated"]
			message = pickle.dumps(strr)
			self.socket.sendall(message)
			print("Sent termination message for previous connection\n")
			print(time.time())

		message = ["","","","","2"]
		message = pickle.dumps(message)
		print("Sending choice to server->"+str(message))
		self.socket.sendall(message)
		list_files = []
		def startClient(list_files):
			print("Waiting for files\n")
			print(time.time())
			list_files = self.socket.recv(1024)
			print("Receives list of files")
			list_files = pickle.loads(list_files)
			if list_files[0] == "":
				print(list_files)
				return startClient(list_files)
			else:
				return list_files
		list_files = startClient(list_files) 
		if list_files == []:
			messagebox.showinfo("No files on the server yet! \n Create a file.")
			return

		new_window = Toplevel()
		new_window.title("Files present on the server ")
		new_window.geometry('400x400')
		self.listbox = Listbox(new_window)
		self.listbox.pack(fill=BOTH, expand=1)	
		
		for i in list_files:
			self.listbox.insert(END, i)

		def on_click(event):
			w = event.widget
			selection = w.get(w.curselection()[0])
			self.filename = selection
			print("Sending filename to server->"+ self.filename)
			self.socket.sendall(self.filename.encode())
			print("Waiting for error code\n")
			err = int(self.socket.recv(1024).decode())
			print("Error Received from server"+ str(err))
			if err == 1:
				print("Error")
				new_window.destroy()
				return
			else:
				print("NO ERROR.\n")
				f = open(os.path.join(HOME, self.filename), 'w')
				lines = ''
				while not lines.endswith('\n'):
					print("Receiving lines from Server")
					line = self.socket.recv(1024).decode()
					lines+=line
				f.write(lines)
				f.close()
				f = open(os.path.join(HOME, self.filename), 'r')
				content = f.read()	
				self.area.text.delete(1.0, END)
				self.area.text.insert(1.0, content)
				f.close()
				self.root.title("Collaborative Editor :  editing "+self.filename)
				new_window.destroy()

			t = threading.Thread(target=ReceiveEditionsFromServer, args=(self, self.socket, self.filename))
			t.setDaemon(True)
			t.start()
	
		self.listbox.bind("<Double-Button-1>", on_click)
	def close(self):
		choice = messagebox.askokcancel("Quit","Are you sure you want to Quit ?")
		if choice is True:
			message = ["","","","","Terminated"]
			message = pickle.dumps(message)
			self.socket.send(message)
			self.root.destroy()
			
		else:	
			return 

	def spaceEvent(self, event):
		if self.filename == None:
			return
		position = self.area.text.index(INSERT)
		row, col = position.split('.')
		char = ' '
		message = ['S', char, int(row), int(col), self.filename]
		print(message)
		local_edit(self.area.text, self.filename, message)
		data = pickle.dumps(message)
		self.socket.sendall(data)

	def newfile(self):
		if self.filename is not None: #end previous connection
			strr = ["" , "" , "", "", "Terminated"]
			message = pickle.dumps(strr)
			self.socket.sendall(message)
		message = ["","","","","1"]
		message = pickle.dumps(message)
		self.socket.sendall(message)
		self.new_window = Toplevel()
		self.new_window.title("Enter filename ")
		self.new_window.geometry('300x100')
		userEntry = Entry(self.new_window, bd=3)
		userEntry.grid(row=0, column=1)
		def choose_filename():
			print(userEntry.get())
			newFileName = userEntry.get()
			
			print(newFileName)
			if newFileName is None:
				return
			if newFileName is "":
				return

			newFileName += ".txt"
			newFileName = newFileName.replace(' ','_')
			if newFileName is None:
				return
			print("Entered Filename->" + newFileName)
			self.filename = newFileName
			self.socket.sendall(self.filename.encode())
			err = int(self.socket.recv(1024).decode())
			print("Error Received"+ str(err))
			if err == 1:
				print("Filename already exists\n")
				messagebox.showinfo("ERROR","Filename already exists.")
				userEntry.delete(0,END)
				choose_filename()
			else:
				print("Filename Ok")
				self.filename = newFileName
				self.root.title("Collaborative Editor :  editing "+self.filename)
				f = open(os.path.join(HOME,self.filename), 'w')
				self.area.text.delete(1.0, END)
				self.new_window.destroy()
				t = threading.Thread(target=ReceiveEditionsFromServer, args=(self, self.socket, self.filename))
				t.setDaemon(True)
				t.start()
				self.new_window.destroy()
		Button(self.new_window, text='Select', command=choose_filename).grid(row=1, column=1)
	def save(self):
		nf = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
		if nf is not None:
			content = str(self.area.text.get(1.0, END))
			nf.write(content)
			nf.close()
		else:
			return

def startCollabEdit(s):
	root = Tk()
	CollabEditor = GUIEditor(root,s)
	root.title('Collaborative Editor : Choose File')
	menubar = Menu(root)
	filemenu = Menu(menubar, tearoff=0)
	filemenu.add_command(label="Open", command=CollabEditor.openfile)
	filemenu.add_command(label="Create", command=CollabEditor.newfile)
	filemenu.add_command(label="Save", command=CollabEditor.save)
	filemenu.add_separator()
	filemenu.add_command(label="Exit", command=CollabEditor.close)
	menubar.add_cascade(label="File", menu=filemenu)

	helpmenu = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Help", menu=helpmenu)
	root.config(menu = menubar)
	root.mainloop()



if __name__ == '__main__':
	
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
	except socket.error as e:
		print("Socket Creation failed " + e)
		sys.exit()
	port = 1234
	host = socket.gethostbyname('localhost')
	try:
		s.connect((host, port))
		print("Client connected to Server\n")
		startCollabEdit(s)
	except socket.error as e:
		print("Socket Connection Failed. "+ str(e))
		sys.exit()

