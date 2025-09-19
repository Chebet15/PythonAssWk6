import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    # Prompt user for the image URL
    url = input("Enter the image URL: ").strip()

    # Create directory for storing images
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Send request to fetch image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder_name, filename)

        # Save image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image successfully downloaded and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please include 'http://' or 'https://'.")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    fetch_image()
