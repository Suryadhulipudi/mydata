#Method-1
import os
import sys
import subprocess
import string
import random

bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile='/tmp/'+bashfile+'.sh'

f = open(bashfile, 'w')
s = """ awk -F\\| '$2 ~ /^E/    { a[$3]++ } END { for (f in a) print f, a[f] }' ~/*/*/*g | sort -k2nr
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)

#Method-2
import os
import glob

dir_path = "/tmp/logs"
files = glob.glob(os.path.join(dir_path, "*.log"))
output = {}


for file_path in files:
    with open(file_path, "r") as file:
        for line in file:
            Error = line.split("|")[1]
            if Error == "ERROR":
                source_file = line.split("|")[2]
                if source_file in output:
                    value = output[source_file] + 1
                    output.update({source_file: value})
                else:
                    output.update({source_file: 1})



def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

sorted_dict = sort_dict_by_value(output, True)

for key, value in sorted_dict.items():
    print(key, value)
