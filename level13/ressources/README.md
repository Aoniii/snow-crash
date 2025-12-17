# Level13

## Solution

We have an executable file.

```
$ ls -l
total 8
-rwsr-sr-x 1 flag13 level13 7303 Aug 30  2015 level13
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
$ scp -P 4242 level13@192.168.56.101:/home/user/level13/level13 .
```

```
int main()
{
    char *v0;  // [bp-0x10], Other Possible Types: unsigned int
    unsigned int v1;  // [bp-0xc]

    if (getuid() == 4242)
    {
        v0 = ft_des("boe]!ai0FB@.:|L6l@A?>qJ}I");
        return printf("your token is %s\n");
    }
    v1 = 4242;
    v0 = getuid();
    printf("UID %d started us but we we expect %d\n");
    exit(1); /* do not return */
}
```

Here we see that if we manage to pass through the ``if`` statement, we will be able to retrieve the ``token``.
</br>
We will need to change the return value of ``getuid()`` in ``eax`` or ``rax``.
</br>
``eax`` est le registre pour la valeur de retour sur ``x86`` et ``rax`` celui pour ``x86-64``

```
$ file ./level13
./level13: setuid setgid ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xde91cfbf70ca6632d7e4122f8210985dea778605, not stripped
level13@SnowCrash:~$ gdb ./level13
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /home/user/level13/level13...(no debugging symbols found)...done.
(gdb) break getuid
Breakpoint 1 at 0x8048380
(gdb) run
Starting program: /home/user/level13/level13

Breakpoint 1, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
(gdb) finish
Run till exit from #0  0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
0x0804859a in main ()
(gdb) set $eax = 4242
(gdb) continue
Continuing.
your token is 2A31L79asukciNyi8uppkEuSx
[Inferior 1 (process 2147) exited with code 050]
```