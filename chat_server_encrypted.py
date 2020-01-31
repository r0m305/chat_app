#By Romeos CyberGypsy
#AES Algorithm coming soon
#Requires port forwarding if client not in the same network as the server

import socket
from termcolor import colored
import time
import sys
from cryptography.fernet import Fernet

key = b'ezarGdrZ6FKkhwoSosKYkIUrMPzLrPK3lOZiJYOUzEQ='
encryptor = Fernet(key)


host='0.0.0.0'
port=1
print(colored("  __   _   _    ___    _____","blue"))
time.sleep(0.5)
print(colored(" /__| | |_| |  / _ \  |_   _|    ","blue"))
time.sleep(0.5)
print(colored(" |__  |  _  | | /_\ |   | |","blue"))
time.sleep(0.5)
print(colored(" \__| |_| |_| |_| |_|   |_|   ANONYMOUSLY","blue"))
time.sleep(0.5)
print(" ")
print(colored("Author--> Romeos CyberGypsy","yellow"))
time.sleep(0.5)
print(colored("Sponsored by Leusoft","white"))
time.sleep(0.5)
print(colored("*Written for private chatting*"))
print(" ")
print(colored("[*] Chat server up and waiting for client connection...","green"))
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((host,port))
	while True:
		s.listen(5)
		client, addr=s.accept()
		print("[*] Received connection from:",addr[0])
		while True:
			request=client.recv(100000)
			request = encryptor.decrypt(request).decode()
			print(colored("[*]{}:" .format(addr[0]),"blue"), request)
			response=input(colored("[*] Me>:","red")).encode()
			response2 = response
			response = encryptor.encrypt(response)
			client.sendall(response)
			if response2.decode() == "exit":
				print(colored("[*] System exiting..","red"))
				time.sleep(2)
				sys.exit()
			print(colored("[-] Waiting for message...","green"))
			del response
