import pandas as pd
import re

# 尝试读取Excel文件，从第二行开始读取
try:
    df = pd.read_excel('/Users/kayson/Downloads/batch_product_fail_info_1726219961019.xlsx', sheet_name=0, header=None, skiprows=1)
    #df = pd.read_excel('/Users/kayson/Downloads/batch_product_fail_info_1726210133233.xlsx', sheet_name=0, skiprows=1)
except FileNotFoundError:
    print("指定的Excel文件未找到，请检查路径是否正确。")
    exit(1)
except ImportError as e:
    print(f"缺少必要的库 'openpyxl'。请确保已安装 openpyxl。错误信息：{e}")
    exit(1)
except Exception as e:
    print(f"读取Excel文件时发生错误：{e}")
    exit(1)

# 假设错误信息在名为'message'的列中
# 如果列名不同，请替换为实际的列名
# column_name = 'A'
# if column_name in df.columns:
#     messages = df[column_name]
# else:
#     print(f"警告：列名'{column_name}'不存在！")
#     messages = []

# 检查DataFrame是否为空
if df.empty:
    print("读取的Excel文件为空。")
    exit(1)


# 打印DataFrame以检查数据
print(df.head())

try:
    messages = df[0]
except KeyError:
    print("读取的Excel文件中没有有效的数据列。")
    exit(1)

# 定义一个函数来从每个消息中提取门店ID
def extract_store_id(message):
    match = re.search(r'门店ID\s*\[(\d+)\]', message, re.IGNORECASE)
    if match:
        return match.group(1)
    return None

# 使用列表推导式一次性过滤掉None值
# 遍历messages列表中的每个元素该行代码的功能如下：
# 遍历messages列表中的每个元素（假设为msg）。
# 对每个msg调用extract_store_id函数提取店ID。
# 如果extract_store_id(msg)返回的值为真（即非空或非零等），则保留这个返回值。
# 最终生成一个新的列表store_ids，包含所有有效的店ID。
store_ids = [extract_store_id(msg) for msg in messages if extract_store_id(msg)]

# 直接计算去重后的数量
count_unique_store_ids = len(set(store_ids))
new_store_ids = set(store_ids)
for id in new_store_ids:
    print(id)

print(f"不同的门店ID数量: {count_unique_store_ids}")
