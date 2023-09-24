import requests
import subprocess
import time
import csv
import random

for i in range(500):
    r = requests.get('https://thispersondoesnotexist.com/')
    with open(f"img/image{i}.jpg", 'wb') as f:
        f.write(r.content)
    #verander naar normale python function call?
    result = subprocess.run(["python", "detect.py", "--image", f"img/image{i}.jpg"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True  ) 
    result = result.stdout.split('\n')
    gender = result[0]
    print(gender)
    with open('img/data.csv', 'a') as f:
        writer = csv.writer(f)
        data = [f"image{i}.jpg", gender]
        writer.writerow(data)
    print(gender, f"image{i}.jpg")
    
    time.sleep(random.randint(20,87))



