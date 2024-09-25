import os
import subprocess

# Create virtual environment and install Python dependencies
def setup_backend():
    print("Setting up Python virtual environment...")
    os.makedirs('backend', exist_ok=True)
    subprocess.run(['python3', '-m', 'venv', 'backend/venv'])
    subprocess.run(['backend/venv/bin/pip', 'install', '-r', 'backend/requirements.txt'])
    print("Backend setup complete!")

# Install Node modules for frontend
def setup_frontend():
    print("Installing Node.js dependencies...")
    subprocess.run(['npm', 'install'], cwd='frontend')
    print("Frontend setup complete!")

if __name__ == "__main__":
    setup_backend()
    setup_frontend()
