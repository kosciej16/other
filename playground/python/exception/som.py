class E(Exception):
    pass

try:
    1/0
except Exception as e:
    raise E from e
