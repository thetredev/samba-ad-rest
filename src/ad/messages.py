import sys

from ad.constants import ERROR_PREFIX
from ad.constants import MESSAGE_PREFIX


def panic(text: str, exit_code: int):
    print(f"{MESSAGE_PREFIX} {ERROR_PREFIX}: {text}")
    sys.exit(exit_code)
