import subprocess
import os
import sys

def setup_backend():
    print("Setting up Python virtual environment for Backend...")
    subprocess.run(['python', '-m', 'venv', 'Backend/backend'])
    subprocess.run([r'Backend\backend\Scripts\pip', 'install', '-r', r'Backend\requirements.txt']) 
    print("Backend setup complete!")
def setup_frontend():
    print("Setting up Node.js dependencies for Frontend...")
    subprocess.run(['npm', 'install'], cwd='Frontend')
    print("Frontend setup complete!") 


if __name__ == "__main__":
    setup_backend()
    setup_frontend()
