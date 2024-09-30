import requests

# input deta
url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {
    'sol': 1000,
    'camera': 'fhaz',
    'api_key': 'DEMO_KEY'
}

# Solution
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data.get('photos', [])

    if photos:
        print(f"Found {len(photos)} photos.")
        for index, photo in enumerate(photos):
            image_url = photo['img_src']
            print(f"Downloading photo {index + 1}: {image_url}")

            img_data = requests.get(image_url).content

            with open(f'mars_photo{index + 1}.jpg', 'wb') as my_image_file:
                my_image_file.write(img_data)
    else:
        print("No photos found for the given parameters.")
else:
    print(f"Request error: {response.status_code}")
