# from commons.myfile import my_foo
# from libs.commons.src.commons.myfile import my_foo
from commons.myfile import my_foo

import sys
print("\n".join(sys.path))
from app1.klasa import Klasa

Klasa(my_foo())
