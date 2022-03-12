import socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_msg = input("Напишите сообщение: ")
    client.sendto(send_msg.encode('utf-8'), ('127.0.0.1', 50001))
    if send_msg == 'q':
        break
    back_msg = client.recv(1024).decode('utf-8')
    print(back_msg)

client.close()