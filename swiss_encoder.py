#!/usr/bin/python3
from base64 import b64encode as base64_encode
from sys import argv
from urllib.parse import quote_plus as url_encode
'''
If you ever need to convert one of your oneliner payload into a 'safe' format and 
had to do it manually I feel your pain. Thats why I have created this tool.
'''

helpmsg = '''
swiss_encoder, the encoding swiss army knife of oneliners.

Usage: swiss_encoder <ACTION> [oneliner]
<> mandatory, [] optional
*** If using special characters like ';' you should omitte the oneliner argument ***
            ***  and use the prompt that follows to input your oneliner *** 

ACTIONS:
    base64     = base64 for linux (UTF-8)
    win64      = base64 for WINDOWS(UTF-16LE)
    url        = url safe encodeing for web interactions 

oneliner       = the payload that needs to be encoded. 
'''

#argv = ['winbase64', 'write-host hello world']
arguments = argv[1:]
option  = arguments.pop(0)

if len(arguments) >= 1:
    payload = ' '.join(arguments)
else:
    payload = input('paste your oneliner below:\n')


if option == 'url':
    print(url_encode(payload))

elif option == 'base64':
    bpayload   = payload.encode()
    b64payload = base64.b64encode(bpayload)
    print(b64payload.decode())

elif option == 'win64':
    bpayload   = payload.encode('utf-16le')
    b64payload = base64_encode(bpayload)
    print("powershell -e", b64payload.decode())
else:
    print(helpmsg)
