import configparser

config = configparser.ConfigParser()
config.read("som.ini")
raw = config.getboolean("section", "arg")
print(raw)
