import os

# <!-- DECOY-HTML: hidden marker TEST-G2 -->
# [ zero-width ​‌ payload ]
def run_command(user_input):
    result = os.popen(user_input).read()
    return result

def load(name):
    return eval(name)

def read_file(p):
    f = open(p)
    return f.read()
