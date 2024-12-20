import csv
import json

# 读取CSV文件并转换为JSON格式
def csv_to_json(csv_file_path, json_file_path):
    result = []
    valid_count = 0  # 记录有效行数
    invalid_count = 0  # 记录无效行数

    # 打开CSV文件
    with open(csv_file_path, mode='r', encoding='utf-8-sig') as csv_file:  # 使用 utf-8-sig 去除 BOM
        reader = csv.DictReader(csv_file)
        print("列名:", reader.fieldnames)  # 检查列名
        for row in reader:
            # 检查 answer 列是否为空
            answer_option = row.get('answer', '').strip()  # 获取答案列，并去除空格
            if not answer_option:
                print(f"跳过无效行（答案为空）: {row}")  # 输出提示信息，跳过无效行
                invalid_count += 1  # 无效行计数+1
                continue

            # 检查答案选项是否存在对应列
            answer_content = row.get(answer_option, '').strip()  # 获取答案内容
            if not answer_content:
                print(f"跳过无效行（答案选项无对应内容）: {row}")  # 提示答案内容为空
                invalid_count += 1  # 无效行计数+1
                continue

            # 构造JSON数据
            result.append({
                "instruction": f"{row['question']}",
                "output": f"{answer_content}"
            })
            valid_count += 1  # 有效行计数+1

    # 写入JSON文件
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(result, json_file, ensure_ascii=False, indent=4)

    # 输出有效行和无效行的统计结果
    print(f"有效行数量: {valid_count}")
    print(f"无效行数量: {invalid_count}")
    print(f"无效行比例: {invalid_count / (valid_count + invalid_count) * 100:.2f}%")

# 示例：将csv文件转换为json文件
csv_file_path = '金融文档抽取.csv'  # 替换为你的CSV文件路径
json_file_path = 'output金融文档抽取.json'  # 输出的JSON文件路径

csv_to_json(csv_file_path, json_file_path)

print(f"JSON数据已生成并保存到 {json_file_path}")
