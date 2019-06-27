from platform import platform


def osversion():
    """
    print the current os this module is running on
    Usage: !util osversion
    """
    return platform()
