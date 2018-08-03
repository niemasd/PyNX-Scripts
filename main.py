from _nx import gfx_set_mode
from glob import glob
from nx.utils import AnsiMenu
from os import chdir
from os.path import isdir,isfile
from runpy import run_path
import sys
sys.argv = ['']
TILED_DOUBLE = 1
MAIN_PY = "main.py"

def run_python_module(path: str):
    run_path(path, run_name='__main__')
    gfx_set_mode(TILED_DOUBLE)

if __name__ == '__main__':
    while True:
        dirs = sorted(['../'] + glob('*/'))
        scripts = sorted(glob('*.py') + glob('*.PY'))
        listing = dirs + scripts
        file_menu = AnsiMenu(listing)
        selected = listing[file_menu.query()]
        if isdir(selected):
            main_file = "%s/%s" % (selected,MAIN_PY)
            if isfile(main_file):
                run_python_module(main_file)
            else:
                chdir(selected)
        elif selected.lower().endswith('.py'):
            run_python_module(selected)
