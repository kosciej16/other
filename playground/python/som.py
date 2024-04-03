from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class A:
    a: Optional[Any] = None
    b: Any = None


a = A()
a.a.append(1)
a.b.append(1)
