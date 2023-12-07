import subprocess
import sys
import os
os.chdir("../")
subprocess.call([sys.executable, '-r requirements.txt', 'pip', 'install']) 
dbutils.library.restartPython()  
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))