# Level02

## Solution

We have a .pcap file in the home directory (a .pcap file is a network packet capture).

```
$ ls -l
total 12
----r--r-- 1 flag02 level02 8302 Aug 30  2015 level02.pcap
```

We will download it to our environment to have access to tools.

```
$ scp -P 4242 level02@0.0.0.0:/home/user/level02/level02.pcap .
```

We will use tshark to read this file (it is like Wireshark, but in command line).

```
$ tshark -r level02.pcap
    1   0.000000 59.233.235.218 → 59.233.235.223 TCP 74 39247 → 12121 [SYN] Seq=0 Win=14600 Len=0 MSS=1460 SACK_PERM TSval=1859280 TSecr=0 WS=128
	...
```

Here we can see that it is a TCP communication.
</br>
We will now reread this file with tshark, specifying that it is TCP and that we want to see the hex dump.

```
$ tshark -r level02.pcap -z follow,tcp,hex,0
...
000000D6  00 0d 0a 50 61 73 73 77  6f 72 64 3a 20           ...Passw ord:
000000B9  66                                                f
000000BA  74                                                t
000000BB  5f                                                _
000000BC  77                                                w
000000BD  61                                                a
000000BE  6e                                                n
000000BF  64                                                d
000000C0  72                                                r
000000C1  7f                                                .
000000C2  7f                                                .
000000C3  7f                                                .
000000C4  4e                                                N
000000C5  44                                                D
000000C6  52                                                R
000000C7  65                                                e
000000C8  6c                                                l
000000C9  7f                                                .
000000CA  4c                                                L
000000CB  30                                                0
000000CC  4c                                                L
000000CD  0d                                                .
...
```

We can see that the password entered is something close to ``ft_wandr...NDRel.L0L.``
</br>
But the . represent non-displayable characters
</br>
Let's try to look in the ASCII table to see what 7f and 0d correspond to.
</br></br>
7f correspond to DEL (delete)
</br>
0d correspond to CR (Carriage Return)
</br></br>
With this, we can determine that the password is ``ft_waNDReL0L``

```
$ su flag02
Password:
Don't forget to launch getflag !
$ getflag
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```
