# Why does this file exist, and why not put this in `__main__`?
#
# You might be tempted to import things from `__main__` later,
# but that will cause problems: the code will get executed twice:
#
# - When you run `python -m pythonscientificcompcourse` python will execute
#   `__main__.py` as a script. That means there won't be any
#   `pythonscientificcompcourse.__main__` in `sys.modules`.
# - When you import `__main__` it will get executed again (as a module) because
#   there's no `pythonscientificcompcourse.__main__` in `sys.modules`.

"""Module that contains the command line application."""


def main(args=None):
    """
    Run the main program.

    This function is executed when you type `pythonscientificcompcourse`
      or `python -m pythonscientificcompcourse`.

    Arguments:
        args: Arguments passed from the command line.

    Returns:
        An exit code.
    """

    print("Hello World", args)
    return 0
