# Level09

## Solution

We have an executable and a file named ``token``.

```
$ ls -l
total 12
-rwsr-sr-x 1 flag09 level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09 level09   26 Mar  5  2016 token
```

We can see that the executable rewrites argv 1 by adding index to the character value, and that the token contains unreadable text.

```
$ ./level09 111111
123456
```

```
$ cat token
f4kmm6p|=�p�n��DB�Du{��
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
$ scp -P 4242 level09@192.168.56.101:/home/user/level09/level09 .
```

```
while (true)
{
	v1 += 1;
	v10 = a1->field_4;
	v0 = 4294967295;
	do
	{
		if (!v0)
			break;
	} while (*(v10));
	if (v1 >= ~(v0) - 1)
		break;
	putchar(a1->field_4[v1].field_0 + v1);
}
```

It confirms that the program adds index to the value.
</br>
We can try doing the opposite on the text in the token file.

```
$ cd /tmp
$ vim main.c
$ gcc main.c
$ ./a.out "$(cat /home/user/level09/token)"
f3iji1ju5yuevaus41q1afiuq
```

Create a ``main.c`` file in ``/tmp``, then compile and execute it with the correct argument.
</br>
All you have to do is connect to ``flag09`` and run ``getflag``.

```
$ su flag09
Password: f3iji1ju5yuevaus41q1afiuq
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```