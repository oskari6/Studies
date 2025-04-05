import subprocess

#.run extension

# ["1s, "-1"] list of command line args
# capture_output, captures stdout and stderr
# text, text not bytes

result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

print("Command output: ")
print(result.stdout)

if result.returncode == 0:
    print("Command succeeded")
else:
    print("Command failed with return code: ", result.returncode)

# example
result = subprocess.run(["grep", "hello"], input="hello world\npython scripting",capture_output=True, text=True)
print("filtered output: ", result.stdout)


import subprocess

# long running shell command
process = subprocess.Popen(["ping", "-c", "4", "google.com"], stdout=subprocess.PIPE, text=True)

for line in process.stdout:
    print(line, end="")

process.wait() # wait to complete

# example 2
with open("output.txt", "w") as file:
    subprocess.run(["ls", "-l"], stdout=file)

