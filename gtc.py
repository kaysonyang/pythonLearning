import pandas as pd
import json

# 读取 CSV 文件
df = pd.read_csv('/Users/kayson/Downloads/test——sku.csv')

# 定义解析函数
def parse_specs(specs_json):
    if pd.isna(specs_json) or specs_json == "":
        return "无规格"
    try:
        specs_data = json.loads(specs_json)
        result = {}
        for spec in specs_data:
            spec_name = spec['specConfigName']
            spec_values = [sv['value'] for sv in spec['specValues']]  # 取所有 value
            if spec_values:
                result[spec_name] = f"【{'|'.join(spec_values)}】"
        return ", ".join([f"{k}{v}" for k, v in result.items()])
    except json.JSONDecodeError:
        return "无效规格"

# 应用解析函数到 specs 列
df['规格'] = df['规格'].apply(parse_specs)

# 保存到新 CSV 文件
df.to_csv('gtc_sku_processed.csv', index=False, encoding='utf-8-sig')

print("CSV 文件已处理并保存为 gtc_sku_processed.csv！")