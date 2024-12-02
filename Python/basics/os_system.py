import os

# cant campture stdout or stderr directly
# less secure than subprocess and vulnerable to attacks
current_dir = os.getcwd()
os.mkdir("example_dir")
os.rename("example_dir", "renamed_dir")
os.rmdir("renamed_dir")

exit_code = os.system("ls -l")

if exit_code == 0:
    print("command succeeded")
else:
    print(f"command failed with exit code: {exit_code}")