import sys
import subprocess
from typing import List


# List of applications to check for installation.
# Each entry is a list where:
#   - First element [0]: executable application name to test for
#   - Middle elements [1:-1]: parameters to submit to is_application_installed()
#   - Last element [-1]: error message to display if application is not found
applications_to_check = [
    ["poetry", "--version", "Poetry is not installed. Please install Poetry to manage dependencies and virtual environments."],
    # ["docker", "--version", "Docker is not installed. Please install Docker to manage containers."],
    ["git", "--version", "Git is not installed. Please install Git for version control."],
    ["make", "--version", "Make is not installed. Please install Make to use the provided Makefile."],
]

def is_application_installed(app_details: List[str]) -> bool:
    """Check if an Application is installed."""
    
    if len(app_details) < 2:
        print("app_details must contain at least the command to check and the error message.", file=sys.stderr)
        return False
    
    try:
        subprocess.run(app_details[0:-1], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print(app_details[-1], file=sys.stderr)
        return False
    
if __name__ == "__main__":
    
    print("Checking for required applications...\n")
    
    all_installed = True
    for app in applications_to_check:
        if not is_application_installed(app):
            all_installed = False
    
    if all_installed:
        print("All required applications are installed. Proceeding with project generation...\n")
    else:
        print("Please install the missing applications and re-run the project generation.", file=sys.stderr)
        sys.exit(1)        