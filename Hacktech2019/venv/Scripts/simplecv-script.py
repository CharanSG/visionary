#!"C:\Users\Manish Dhankani\PycharmProjects\Hacktech2019\venv\Scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'SimpleCV==1.3','console_scripts','simplecv'
__requires__ = 'SimpleCV==1.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('SimpleCV==1.3', 'console_scripts', 'simplecv')()
    )
