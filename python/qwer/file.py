#socket：套接字，提供了网络间通讯的基本功能


# server 端  TCP
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)   #创建socket，封装协议（ipv4协议，tcp的协议）  (socket.SOCK_DGRAM是udp的协议)
a=('0.0.0.0',3000)  #ip和端口号
s.bind(a)          #绑定ip和端口号 bind接受到的参数是元组
# s.listen(3)   ###udp的不适用监听状态，里面的数字是指最大等待数
# 下面是tcp的
# while True:         #接受请求的
#     a,b = s.accept()   #会产生两个结果  第一份结果a:是客服端的链接信息  第二个结果b:存放的是客服端的ip地址和端口号
#     msg=a.recv(1024)   #recv接受数据 内的数字指：每次接受的最大字节
#     print(msg.decode('utf-8'))  #打印msg
#     print(b)
#     reg='welcome'  #发送响应
#     a.send(reg.encode('utf-8'))
#     a.close()
#######################################
##udp服务器
while True:
    a,b=s.recvfrom(1024)#接受数据  第一个变量a:客户端发送的请求数据   第二个变量：客服端的ip地址和端口号
    print(a.decode('utf-8'))
    print(b)
    msg='welcom'
    s.sendto(msg.encode('utf-8'),b)#发送相应数据

##################################################################









