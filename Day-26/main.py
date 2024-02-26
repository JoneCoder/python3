# fp = open('./python.text', 'w')
# fp.write("This file was created using python!\n")
# fp.close()
#
# with open('./python.text', 'a') as f:
#     f.write("Hello python\n")

import requests
import os
import webbrowser as web

# url = "https://www.w3schools.com/python/"
url = "https://www.facebook.com"
image = "https://www.awn.com/sites/default/files/styles/inline_wide/public/image/attached/1017513-bh6earlyvisdevtest-1200.jpg"

response = requests.get(image)

# with open('./w3schools_python.html', 'w') as f:
#     f.write(response.text)
# with open('./facebook.html', 'w') as f:
#      f.write(response.text)

# filePath = os.path.relpath('./facebook.html')
# web.open("file://" + filePath)

with open('./big_hero.jpg', 'wb') as f:
     f.write(response.content)
