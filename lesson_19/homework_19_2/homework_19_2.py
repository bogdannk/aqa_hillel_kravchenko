import requests

# Upload the image
upload_url = 'http://127.0.0.1:8080/upload'
image_path = '/Users/bogdankravcenko/Downloads/sunset.jpg'
with open(image_path, 'rb') as img_file:
    files = {'image': img_file}
    response = requests.post(upload_url, files=files)

if response.status_code == 201:
    image_data = response.json()
    image_url = image_data['image_url']
    print(f"Image uploaded successfully: {image_url}")
else:
    print(f"Failed to upload image: {response.status_code}")

# Get the image URL
get_url = f'http://127.0.0.1:8080/image/{image_path.split("/")[-1]}'
response = requests.get(get_url)

if response.status_code == 200:
    print(f"Image available at: {get_url}")
else:
    print(f"Failed to get image: {response.status_code}")

# Delete the image
delete_url = f'http://127.0.0.1:8080/delete/{image_path.split("/")[-1]}'
response = requests.delete(delete_url)

if response.status_code == 200:
    print(f"Image deleted successfully")
else:
    print(f"Failed to delete image: {response.status_code}")