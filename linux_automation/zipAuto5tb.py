import os
import subprocess
import sys

# Create a log file path in the specified directory
log_dir = '/path/to/archive_dir/logs'
log_file = os.path.join(log_dir, 'log5tb_zip.log')
reading_dir = '/path/to/Python/linux_automation'
reading_file = os.path.join(reading_dir, 'seagate_hdd_5tb_coding_dir.txt')

try:
    with open(reading_file, "r") as f:
        reading_list = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: The file {reading_file} could not be found.")
    sys.exit(1)

for element in reading_list:
    with open(log_file, 'a') as f:
        time = subprocess.run(["date", "+%s"], capture_output=True, text=True).stdout.strip()
        save_dir = '/path/to/save/archive_dir/archives'
        zip_file = os.path.join(save_dir, "data_" + os.path.basename(element) + ".zip")
        output = subprocess.run(["zip", "-r", zip_file, element], capture_output=True, text=True)

        # Write the command's output to the log file
    with open(log_file, 'a') as f:
        f.write(output.stdout)
        if output.returncode !=0:
            f.write(output.stderr)

print("Successfully created zip files for all the directories!")