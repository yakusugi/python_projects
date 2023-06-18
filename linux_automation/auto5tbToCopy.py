import shutil
import os

src_dir = "/shares/smb/seagate_hdd_5tb/archive_dir/archives"
dst_dir = "/home/johnito/seagate_hdd_100gb_home/archives/archive_dir"

files = os.listdir(src_dir)

for f in files:
    src_file = os.path.join(src_dir, f)
    dst_file = os.path.join(dst_dir, f)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)