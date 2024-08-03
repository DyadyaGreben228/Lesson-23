##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
##'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#
#
#
#
#import requests
#import aiohttp
#import asyncio
#import os
#
#async def download_image(session, url, filename):
#    async with session.get(url) as response:
#        if response.status == 200:
#            image_data = await response.read()
#            with open(filename, 'wb') as f:
#                f.write(image_data)
#
#async def fetch_images(urls):
#    tasks = []
#    async with aiohttp.ClientSession() as session:
#        for i, url in enumerate(urls):
#            filename = f'image_{i+1}.jpg'  
#            tasks.append(download_image(session, url, filename))
#        await asyncio.gather(*tasks)
#
#def download_images_with_aiohttp():
#   
#    image_urls = [
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#        'https://kinogo.so/uploads/posts/2021-12/690133_1639957322.jpg',
#    ]
#
#    asyncio.run(fetch_images(image_urls))
#
#def save_images_to_folders():
#    images_directory = 'F:\КОМПЬЮТЕРНЫЕКУРСЫЧАСТЬ4\Lesson 23\images' 
#    os.makedirs(images_directory, exist_ok=True)
#
#    
#    for i in range(1, 11):
#        folder_name = os.path.join(images_directory, f'image_{i}')
#        os.makedirs(folder_name, exist_ok=True)
#
#    print(f'Created {len(os.listdir(images_directory))} directories.')
#
#
#download_images_with_aiohttp()    
#save_images_to_folders()



import requests
from bs4 import BeautifulSoup

def get_weather_astana():
    url = "https://www.gismeteo.kz/weather-astana-5164/now/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }  # Добавляем заголовок User-Agent для обхода защиты от парсинга
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        temperature_tag = soup.find("span", class_="js_value tab-weather__value_l")
        temperature = temperature_tag.text.strip() if temperature_tag else "Нет данных"
        
        feels_like_tag = soup.find("span", class_="tab-weather__feels-like-value")
        feels_like = feels_like_tag.text.strip() if feels_like_tag else "Нет данных"
        
        conditions_tag = soup.find("div", class_="tab-weather__desc")
        conditions = conditions_tag.text.strip() if conditions_tag else "Нет данных"
        
        wind_tag = soup.find("span", class_="tab-weather__value_mph")
        wind = wind_tag.text.strip() if wind_tag else "Нет данных"
        
        weather_info = {
            "temperature": temperature,
            "feels_like": feels_like,
            "conditions": conditions,
            "wind": wind
        }
        
        return weather_info
    else:
        print("Ошибка при получении данных:", response.status_code)

# Пример использования
weather_data = get_weather_astana()
if weather_data:
    print("Температура:", weather_data["temperature"])
    print("Ощущается как:", weather_data["feels_like"])
    print("Условия:", weather_data["conditions"])
    print("Ветер:", weather_data["wind"])
else:
    print("Не удалось получить данные о погоде.")









