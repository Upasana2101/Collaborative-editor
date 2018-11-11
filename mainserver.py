#New Server
import socket
import sys
from _thread import *
import threading
import os
import pickle
import time

clientList = []
filesLock = {}
no_of_clients = 0


directory = os.getcwd() + '/files/'
if os.path.isdir(directory) != True:
    os.mkdir(directory)

class Editor:
	def __init__(self, name):
		self.name = name
		global directory
		self.directory = directory
		self.lock = threading.Lock()
		if os.path.isfile(self.directory+self.name)!=True:
			f = open(self.directory+self.name,'w')
			f.close()

	def edit(self, message):
		print("Editing")
		print(message)
		try:
			if message[0] == 'I':
				ins_char = message[1]
				print("Inserting"+ins_char)
				row_n = message[2] - 1 
				col_n = message[3]
				while filesLock[self.name] == 1:   #some other thread is writing on the file
					pass
				self.lock.acquire()
				f = open(self.directory + self.name, 'r')
				lines = f.readlines()
				f.close()
				
				if(row_n >= len(lines)):
					while row_n >=len(lines):
						lines.append("\n")
				lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
				while filesLock[self.name] == True:
					pass
				filesLock[self.name] = True
				f = open(self.directory + self.name, 'w')
				for i in range(len(lines)):
					f.write(lines[i])	
				f.close()	
				self.lock.release()	
				filesLock[self.name] = 0


			elif message[0] == 'B':           # for delete or backspace event
				dlt_char = message[1]
				print("Backspace command\n")
				row_n = message[2] - 1
				col_n = message[3]
				while filesLock[self.name] == 1:   #some other thread is writing on the file
					pass
				self.lock.acquire()
				f = open(self.directory + self.name, 'r')
				lines = f.readlines()
				f.close()
				for i in range(len(lines)):
					if row_n >= i:
						break
				lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
				f = open(self.directory + self.name, 'w')
				for i in range(len(lines)):
					f.write(lines[i])	
				f.close()
				self.lock.release()	
				filesLock[self.name] = 0	

			elif message[0] == 'D':           # for delete or backspace event
				dlt_char = message[1]
				print("Delete command\n")
				row_n = message[2] - 1
				col_n = message[3]
				while filesLock[self.name] == 1:   #some other thread is writing on the file
					pass
				self.lock.acquire()
				f = open(self.directory + self.name, 'r')
				lines = f.readlines()
				f.close()
				for i in range(len(lines)):
					if row_n >= i:
						break
				lines[row_n] = lines[row_n][0:col_n] + lines[row_n][col_n+1:]
				f = open(self.directory + self.name, 'w')
				for i in range(len(lines)):
					f.write(lines[i])	
				f.close()
				self.lock.release()	
				filesLock[self.name] = 0	

			elif message[0] == 'S':
	 			ins_char = ' '
	 			print("Inserting space")
	 			row_n = message[2] - 1 
	 			col_n = message[3]
	 			while filesLock[self.name] == 1:   #some other thread is writing on the file
	 				pass
	 			self.lock.acquire()
	 			f = open(self.directory + self.name, 'r')
	 			lines = f.readlines()
	 			f.close()
	 			if row_n >= len(lines):
	 				while row_n >=len(lines):
	 					lines.append("\n")
	 			lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
	 			f = open(self.directory + self.name, 'w')
	 			for i in range(len(lines)):
	 				f.write(lines[i])	
	 			f.close()
	 			self.lock.release()	
	 			filesLock[self.name] = 0		

			elif message[0] == 'N':
				ins_char = '\n'
				print("New line\n")
				row_n = message[2] - 1 
				col_n = message[3]
				while filesLock[self.name] == 1:   #some other thread is writing on the file
					pass
				self.lock.acquire()
				f =  open(self.directory + self.name, 'r')
				lines = f.readlines()
				f.close()
				if row_n >= len(lines):
					while row_n >=len(lines):
						lines.append("\n")
				lines[row_n] = lines[row_n][0:col_n] + ins_char  + lines[row_n][col_n:]
				f = open(self.directory + self.name, 'w')
				for i in range(len(lines)):
					f.write(lines[i])	
				f.close()
				self.lock.release()	
				filesLock[self.name] = 0

		except Exception as e:		
			print("Exception occured : ", e)

	def sendContents(self,cli_socket):
		f = open(self.directory + self.name, 'r')
		content = f.read()
		content +="\n"
		cli_socket.sendall(content.encode())



def getFileName(cli_socket):
	filename = cli_socket.recv(1024).decode() #Client's chosen filename
	print("Filename entered->"+filename)
	if filename== "QUIT" or filename == "Terminated": #PROBLEMATIC
		return filename
	print(directory+filename)
	if os.path.isfile(directory + filename)!=False:
		print("Error. File Exists")
		err = str(1)
		cli_socket.sendall(err.encode())
		return getFileName(cli_socket)
	else:
		print("Filename OK")
		err = str(0)
		cli_socket.sendall(err.encode())
		return filename

def listFiles(cli_socket):
	files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
	fileList = pickle.dumps(files)
	print("Sent files to client\n")
	# time.sleep(0.1)
	print(time.time())
	cli_socket.sendall(fileList)

def getExistingFileName(cli_socket):
	listFiles(cli_socket)
	print("Waiting for filename from client\n")
	filename = cli_socket.recv(1024).decode()
	print("Filename received from client" + filename)
	if filename == "QUIT":
		return getExistingFileName(cli_socket)

	if os.path.isfile(directory + filename)==False:
		err = str(1)
		cli_socket.sendall(err.encode())
		print("Sent error")
		return getExistingFileName(cli_socket)
	else:
		#File exists
		err = str(0)
		print("Sent NO error to client\n")
		cli_socket.sendall(err.encode())
		return filename	
	


def editAll(message, cli_socket, file):

	print(message)
	print(clientList)
	try:
		for i in clientList:
			if i != cli_socket:
				data = pickle.dumps(message)
				i.sendall(data) 
	except Exception as e:
		print("Exception occured"+e)


def startEditing(cli_socket, file):
	print("---------startEditing()---------")
	print("Started Editing")
	print("Inside start edit function"+file.name)
	print("Waiting for client message")
	data = cli_socket.recv(1024)
	message=pickle.loads(data)
	print("Received message from client"+str(message))
	if message[4] == "QUIT" or message[4] == "Terminated":
		print("QUIT MSG RECEIVED\n")
		print(time.time())
	else:
		while message[4] != "QUIT" and message[4] != "Terminated":
			# message = cli_socket.recv(1024)
			print("message received->"+str(message)+"\n")
			file.edit(message)
			print("Done editing. Now send edits to all clients\n")
			editAll(message, cli_socket, file)
			data = cli_socket.recv(1024)
			message=pickle.loads(data)
	message = ["", "", "", "", "QUIT"]
	message = pickle.dumps(message)
	print("Sending quit message to client's thread")
	print(time.time())
	cli_socket.sendall(message) 


		

def do_task(buff, cli_socket):
	print("---------DO_TASK()---------")
	print("START COLLAB EDIT ")
	global no_of_clients
	ch = ["","","","",""]

	while True:
		data = cli_socket.recv(1024)
		ch = pickle.loads(data)

		print("Choice Entered by client Received->"+ch[4])
		if ch[4]=="Terminated" or ch[4]=="QUIT":
			break
			
		if int(ch[4]) == 1:  #create new file
			print("NEW FILE WANTED BY CLIENT\n")
			filename = getFileName(cli_socket)
			print("Filename inside dotask->"+ filename)
			if filename == "QUIT" or filename == "Terminated": 
				continue
			print(filename)
			file = Editor(filename)
			filesLock[filename] = 0;
			startEditing(cli_socket, file)

		elif int(ch[4]) == 2: #open existing file
			print("OPEN NEW FILE\n")
			filename = getExistingFileName(cli_socket)
			file = Editor(filename)
			if filename not in filesLock:
				filesLock[filename] = 0
			print("Sending file contents to client\n")
			file.sendContents(cli_socket)
			print("Calling StartEditing function\n")
			startEditing(cli_socket, file)
			ch[4] = "Terminated"
			
		elif int(ch[4]) == 3 or ch[4] == "Terminated" or ch[4] == "QUIT": #Eit
			print("Terminated")
			break
		else:
			return
	clientList.remove(cli_socket)
	cli_socket.close()
	no_of_clients-=1
	  

if __name__ == '__main__':
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM )
		
	except socket.error as e:
		print("Socket Creation failed "+ str(e))
		sys.exit()
	port = 1234
	host = socket.gethostbyname('localhost')
	s.bind((host, port))
	s.listen(5)
	while True:
		try:
			cli_socket, cli_addr = s.accept()
			clientList.append(cli_socket)
			no_of_clients+=1
			print("Server connected to Client "+ str(no_of_clients) + " Addr = "+ str(cli_addr) + "\n")
			print(clientList)
			print("\n")
			buff = "Testing"
			t1 = threading.Thread(target = do_task, args=(buff,cli_socket))
			t1.start()
		except Exception as e:
			print(e)


	
		
		

