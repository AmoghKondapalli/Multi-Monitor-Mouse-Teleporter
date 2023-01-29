import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'opencv-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'mediapipe'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pyautogui'])
