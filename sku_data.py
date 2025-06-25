import pandas as pd
import requests
import os

# 读取 CSV 文件
file_path = "/Users/kayson/Downloads/GTC商品sku数据.csv"
df = pd.read_csv(file_path)

# 创建下载文件夹
download_folder = "/Users/kayson/Downloads/downloaded_images"
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# 遍历每行数据
for index, row in df.iterrows():
    spu_code = str(row['商品编码(spu_code)'])  # 转换为字符串
    product_name = row['商品名称'].replace(" ", "_")  # 替换空格
    image_urls = row['列表图'].split(",")  # 按逗号分割多张图片 URL

    # 遍历每张图片 URL，下载并命名
    for i, url in enumerate(image_urls, 1):
        if url.strip():  # 确保 URL 非空
            file_name = f"{spu_code}_{product_name}_{i}.jpg"
            file_path = os.path.join(download_folder, file_name)

            try:
                response = requests.get(url.strip(), timeout=10)
                response.raise_for_status()
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"下载成功: {file_name}")
            except requests.RequestException as e:
                print(f"下载失败 {url}: {e}")