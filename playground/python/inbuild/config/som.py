import configparser


c = configparser.ConfigParser()
c.read("conf.ini")
s = c.get("API", "key")
print(type(s))
s = int(c.get("API", "iii"))
print((s))
