# Usage: python deletefiles startdir fileextension

import os
import sys

if len(sys.argv) < 3:
    print("Usage : python deletefiles <startdir> <extension>")
    exit()

startdir = sys.argv[1]
ext = sys.argv[2]

# Create log file
logfile = open("deletefiles.log", "wt")

allfiles = os.walk(startdir)
count = 0
for (dirname, dirs, files) in allfiles:
    for f in files:
        if f.endswith(ext):   # if file is found with given extension
            # Delete file
            filename = dirname + "\\" + f
            try:
                os.remove(filename)
                print(f"Deleted -> {filename}")
                count += 1
            except Exception as ex:
                # write error to log file
                logfile.write(f"While deleting {filename} error is -> {ex}")
                print(f"Error deleting -> {filename}")

logfile.close()
print(f"No. of files deleted : {count}")
