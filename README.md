# chat_app
chat via terminal...encrypted with AES Algorithm

send the chat_client_encrypted.py file to the client you want to chat with 
port forward tcp port number 1 if communicating over WAN i.e ./ngrok tcp 1
now ping 0.tcp.ngrok.online.io to retrieve the ip address and the port that the client has to connect by setting the host and the port to connect to
on your side, ensure that the chat_server_encrypted.py is already up and online and wait for the client to connect

nice chatting!!

PROCEDURE:
start by port forwarding on port number 1 (default) though this can be editted in the script
  ./ngrok tcp 1

now ping 0.tcp.ngrok.io and this will provide you with the ip address and the port the client needs to connect to

Before running the server script, ensure that your python satisfies all the requirements as follows:
    python3 -m pip install -r requirements.txt
    
Once finishes, launch your server as follows and wait for the client to connect:
    python3 chat_server_encrypted.py
    
 The client should now connect remotely as follows:
    python3 chat_client_encrypted.py -H <ip address provided by ngrok> -p <port provided by ngrok>
    e.g python3 chat_client_encrypted.py -H 3.14.212.173 -p 10344 
    
ADDITION:
The chats are encrypted with AES, and for the sake of security, you can always feel free to edit the key.key file with a valid AES encryption key.

