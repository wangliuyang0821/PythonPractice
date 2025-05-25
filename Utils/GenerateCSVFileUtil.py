import csv
from faker import Faker
import random

# 初始化Faker实例（默认生成英文数据，如需中文则改为Faker('zh_CN')）
fake = Faker()

# 生成100条数据
data = []
for id in range(1, 101):
    record = {
        "id": id,
        "age": random.randint(18, 80),
        "name": fake.name(),
        "address": fake.address().replace('\n', ', ')  # 将地址中的换行符替换为逗号
    }
    data.append(record)

# 写入CSV文件
with open('../files/csv/user_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'age', 'name', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)  # 自动处理特殊字符[3](@ref)

    writer.writeheader()
    writer.writerows(data)