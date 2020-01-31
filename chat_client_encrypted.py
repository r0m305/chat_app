#Chat app
#By Romeos CyberGypsy
#ASE Algorithm encryption coming soon


import socket
import sys
from termcolor import colored
import optparse
from cryptography.fernet import Fernet
print(colored("[+] Chat Client ","blue"))
print(colored("Written by Romeos CyberGypsy","green"))
print(colored("[+] Now safe with the new AES Encryption","yellow"))

parser = optparse.OptionParser()
parser.add_option("-H", "--host", dest = "host", help = "Host to connect to")
parser.add_option("-p", "--port", dest = "port", help = "Port through which to connect to host")
(values, keys) = parser.parse_args()

host = values.host
port = int(values.port)

key = b'ezarGdrZ6FKkhwoSosKYkIUrMPzLrPK3lOZiJYOUzEQ='
encryptor = Fernet(key)

with open("key.key","wb") as f:
    f.write(key)
    f.close()

f = open("logs.log","a")

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	try:
		s.connect((host,port))
		print(colored("[+] Connected to server", "blue"))
		status = "[+] Connected to server " + host + "\n"
		f.write(status)
	except:
		print(colored("[*] Lewis is not currently online...Quiting","red"))
		status = "Lewis not online...Quiting!!\n"
		f.write(status)
		sys.exit()
	while True:
		text = colored("[*] Enter data to send>","red")
		data=input(text)
		status = "Me: " + data +"\n"
		f.write(status)
		s.sendall(encryptor.encrypt(data.encode()))
		print(colored("[+] Waiting for message","blue"))
		response=s.recv(100000)
		response = encryptor.decrypt(response).decode()
		status = "Lewis: " + response +"\n"
		f.write(status)
		if response=="exit":
			print("[*] Received exit command from the chat server..")
			print("[-] System exiting...")
			f.write("System exiting...\n\n\n")
			sys.exit()
		print(colored("Received:","blue"),response)
		del response
