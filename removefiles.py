import os
import time
import shutil

ctime = os.stat(path).st_ctime
os.remove(path)
