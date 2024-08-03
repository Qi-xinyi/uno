import socket

# 创建Socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定服务器地址和端口
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# 监听连接请求
server_socket.listen(5)
print("等待客户端连接...")

while True:
    # 接受客户端连接请求
    client_socket, client_address = server_socket.accept()
    print("与客户端 {}:{} 建立连接".format(client_address[0], client_address[1]))

    try:
        while True:
            # 接收客户端发送的数据
            data = client_socket.recv(1024)
            if data:
                print("接收到来自客户端的数据:", data.decode())
                # 发送响应给客户端
                client_socket.sendall("服务器收到消息了".encode())
            else:
                print("客户端断开连接")
                break
    finally:
        # 关闭与客户端的连接
        client_socket.close()