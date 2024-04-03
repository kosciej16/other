from itertools import count
from copy import deepcopy

import warnings

warnings.simplefilter(action="default", category=DeprecationWarning)
i = count(start=5)
next(i)
print(next(i))

j = deepcopy(i)
print(next(j))
print(next(i))
