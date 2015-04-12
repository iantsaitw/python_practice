import sys
from subprocess import call
sys.path.append("/home/yntsai/python_practice/lib/")
from utlis import *

def call_cmd(cmd):
    call([cmd], shell=True)

call_cmd("echo call_cmd")
command("ls")
command("echo Hello")

