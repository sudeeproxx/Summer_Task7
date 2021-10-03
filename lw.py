#!/usr/bin/python3
import cgi
import os
import subprocess
import time

print("content-type: text/html")
print()


print("Hello from backend")
print()
print("$os.open")
f=cgi.FieldStorage()
cmd=f.getvalue("x")
o=subprocess.getoutput("sudo "+ cmd)
print(o)
