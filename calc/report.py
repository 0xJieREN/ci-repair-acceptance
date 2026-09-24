from calc.mathutil import inclusive_sum
from calc.text import slugify


def summary(name: str, start: int, end: int) -> str:
    return f"{slugify(name)}: {inclusive_sum(start, end)}"
