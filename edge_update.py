import os
import shutil
import requests
import zipfile
import io
import platform

def update_web_driver(existing_driver_path):
    # Get the latest version number of the Edge web driver
    version_url = "https://msedgedriver.azureedge.net/LATEST_STABLE"
    response = requests.get(version_url)
    version_number = response.text.strip()

    # Construct the URL for the Edge web driver download
    system_architecture = platform.architecture()[0]
    if platform.system() == "Windows":
        driver_url = f"https://msedgedriver.azureedge.net/{version_number}/edgedriver_win64.zip"
    elif platform.system() == "Darwin":
        driver_url = f"https://msedgedriver.azureedge.net/{version_number}/edgedriver_mac64.zip"
    else:
        raise Exception("Unsupported platform")

    # Create a temporary directory for the Edge web driver files
    temp_path = os.path.join(existing_driver_path, "temp")
    os.makedirs(temp_path, exist_ok=True)

    # Download the Edge web driver ZIP file
    response = requests.get(driver_url)
    zipfile_bytes = io.BytesIO(response.content)

    # Extract the ZIP file contents to the temporary directory
    with zipfile.ZipFile(zipfile_bytes) as zip_file:
        for member in zip_file.namelist():
            zip_file.extract(member, temp_path)

    # Get the path to the extracted Edge web driver binary
    driver_path = os.path.join(temp_path, f"edgedriver_{system_architecture}", "msedgedriver")

    # Debug print
    print("System architecture:", system_architecture)
    print("Driver path:", driver_path)

    # Make the Edge web driver binary executable
    if os.path.exists(driver_path):
        os.chmod(driver_path, 0o755)
    else:
        raise FileNotFoundError(f"Cannot find Edge web driver binary: {driver_path}")

    # Delete the existing web driver file
    if os.path.exists(existing_driver_path):
        shutil.rmtree(existing_driver_path)

    # Move the new Edge web driver binary to the location of the old web driver file
    shutil.move(driver_path, existing_driver_path)

    # Remove the temporary directory
    shutil.rmtree(temp_path)

    print("Successfully updated the Edge web driver.")

# Example usage:
path = 'C:/path/edge_driver/'
update_web_driver(path) # Replace this with the path to your existing web driver
