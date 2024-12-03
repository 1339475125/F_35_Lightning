import pandas as pd
import random
from faker import Faker


# 生成随机姓名的函数
def generate_random_name():
    fake = Faker("zh_CN")
    return fake.name()


# 生成随机分数的函数
def generate_random_score():
    return random.randint(0, 100)


# 生成指定数量的随机姓名和分数数据
def generate_random_data(num_records):
    data = {
        "姓名": [generate_random_name() for _ in range(num_records)],
        "分数": [generate_random_score() for _ in range(num_records)]
    }

    return data


# 生成CSV文件
def generate_csv_file(data, file_name):
    df = pd.DataFrame(data)
    df.to_csv(file_name, index=False)


if __name__ == "__main__":
    num_records = 10000  # 可以根据需要修改生成的数据记录数量
    file_name = "score.csv"  # 可以根据需要修改文件名
    random_data = generate_random_data(num_records)
    generate_csv_file(random_data, file_name)

    print(f"已生成CSV文件: {file_name}")