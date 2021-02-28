import sys
import subprocess
import os

# Get the current working directory irrespective of this scripts' execution
getcurrent = os.getcwd()
print(f"Current Working Directory: {getcurrent}")

# Join the current working directory with requirements.txt file
reqAppend = os.path.join(getcurrent, "requirements.txt")
print(reqAppend)

# implement pip as a subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'xmltodict'])
# It works

# Now let's try to install all the packages from requirements.txt file
subprocess.check_call(["pip", 'install', '-r', reqAppend])
# It works


