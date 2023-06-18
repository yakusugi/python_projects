#!/usr/bin/python3

import subprocess
dir = input("Enter a directly name: ")
print("You chose", dir + "!")
subprocess.run(["cd $dir"])
