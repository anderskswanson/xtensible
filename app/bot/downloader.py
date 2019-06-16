import os
from pathlib import Path


_REQ_DL_FAIL = 'Failed to download requirements for file {}'
_REQ_FILE_NF = 'Failed to download requirements: File {} does not exist'


class RequirementDownloaderException(Exception):
    def __init__(self, message):
        super().__init__(message)


def download_requirements(src):
    """
    Download the requirements of a module
    If the source requirements file does not exist,
    or the install fails for any reason,
    raise an exception
    """
    if not Path(src).exists():
        raise FileNotFoundError(_REQ_DL_FAIL.format(src))

    system_code = os.system('pip install -r {}'.format(src))
    if system_code != 0:
        raise RequirementDownloaderException(_REQ_DL_FAIL.format(src))


def download_module(src, dest):
    """
    Download the source code of a module from github if it exists
    """
    pass
