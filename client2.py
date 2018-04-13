from socket import  *

s = socket ()
minhastr = "Mario!!\r\n"
print (minhastr)
meusbytes=str.encode (minhastr, "UTF-8")

s.connect(("10.10.13.1", 8752))


while 1:
		meusbytes = input()
		s.send (str.encode(meusbytes, "UFT-8"))

data = s.recv (1024)

print (data.decode("utf-8"))

s.close ()

#threads=[]
#for i in range (2):
#	threads.append(threading.thread(target=prod, args=(i,)))
#	conn.
