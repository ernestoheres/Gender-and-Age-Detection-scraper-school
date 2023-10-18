import requests
import subprocess
import time
import json
import random

data_list = []

for i in range(20):
    r = requests.get('https://thispersondoesnotexist.com/')
    with open(f"img/image{i}.jpg", 'wb') as f:
        f.write(r.content)
    #verander naar normale python function call?
    result = subprocess.run(["python", "detect.py", "--image", f"img/image{i}.jpg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True  ) 
    result = result.stdout.split('\n')
    gender = result[0]
    print(gender)
    data = {
        "img": f"image{i}.jpg",
        "gender": gender
    }
    data_list.append(data)

    time.sleep(random.randint(5,12))

with open('img/data.json', 'w') as f:
   json.dump(data_list, f, indent=4)
    
