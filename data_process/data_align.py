import pandas as pd

def align_spatiotemporal():
    print("→ 数据时空对齐...")
    df = pd.read_csv("./data/sim_data.csv", index_col=0, parse_dates=True)
    df = df.resample("H").mean()
    df["season"] = df.index.month.map(lambda x: 1 if x in [5,6,7,10] else 0)
    df.to_csv("./data/aligned_data.csv")
    print("✓ 时空对齐完成")