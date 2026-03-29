import pandas as pd
import numpy as np
import os

def generate_sim_data():
    """生成模拟负荷/光伏数据，无需外部下载"""
    print("→ 生成内置模拟数据...")
    time_index = pd.date_range('2025-01-01', periods=1000, freq='H')
    df = pd.DataFrame({
        'load_power': np.random.uniform(0.5, 5, 1000),
        'pv_power': np.random.uniform(0, 5, 1000),
        'irradiance': np.random.uniform(0, 1000, 1000)
    }, index=time_index)
    df.to_csv("./data/sim_data.csv")
    print("✓ 模拟数据生成完成")

def fill_missing(df):
    return df.fillna(df.groupby([df.index.month, df.index.hour]).transform('mean'))

def remove_outliers(df, col):
    mean, std = df[col].mean(), df[col].std()
    return df[(df[col] >= mean-3*std) & (df[col] <= mean+3*std)]