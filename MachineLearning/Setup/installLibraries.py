# install libraries command

import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'numpy'])

# implement conda as a subprocess:
subprocess.check_call([sys.executable, '-m', 'conda', 'install', 'numpy'])

