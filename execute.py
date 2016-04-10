import sys
from workflow import Workflow
from cStringIO import StringIO

import __builtin__
try:
    from numpy import *
except ImportError:
    pass
from math import *
from random import *
from re import *
from calendar import *
from os.path import *
from shutil import *
from json import *
from time import *
from macostools import *

import contextlib
@contextlib.contextmanager
def capture():
    import sys
    from cStringIO import StringIO
    oldout,olderr = sys.stdout, sys.stderr
    try:
        out=[StringIO(), StringIO()]
        sys.stdout,sys.stderr = out
        yield out
    finally:
        sys.stdout,sys.stderr = oldout, olderr
        out[0] = out[0].getvalue()
        out[1] = out[1].getvalue()

def main(wf):
    args = wf.args
    command = ' '.join(args)
    answer = None
    with capture() as out:
        try:
            answer = eval(__builtin__.compile(command, '<string>', 'single'))
        except Exception as e:
            answer = str(e)
    if answer is None:
        if not out[0]:
            answer = "None"
        else:
            answer = out[0]
    wf.add_item(title=str(answer), subtitle="Press enter to copy to clipboard.", arg=str(answer), valid=True)
    wf.send_feedback()

if __name__ == "__main__":
    wf = Workflow()
    sys.exit(wf.run(main))