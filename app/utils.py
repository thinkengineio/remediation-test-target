import subprocess

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

def run_command(cmd: str) -> str:
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def get_disk_usage() -> str:
    return subprocess.run(["df", "-h"], shell=True, capture_output=True, text=True).stdout
