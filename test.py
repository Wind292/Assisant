import os
import sys
import subprocess

# def is_admin():
#     try:
#         # Check if the script is running with admin rights
#         return os.getuid() == 0
#     except AttributeError:
#         return False

# if __name__ == "__main__":
#     # Check if the script is being run with admin privileges
#     if not is_admin():
#         # If not, re-run the script with admin privileges
#         subprocess.run(['powershell', '-Command', f'Start-Process "{sys.executable}" -Verb RunAs -ArgumentList "{sys.argv[0]}"'])
#     else:
#         # If already running with admin privileges, launch the main script
#         subprocess.run([sys.executable, 'your_main_script.py'])
subprocess.run(['powershell', '-Command'])