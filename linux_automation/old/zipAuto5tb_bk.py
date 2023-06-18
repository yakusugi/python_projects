import os
import subprocess

time = subprocess.run(["date", "+%s"], capture_output=True, text=True).stdout.strip()

save_dir = '/home/johnito/seagate_hdd_100gb_home'
tar_file = os.path.join(save_dir, "data_" + time + ".tar.xz")

subprocess.run(["tar", "-Jcvf", tar_file, "/shares/smb/seagate_hdd_5tb"], capture_output=True, text=True)
