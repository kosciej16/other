import time
import glob
import subprocess
import os
import signal


m = set()
fid = 0


# def find_free():
#     v = m.values()
#     for i in range(100):
#         if i not in v:
#             return i


def redraw():
    # find_and_kill()
    g = glob.glob("./screenshots/*")
    for f in g:
        subprocess.run(["open", str(f)])
        time.sleep(1)


def find_and_kill():
    ps = subprocess.Popen(("ps", "aux"), stdout=subprocess.PIPE)
    out1 = subprocess.Popen(("grep", "-v", "grep"), stdin=ps.stdout, stdout=subprocess.PIPE)
    out2 = subprocess.Popen(("grep", "-v", "grep"), stdin=out1.stdout, stdout=subprocess.PIPE)
    out3 = subprocess.Popen(
        ("grep", "-i", "preview.app"), stdin=out2.stdout, stdout=subprocess.PIPE
    )
    out4 = subprocess.check_output(("awk", "{print $2;}"), stdin=out3.stdout, text=True)
    if out4:
        os.kill(int(out4), signal.SIGTERM)  # or signal.SIGKILL


while True:
    g = glob.glob("./screenshots/*")
    for f in g:
        if f not in m:
            redraw()
            m.add(f)
    time.sleep(10)
