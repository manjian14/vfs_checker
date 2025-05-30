import os
import sys
import platform
import subprocess

COUNTRY_CODE_MAP = {
    "france": "fra",
    "germany": "deu",
    "italy": "ita",
    "greece": "grc",
    "spain": "esp"
}

def activate_and_run(destination_name):
    system = platform.system().lower()

    country_code = COUNTRY_CODE_MAP.get(destination_name.lower())
    if not country_code:
        print(f"❌ Unsupported country: {destination_name}")
        print("Available options:", ", ".join(COUNTRY_CODE_MAP.keys()))
        return

    print(f"🌍 Target country: {destination_name.capitalize()} → code: {country_code}")

    if system == "windows":
        activate_cmd = ".venv\\Scripts\\activate.bat &&"
        python_cmd = f"python vfs_checker.py {country_code}"
        full_cmd = f'{activate_cmd} {python_cmd}'
        subprocess.run(["cmd.exe", "/c", full_cmd])
    elif system == "linux":
        activate_cmd = "source .venv/bin/activate"
        python_cmd = f"python3 vfs_checker.py {country_code}"
        full_cmd = f'{activate_cmd} && {python_cmd}'
        subprocess.run(["bash", "-c", full_cmd])
    else:
        print("❌ Unsupported OS:", system)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_bot.py <country_name>")
        print("Example: python run_bot.py italy")
        sys.exit(1)

    activate_and_run(sys.argv[1])
