import shutil
import sys
from pathlib import Path

import ad.entry
from ad.messages import panic


def main():
    if not shutil.which("samba-tool"):
        panic("samba-tool not found in PATH", 1)

    if len(sys.argv) == 1:
        panic(f"Please provide a config file", 1)

    config_path = Path(sys.argv[1])
    if not config_path.exists():
        panic(f"Config file {config_path.as_posix()} does not exist", 1)

    ad.entry.main(config_path)
