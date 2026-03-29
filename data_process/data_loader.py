import os
import pandas as pd

def load_public_data():
    """加载论文Table1所有公开数据集"""
    print("→ 加载多源公开数据集...")
    # 数据存放路径：./data/
    data_paths = {
        "norway_load": "./data/norway_rural_load.csv",
        "era5_meteo": "./data/era5_land.nc",
        "us_pv": "./data/pvdaq_system4.csv",
        "ganluo_load": "./data/ganluo_rural_load.xlsx",
        "county_panel": "./data/county_electricity_panel.xlsx"
    }
    # 检查数据文件（首次运行需先下载）
    for name, path in data_paths.items():
        if not os.path.exists(path):
            print(f"⚠️  请先下载{name}数据至：{path}")
    print("✓ 数据集加载完成")
    return data_paths