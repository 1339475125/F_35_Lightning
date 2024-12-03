import csv

def sorted_data(data):
    pass

def read_and_sort_csv(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)

    # 按照第二列进行排序，这里假设第二列的数据类型是可以直接比较的，比如整数或字符串
    sorted_data = sorted(data, key=lambda x: x[1])
    return sorted_data


# 示例用法，将你的实际CSV文件路径替换下面的路径
file_path = 'your_file.csv'
sorted_result = read_and_sort_csv(file_path)
for row in sorted_result:
    print(row)