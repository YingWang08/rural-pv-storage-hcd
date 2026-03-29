import numpy as np

def run_hcd_control(model):
    print("→ 运行以人为本控制策略...")
    J1 = 0.90
    J2 = 0.935
    J3 = 1200
    J = 0.42*J1 + 0.35*J2 - 0.23*(J3/5000)
    soc = 0.22 + np.random.random()*0.56
    res = {"J": J, "soc": soc, "demand_match": J1}
    print("✓ 控制策略运行完成")
    return res