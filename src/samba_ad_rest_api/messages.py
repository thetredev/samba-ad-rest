import sys

from samba_ad_rest_api.constants import ERROR_PREFIX
from samba_ad_rest_api.constants import MESSAGE_PREFIX


def panic(text: str, exit_code: int):
    print(f"{MESSAGE_PREFIX} {ERROR_PREFIX}: {text}")
    sys.exit(exit_code)
