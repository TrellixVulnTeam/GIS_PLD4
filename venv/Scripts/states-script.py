#!C:\Users\Joe\PycharmProjects\GIS\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'us==1.0.0','console_scripts','states'
__requires__ = 'us==1.0.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('us==1.0.0', 'console_scripts', 'states')()
    )
