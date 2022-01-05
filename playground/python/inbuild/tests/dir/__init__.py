from const import ENVIRONMENT

print(ENVIRONMENT)

const = __import__(f"{__name__}.{ENVIRONMENT}", fromlist=[ENVIRONMENT])
print(type(const))

__all__ = ["const"]
