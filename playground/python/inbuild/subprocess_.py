import subprocess
import sys


def sleeping():
    p = subprocess.Popen(["sleep", "3"])
    p2 = subprocess.Popen(["sleep", "5"])
    print("sleeping")
    # import time

    # time.sleep(5)
    print("p1")
    p.communicate()
    print("p2")
    p2.communicate()
    print("end")


sleeping()
# p = subprocess.Popen(["./som.sh"], stdout=subprocess.PIPE)
# for c in iter(lambda: p.stdout.read(1), b""):
#     sys.stdout.buffer.write(c)
#     sys.stdout.flush()
# p.communicate()
# print(p)
# print(p)
