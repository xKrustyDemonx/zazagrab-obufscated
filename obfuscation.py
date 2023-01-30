import os #line:1:import os
import base64 #line:2:import base64
import argparse #line:3:import argparse
import codecs #line:4:import codecs
import random #line:5:import random
import string #line:6:import string
from colorama import Fore #line:7:from colorama import Fore
class Obfuscator :#line:11:class Obfuscator:
    def __init__ (O0O00O0OOOO000000 ,OOOO0OO00000OO0O0 ):#line:12:def __init__(self, code):
        O0O00O0OOOO000000 .code =OOOO0OO00000OO0O0 #line:13:self.code = code
        O0O00O0OOOO000000 .__OOOOOO0O0000O0OO0 ()#line:14:self.__obfuscate()
    def __OO00O0OOO0O0O000O (O0O0OOOOO000O00OO ,O00O0OO0OO000OOOO ,O0OOOOO0OO0OO0000 =None ):#line:16:def __xorED(self, text, key = None):
        OO00000OOOOO0000O =""#line:17:newstring = ""
        if O0OOOOO0OO0OO0000 is None :#line:18:if key is None:
            O0OOOOO0OO0OO0000 ="".join (random .choices (string .digits +string .ascii_letters ,k =random .randint (4 ,8 )))#line:19:key = "".join(random.choices(string.digits + string.ascii_letters, k= random.randint(4, 8)))
        if not O0OOOOO0OO0OO0000 [0 ]==" ":#line:20:if not key[0] == " ":
            O0OOOOO0OO0OO0000 =" "+O0OOOOO0OO0OO0000 #line:21:key = " " + key
        for OO0000O0O00OOOOOO in range (len (O00O0OO0OO000OOOO )):#line:22:for i in range(len(text)):
            OO00000OOOOO0000O +=chr (ord (O00O0OO0OO000OOOO [OO0000O0O00OOOOOO ])^ord (O0OOOOO0OO0OO0000 [(len (O0OOOOO0OO0OO0000 )-2 )+1 ]))#line:23:newstring += chr(ord(text[i]) ^ ord(key[(len(key) - 2) + 1]))
        return (OO00000OOOOO0000O ,O0OOOOO0OO0OO0000 )#line:24:return (newstring, key)
    def __OO0OOO0O000O0O0O0 (O0OO000O0OOOOO00O ,O000O0OOOOOO0000O ):#line:26:def __encodestring(self, string):
        OOOO0O0O0OO0O0OOO =''#line:27:newstring = ''
        for O00OO0O00O00O0OOO in O000O0OOOOOO0000O :#line:28:for i in string:
            if random .choice ([True ,False ]):#line:29:if random.choice([True, False]):
                OOOO0O0O0OO0O0OOO +='\\x'+codecs .encode (O00OO0O00O00O0OOO .encode (),'hex').decode ()#line:30:newstring += '\\x' + codecs.encode(i.encode(), 'hex').decode()
            else :#line:31:else:
                OOOO0O0O0OO0O0OOO +='\\'+oct (ord (O00OO0O00O00O0OOO ))[2 :]#line:32:newstring += '\\' + oct(ord(i))[2:]
        return OOOO0O0O0OO0O0OOO #line:33:return newstring
    def __OOOOOO0O0000O0OO0 (OOOO00OO0OOO00000 ):#line:35:def __obfuscate(self):
        O0O0OOO000OOO00OO =OOOO00OO0OOO00000 .__OO00O0OOO0O0O000O (OOOO00OO0OOO00000 .code )#line:36:xorcod = self.__xorED(self.code)
        OOOO00OO0OOO00000 .code =O0O0OOO000OOO00OO [0 ]#line:37:self.code = xorcod[0]
        O0000000O0OO0OOO0 =base64 .b64encode (codecs .encode (codecs .encode (OOOO00OO0OOO00000 .code .encode (),'bz2'),'uu')).decode ()#line:38:encoded_code = base64.b64encode(codecs.encode(codecs.encode(self.code.encode(), 'bz2'), 'uu')).decode()
        O0000000O0OO0OOO0 =[O0000000O0OO0OOO0 [OOOO000000OO00OOO :OOOO000000OO00OOO +int (len (O0000000O0OO0OOO0 )/4 )]for OOOO000000OO00OOO in range (0 ,len (O0000000O0OO0OOO0 ),int (len (O0000000O0OO0OOO0 )/4 ))]#line:39:encoded_code = [encoded_code[i:i + int(len(encoded_code) / 4)] for i in range(0, len(encoded_code), int(len(encoded_code) / 4))]
        O0O000OO000OO0O00 =[]#line:40:new_encoded_code = []
        O0O000OO000OO0O00 .append (codecs .encode (O0000000O0OO0OOO0 [0 ].encode (),'uu').decode ()+'u')#line:41:new_encoded_code.append(codecs.encode(encoded_code[0].encode(), 'uu').decode() + 'u')
        O0O000OO000OO0O00 .append (codecs .encode (O0000000O0OO0OOO0 [1 ],'rot13')+'r')#line:42:new_encoded_code.append(codecs.encode(encoded_code[1], 'rot13') + 'r')
        O0O000OO000OO0O00 .append (codecs .encode (O0000000O0OO0OOO0 [2 ].encode (),'hex').decode ()+'h')#line:43:new_encoded_code.append(codecs.encode(encoded_code[2].encode(), 'hex').decode() + 'h')
        O0O000OO000OO0O00 .append (base64 .b85encode (codecs .encode (O0000000O0OO0OOO0 [3 ].encode (),'hex')).decode ()+'x')#line:44:new_encoded_code.append(base64.b85encode(codecs.encode(encoded_code[3].encode(), 'hex')).decode() + 'x')
        OOOO00OO0OOO00000 .code =f"""
_____=eval("{OOOO00OO0OOO00000.__encodestring('eval')}");_______=_____("{OOOO00OO0OOO00000.__encodestring('compile')}");______,____=_____(_______("{OOOO00OO0OOO00000.__encodestring("__import__('base64')")}","",_____.__name__)),_____(_______("{OOOO00OO0OOO00000.__encodestring("__import__('codecs')")}","",_____.__name__));____________________=_____("'{OOOO00OO0OOO00000.__encodestring(O0O0OOO000OOO00OO[True])}'");________,_________,__________,___________=_____(_______("{OOOO00OO0OOO00000.__encodestring('exec')}","",_____.__name__)),_____(_______("{OOOO00OO0OOO00000.__encodestring('str.encode')}","",_____.__name__)),_____(_______("{OOOO00OO0OOO00000.__encodestring('isinstance')}","",_____.__name__)),_____(_______("{OOOO00OO0OOO00000.__encodestring('bytes')}","",_____.__name__))
def ___________________(__________, ___________):
    __________=__________.decode()
    _________=""
    if not ___________[False]=="{OOOO00OO0OOO00000.__encodestring(' ')}":
        ___________="{self.__encodestring(' ')}"+___________
    for _ in range(_____("{OOOO00OO0OOO00000.__encodestring('len(__________)')}")):
        _________+=_____("{OOOO00OO0OOO00000.__encodestring('chr(ord(__________[_])^ord(___________[(len(___________) - True*2) + True]))')}")
    return (_________,___________)
def ____________(_____________):
    if(_____________[-True]!=_____(_______("'{OOOO00OO0OOO00000.__encodestring('c________________6s5________________6ardv8')}'[-True*4]","",_____.__name__))):_____________ = _________(_____________)
    if not(__________(_____________, ___________)):_____________ = _____(_______("{OOOO00OO0OOO00000.__encodestring('____.decode(_____________[:-True]')},'{OOOO00OO0OOO00000.__encodestring('rot13')}')","",_____.__name__))
    else:
        if(_____________[-True]==_____(_______("b'{OOOO00OO0OOO00000.__encodestring('f5sfsdfauf85')}'[-True*4]","", _____.__name__))):
            _____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{OOOO00OO0OOO00000.__encodestring('uu')}')","",_____.__name__))
        elif (_____________[-True] ==_____(_______("b'{OOOO00OO0OOO00000.__encodestring('d5sfs1dffhsd8')}'[-True*4]","", _____.__name__))):_____________=_____(_______("{self.__encodestring('____.decode(_____________[:-True]')},'{OOOO00OO0OOO00000.__encodestring('hex')}')","",_____.__name__))
        else:_____________=_____(_______("{OOOO00OO0OOO00000.__encodestring('______.b85decode(_____________[:-True])')}","",_____.__name__));_____________=_____(_______("{OOOO00OO0OOO00000.__encodestring('____.decode(_____________')}, '{self.__encodestring('hex')}')","",_____.__name__))
        _____________=_____(_______("{OOOO00OO0OOO00000.__encodestring('___________.decode(_____________)')}","",_____.__name__))
    return _____________
_________________=_____(_______("{OOOO00OO0OOO00000.__encodestring('___________.decode')}({OOOO00OO0OOO00000.__encodestring(O0O000OO000OO0O00[True*3]).encode()})","",_____.__name__));________________ = _____(_______("{self.__encodestring('___________.decode')}({OOOO00OO0OOO00000.__encodestring(O0O000OO000OO0O00[1]).encode()})","",_____.__name__));__________________=_____(_______("{self.__encodestring('___________.decode')}({OOOO00OO0OOO00000.__encodestring(O0O000OO000OO0O00[True*2]).encode()})","",_____.__name__));______________=_____(_______("{self.__encodestring('___________.decode')}({OOOO00OO0OOO00000.__encodestring(O0O000OO000OO0O00[False]).encode()})","",_____.__name__));_______________=_____(_______("{OOOO00OO0OOO00000.__encodestring('str.join')}('', {OOOO00OO0OOO00000.__encodestring('[____________(x) for x in [______________,________________,__________________,_________________]]')})","", _____.__name__));________(___________________(____.decode(____.decode(______.b64decode(_________(_______________)), "{OOOO00OO0OOO00000.__encodestring("uu")}"),"{OOOO00OO0OOO00000.__encodestring("bz2")}"),____________________)[_____("{OOOO00OO0OOO00000.__encodestring('False')}")])\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"""#line:65:_________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*3]).encode()})","",_____.__name__));________________ = _____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[1]).encode()})","",_____.__name__));__________________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[True*2]).encode()})","",_____.__name__));______________=_____(_______("{self.__encodestring('___________.decode')}({self.__encodestring(new_encoded_code[False]).encode()})","",_____.__name__));_______________=_____(_______("{self.__encodestring('str.join')}('', {self.__encodestring('[____________(x) for x in [______________,________________,__________________,_________________]]')})","", _____.__name__));________(___________________(____.decode(____.decode(______.b64decode(_________(_______________)), "{self.__encodestring("uu")}"),"{self.__encodestring("bz2")}"),____________________)[_____("{self.__encodestring('False')}")])\nimport asyncio, json, ntpath, os, random, re, shutil, sqlite3, subprocess, threading, winreg, zipfile, httpx, psutil, win32gui, win32con, base64, requests, ctypes, time;from sqlite3 import connect;from base64 import b64decode;from urllib.request import Request, urlopen;from shutil import copy2;from datetime import datetime, timedelta, timezone;from sys import argv;from tempfile import gettempdir, mkdtemp;from json import loads, dumps;from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer;from Crypto.Cipher import AES;from PIL import ImageGrab;from win32crypt import CryptUnprotectData"""
def main ():#line:67:def main():
    OO0000000O000O0OO =argparse .ArgumentParser ()#line:68:parser = argparse.ArgumentParser()
    OO0000000O000O0OO .add_argument ('FILE',help ='the target file',metavar ='SOURCE')#line:69:parser.add_argument('FILE', help='the target file', metavar= 'SOURCE')
    OO0000000O000O0OO .add_argument ('-o',metavar ='path',help ='custom output file path')#line:70:parser.add_argument('-o', metavar='path', help='custom output file path')
    OOOO00OO0O0OO0OO0 =OO0000000O000O0OO .parse_args ()#line:71:args = parser.parse_args()
    if OOOO00OO0O0OO0OO0 .o is None :#line:72:if args.o is None:
        OOOO00OO0O0OO0OO0 .o =f'obfuscated_{os.path.basename(OOOO00OO0O0OO0OO0.FILE)}'#line:73:args.o = f'obfuscated_{os.path.basename(args.FILE)}'
    if not os .path .isfile (OOOO00OO0O0OO0OO0 .FILE ):#line:74:if not os.path.isfile(args.FILE):
        print (f'File "{os.path.basename(OOOO00OO0O0OO0OO0.FILE)}" is not found')#line:75:print(f'File "{os.path.basename(args.FILE)}" is not found')
        exit ()#line:76:exit()
    elif not 'py'in os .path .basename (OOOO00OO0O0OO0OO0 .FILE ).split ('.')[-1 ]:#line:77:elif not 'py' in os.path.basename(args.FILE).split('.')[-1]:
        print (f'''File "{os.path.basename(OOOO00OO0O0OO0OO0.FILE)}" is not a '.py' file''')#line:78:print(f'''File "{os.path.basename(args.FILE)}" is not a '.py' file''')
        exit ()#line:79:exit()
    with open (OOOO00OO0O0OO0OO0 .FILE ,encoding ='utf-8')as OOOOO0000O0O0OO0O :#line:80:with open(args.FILE, encoding='utf-8') as file:
        OO0OO00O00OOOOOOO =OOOOO0000O0O0OO0O .read ()#line:81:CODE = file.read()
    OOOOOOO0O000O00O0 =Obfuscator (OO0OO00O00OOOOOOO )#line:82:obfuscator = Obfuscator(CODE)
    with open (OOOO00OO0O0OO0OO0 .o ,'w',encoding ='utf-8')as O0O000OO0OOOOOO0O :#line:83:with open(args.o, 'w', encoding='utf-8') as output_file:
        O0O000OO0OOOOOO0O .write (OOOOOOO0O000O00O0 .code )#line:84:output_file.write(obfuscator.code)
    print (f'{Fore.MAGENTA}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}{Fore.WHITE} Code obfuscated!{Fore.RESET}')#line:85:print(f'{Fore.MAGENTA}[{Fore.RESET}{Fore.WHITE}+{Fore.RESET}{Fore.MAGENTA}]{Fore.RESET}{Fore.WHITE} Code obfuscated!{Fore.RESET}')
if __name__ =='__main__':#line:87:if __name__ == '__main__':
    main ()
    
