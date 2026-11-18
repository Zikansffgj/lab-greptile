import os

def exec_cmd2(x):
    return os.popen(x).read()

def deserialize2(s):
    return eval(s)
