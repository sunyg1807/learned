#s客服端
import  socket
#创建socket 封装协议
# sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建socket，封装协议（ipv4协议，tcp的协议）
# sock.connect(('192.168.0.53',3000))###链接服务器
# aaa='nihao'###发送的内容
# sock.send(aaa.encode('utf-8'))####给服务器的编码方式
# msg=sock.recv(1024)###传输数据的最大字节
# print(msg.decode('utf-8'))###服务器返回的数据


#udp的
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建socket，封装协议（ipv4协议，tcp的协议）
a=('192.168.0.53',3000)
reg="俺老孙来也"
sock.sendto(reg.encode('utf-8'),a)
c=sock.recv(2048)
print(c.decode('utf-8'))