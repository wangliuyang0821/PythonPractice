import pandas as pd
from faker import Faker
import random
import os

fake = Faker('en_US')

data = []
for i in range(1,1000):
    gender = random.choice(['Male','Female'])
    first_name = fake.first_name_female() if gender == 'Male' else fake.first_name_male()
    last_name = fake.last_name()

    data.append({
        'id':i,
        'name': f"{first_name} {last_name}",
        'age': random.randint(18,100),
        'address': fake.address().replace('\n',','),
        'email': f"{first_name}{last_name}2099@gmail.com",
        'gender':f"{gender}"
    })

df = pd.DataFrame(data)

df.to_excel("test_data.xlsx",index=False,columns=["id","name","age","address","email","gender"],engine='openpyxl')

print("文件路径：",os.path.abspath("test_data.xlsx"))


