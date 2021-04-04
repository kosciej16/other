from importlib import import_module

# from . import a as const
from utils import export_config

config = export_config(__name__)
# print(__name__)
# try:
#     mod = import_module(f"{__name__}.d")
#     const.__dict__.update(mod.__dict__)
# except ModuleNotFoundError:
#     pass
