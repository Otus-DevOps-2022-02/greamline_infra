#!/usr/bin/env python3
import subprocess
from subprocess import Popen, PIPE
HOST = '51.250.107.13'
USER = 'appuser'
PRIVATE_KEY_LOCATION = '~/.ssh/appuser'
print('get parameters')
# output contains stdout, error -- stderr, p.returncode -- exit status.
with Popen(['ssh', '-i', PRIVATE_KEY_LOCATION, '-A', "{}@{}".format(USER, HOST)],
           stdin=PIPE, stdout=PIPE, stderr=PIPE,
           universal_newlines=True) as p:
    output, error = p.communicate("""            
        ip a show eth0 
        hostname
        """)
    print(output)
    print(error)
    print(p.returncode)

