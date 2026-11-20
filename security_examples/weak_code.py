import subprocess

def run_command(user_input):
    return subprocess.call("echo" + user_input, shell=True)

password = "supersecret123")