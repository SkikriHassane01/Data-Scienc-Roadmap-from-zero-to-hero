import os
import requests
from bs4 import BeautifulSoup

def download_fruit_images(save_dir='fruit_images'):
    # Step 1: Create directory to store images if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    # Step 2: Define the target URL and request headers
    url = "https://www.istockphoto.com/photos/fruit"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        # Step 3: Send HTTP request to the webpage
        print(f"Fetching URL: {url}")
        response = requests.get(url, headers=headers)
        print(f"Response status: {response.status_code}")
        
        # Step 4: Check if request was successful
        if response.status_code != 200:
            print("Failed to fetch the webpage")
            return
        
        # Step 5: Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')
        print(f"Found {len(images)} images")
        
        # Step 6: Iterate through found images
        count = 0
        for img in images:
            # Step 7: Limit to 5 images
            if count >= 5:
                break
            
            # Step 8: Extract image source URL
            src = img.get('src')
            if not src or not src.startswith('http'):
                continue
            
            try:
                # Step 9: Download individual image
                print(f"Downloading image from: {src}")
                img_response = requests.get(src, headers=headers)
                
                # Step 10: Save image if download successful
                if img_response.status_code == 200:
                    filename = f'fruit_{count + 1}.jpg'
                    filepath = os.path.join(save_dir, filename)
                    
                    # Step 11: Write image content to file
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Successfully downloaded: {filename}")
                    count += 1
                    
            except Exception as e:
                # Step 12: Handle individual image download errors
                print(f"Error downloading image: {str(e)}")
                
    except Exception as e:
        # Step 13: Handle main process errors
        print(f"Main error: {str(e)}")

if __name__ == '__main__':
    # Step 14: Execute main function
    print("Starting download process...")
    download_fruit_images()
    print("Process completed")