import matplotlib.pyplot as plt
import matplotlib.image as mpgimg
import json
import requests

img = mpgimg.imread('unnamed.jpg')
plt.figure(figsize=(10,8))
plt.imshow(img)
plt.show()

client_id = "9n7Sda1ROiwUS7nXkmFl"
client_secret = "_71jNipGf4"
url = "https://openapi.naver.com/v1/vision/face"        # 얼굴 감지.
files = {'image':open('unnamed.jpg', 'rb')}
headers = {'X-Naver_Client-id' : client_id, 'X-Naver-Client=Secret': client_secret }
response = requests.post(url, files=files, headers=headers)

print(response.text)
parsed = json.loads(response.text)
print(parsed)



