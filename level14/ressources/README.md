# Level14

## Solution

We have nothing to use.

```
$ ls -la
total 12
dr-x------ 1 level14 level14  100 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level14 level14  220 Apr  3  2012 .bash_logout
-r-x------ 1 level14 level14 3518 Aug 30  2015 .bashrc
-r-x------ 1 level14 level14  675 Apr  3  2012 .profile
```

```
$ find / -user level14 2>/dev/null
all useless
```

Let's try reverse ``getflag``.

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
$ scp -P 4242 level14@0.0.0.0:/bin/getflag .
```

```
unsigned int main()
...
if (ptrace(0, 0, 1, 0, 0) < 0)
...
v2 = getuid();
...
```

We must successfully pass the ``ptrace`` verification, then send the correct ``getuid`` of ``flag14``.

```
$ id flag14
uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)
```

Now, let's use gdb.

```
$ gdb getflag
GNU gdb (Ubuntu/Linaro 7.4-2012.04-0ubuntu2.1) 7.4-2012.04
Copyright (C) 2012 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "i686-linux-gnu".
For bug reporting instructions, please see:
<http://bugs.launchpad.net/gdb-linaro/>...
Reading symbols from /bin/getflag...(no debugging symbols found)...done.
(gdb) break ptrace
Breakpoint 1 at 0x8048540
(gdb) break getuid
Breakpoint 2 at 0x80484b0
(gdb) run
Starting program: /bin/getflag

Breakpoint 1, 0xb7f146d0 in ptrace () from /lib/i386-linux-gnu/libc.so.6
(gdb) return (int)0
Make selected stack frame return now? (y or n) y
#0  0x0804898e in main ()
(gdb) continue
Continuing.

Breakpoint 2, 0xb7ee4cc0 in getuid () from /lib/i386-linux-gnu/libc.so.6
(gdb) return (int)3014
Make selected stack frame return now? (y or n) y
#0  0x08048b02 in main ()
(gdb) continue
Continuing.
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```

We place two breakpoints on the functions we are interested in and change the return value.
</br>
This method would surely have worked for all levels.

```
$ su flag14
Password: 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
Congratulation. Type getflag to get the key and send it to me the owner of this livecd :)
$ getflag
Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
```
