import re
import shutil
import sys
from datetime import datetime
from os import path, getcwd, mkdir, remove
from typing import List

def resolve_path():
    return (
        path.abspath(path.dirname(sys.executable))
        if getattr(sys, "frozen", False)
        else path.abspath(path.join(getcwd()))
    )