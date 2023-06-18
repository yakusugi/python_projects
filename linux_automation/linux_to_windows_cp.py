import shutil
import os

src_dir = "/path/to/src/dir/"
dst_dir = "//192.168.0.xxx/path/to/dst/dir"

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)
shutil.copytree(src_dir, dst_dir)