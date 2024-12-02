import socket
import paramiko
from paramiko import SSHClient, SFTPClient

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0:8000"))

server_socket.listen(5)
print("running")

while True:
    client_socket, addr = server_socket.accept()
    print("conneted")
    client_socket.send("hello")
    client_socket.close()

client_socket = socket.socket(socket.AD_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 8000))
message = client_socket.recv(1024)
print("server: ", message.decode())
client_socket.close()

hostname = "example.com"
username = "user"
password = "password"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoPolicy())
ssh.connect(hostname, username=usernam, password=password)

stdin, stdout, stderr = ssh.exec_command("ls -l")
print(stdout.read().decode())

ssh.close()

sftp = ssh.open_sftp()
sftp.put("local_file.txt", "remote_file.txt")
sftp.close()

ssh.close()