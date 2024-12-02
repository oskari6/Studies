import subprocess

# example
result = subprocess.run("dir | findstr .py", shell=True, capture_output=True, text=True)
#print(result.stdout)

# example 2, Command chaining with Popen
dir_process = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, text=True)

findstr_process = subprocess.Popen("findstr .py", shell=True, stdin=dir_process.stdout, stdout=subprocess.PIPE, text=True)

output, _ = findstr_process.communicate()
#print(output)

# redirect >
# equivalent to dir > output.txt
with open("output.txt", "w") as file:
    subprocess.run("dir", shell=True, stdout=file)

# appending >>
#equivalent to dir | findstr .py >> output.txt
with open("output.txt", "a") as file:
    subprocess.run("dir | findstr .py", shell=True, stdout=file)

# combining
# equivalent to dir | findstr .py > py_files.txt
with open("py_files.txt", "w") as file:
    subprocess.run("dir | findstr .py", shell=True, stdout=file)

# filepaths
r"path\to\file"

# findstr ".txt" | sort > sorted_txt_files.txt
dir_process = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, text=True)
findstr_process = subprocess.Popen("findstr .txt", shell=True, stdin=dir_process.stdout, stdout=subprocess.PIPE, text=True)

with open("sorted_txt_files.txt", "w") as file:
    subprocess.run("sort", shell=True, stdin=findstr_process.stdout, stdout=file)

