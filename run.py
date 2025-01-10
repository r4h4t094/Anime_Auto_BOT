import os
import subprocess
import sys

def install_docker():
    """Installs Docker on the system if it is not already installed."""
    try:
        subprocess.run(["docker", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Docker is already installed.")
    except FileNotFoundError:
        print("Docker is not installed. Installing Docker...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "apt-transport-https", "ca-certificates", "curl", "software-properties-common"], check=True)
        subprocess.run(["curl", "-fsSL", "https://download.docker.com/linux/ubuntu/gpg"], stdout=subprocess.PIPE, check=True)
        subprocess.run(["sudo", "gpg", "--dearmor", "-o", "/usr/share/keyrings/docker-archive-keyring.gpg"], check=True)
        subprocess.run(["echo", "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"], shell=True, check=True)
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "docker-ce"], check=True)
        print("Docker installation completed.")

    # Start Docker service
    subprocess.run(["sudo", "systemctl", "start", "docker"], check=True)
    subprocess.run(["sudo", "systemctl", "enable", "docker"], check=True)


def build_and_run_docker():
    """Builds and runs a Docker container using the provided Dockerfile."""
    # Write the Dockerfile content to a file
    dockerfile_content = """FROM python:3.10.4-slim-buster

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

RUN apt -qq update && apt -qq install -y git wget pv jq python3-dev mediainfo gcc aria2 libsm6 libxext6 libfontconfig1 libxrender1 libgl1-mesa-glx ffmpeg

COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt

#CMD [\"bash\",\"pkg.sh\"]
CMD [\"bash\",\"run.sh\"]
"""

    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)

    # Build the Docker image
    image_name = "custom_python_app"
    print("Building the Docker image...")
    subprocess.run(["docker", "build", "-t", image_name, "."], check=True)

    # Run the Docker container
    print("Running the Docker container...")
    subprocess.run(["docker", "run", "-it", image_name], check=True)


def main():
    # Check for root privileges by attempting a privileged command
    try:
        subprocess.run(["sudo", "-n", "true"], check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("This script requires root privileges. Please run as root or with sudo.")
        sys.exit(1)

    try:
        install_docker()
        build_and_run_docker()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
