import subprocess
import sys
subprocess.call([sys.executable, '-r ../requirements.txt', 'pip', 'install'])    
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))