# shark on wire 2

## Objetivo

We found this [packet capture](https://jupiter.challenges.picoctf.org/static/b506393b6f9d53b94011df000c534759/capture.pcap). Recover the flag that was pilfered from the network.

## Hints


## Solución

```
┌──(kali㉿kali)-[~/Downloads]
└─$ ls    
capture.pcap  sstv
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ file capture.pcap                            
capture.pcap: pcap capture file, microsecond ts (little-endian) - version 2.4 (Ethernet, capture length 262144)
                                                                                                    
┌──(kali㉿kali)-[~/Downloads]
└─$ wireshark capture.pcap &                                                                   
[1] 61026

┌──(kali㉿kali)-[~/Downloads]
└─$ python3
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> chr(112)
'p'
>>> chr(105)
'i'
>>> chr(99)
'c'
>>> chr(111)
'o'
>>> 
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 -m pip install scapy
Defaulting to user installation because normal site-packages is not writeable
Requirement already satisfied: scapy in /usr/lib/python3/dist-packages (2.5.0)
     
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 exp.py              
<capture.pcap: TCP:138 UDP:614 ICMP:0 Other:574>
┌──(kali㉿kali)-[~/Downloads]
└─$ python3 exp.py
Ether / IPv6 / UDP / DNS Qry "b'_nfs._tcp.local.'" 
Ether / IP / UDP / DNS Qry "b'_nfs._tcp.local.'" 
Ether / IPv6 / UDP / DNS Qry "b'_ftp._tcp.local.'" 
Ether / IP / UDP / DNS Qry "b'_ftp._tcp.local.'" 
Ether / IPv6 / UDP / DNS Qry "b'_nfs._tcp.local.'" 

┌──(kali㉿kali)-[~/Downloads]
└─$ picoCTF{p1LLf3r3d_data_v1a_st3g0}

┌──(kali㉿kali)-[~/Downloads]
└─$ 
```

## Flag

picoCTF{p1LLf3r3d_data_v1a_st3g0}

## Notas adicionales


## Referencias

[scapy](https://scapy.net/)

