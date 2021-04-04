from importlib import import_module

# from core.config import ENVIRONMENT


ENVIRONMENT = "c"


def export_config(dir):
    const = import_module(f"{dir}.common")
    try:
        env_module = import_module(f"{dir}.{ENVIRONMENT}")
        const.__dict__.update(env_module.__dict__)
    except ModuleNotFoundError:
        pass

    return const
