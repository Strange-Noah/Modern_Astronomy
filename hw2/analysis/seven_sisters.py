import os
import pandas as pd
from sklearn.cluster import DBSCAN

# 获取当前脚本所在目录
base_dir = os.path.dirname(os.path.abspath(__file__))

# 拼接文件路径（和.py在同一目录）
file_path = os.path.join(base_dir, "gaia.xlsx")

# 读取Excel
df = pd.read_excel(file_path)

# 转为数值（保险）
df = df.apply(pd.to_numeric, errors='coerce')

# 删除缺失值
df = df.dropna()

# 选取特征（根据你的列名）
X = df[[
    "pm_RA",
    "pm_Dec",
    "Distance (pc)"
]]

# DBSCAN 聚类
clustering = DBSCAN(eps=2, min_samples=5).fit(X)

# 保存结果
df["cluster"] = clustering.labels_

# 输出每一类的数量
print(df["cluster"].value_counts())

# 输出前几行看看
# print(df.head())

# 只选 Pleiades 成员
members = df[df["cluster"] == 0]

# 找最亮的7颗（Gp越小越亮）
seven_sisters = members.sort_values(by="Gp").head(7)

# 输出编号
print("Seven Sisters (by Number):")
print(seven_sisters["Number"].values)

# 如果想看详细信息
print(seven_sisters[["Number", "RA", "Dec", "Gp"]])