import os
import subprocess
import sys

def create_virtual_env(env_name="myenv"):
    """Creates a virtual environment if it doesn't exist."""
    if not os.path.exists(env_name):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", env_name])
    else:
        print("Virtual environment already exists.")

def install_dependencies(env_name="myenv"):
    """Installs dependencies from requirements.txt into the virtual environment."""
    print("Installing dependencies...")
    # Adjust the pip path based on the OS
    pip_path = os.path.join(env_name, "Scripts", "pip") if os.name == "nt" else os.path.join(env_name, "bin", "pip")
    try:
        subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)

def run_streamlit_app(env_name="myenv"):
    """Runs the Streamlit app using the virtual environment."""
    print("Running Streamlit app...")
    # Adjust the Streamlit executable path based on the OS
    streamlit_path = os.path.join(env_name, "Scripts", "streamlit") if os.name == "nt" else os.path.join(env_name, "bin", "streamlit")
    if not os.path.exists(streamlit_path):
        print("Streamlit is not installed in the virtual environment.")
        sys.exit(1)
    
    # Use the correct path to ui.py
    ui_file_path = os.path.join(os.getcwd(), "Personal Project", "ui.py")
    if not os.path.exists(ui_file_path):
        print(f"Streamlit app file not found: {ui_file_path}")
        sys.exit(1)
    
    try:
        # Run the Streamlit app
        subprocess.run([streamlit_path, "run", ui_file_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to run Streamlit app: {e}")
        sys.exit(1)

def main():
    # Use the correct virtual environment name
    env_name = "myenv"

    try:
        # Step 1: Create Virtual Environment
        create_virtual_env(env_name)

        # Step 2: Install Dependencies
        install_dependencies(env_name)

        # Step 3: Run Streamlit App
        run_streamlit_app(env_name)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
