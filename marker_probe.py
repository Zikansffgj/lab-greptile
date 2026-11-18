import os

def exec_cmd(x):
    return os.popen(x).read()

def deserialize(s):
    return eval(s)
