import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def build_fuzzy_model():
    print("→ 构建轻量化模糊预测模型...")
    season = ctrl.Antecedent(np.arange(0, 2, 1), 'season')
    irradiance = ctrl.Antecedent(np.arange(0, 1001, 1), 'irradiance')
    load_power = ctrl.Consequent(np.arange(0, 6, 1), 'load_power')

    season.automf(2)
    irradiance.automf(3)
    load_power.automf(3)

    rule1 = ctrl.Rule(season['poor'] & irradiance['poor'], load_power['poor'])
    rule2 = ctrl.Rule(season['good'] & irradiance['good'], load_power['good'])
    load_ctrl = ctrl.ControlSystem([rule1, rule2])
    load_sim = ctrl.ControlSystemSimulation(load_ctrl)
    print("✓ 模糊模型构建完成")
    return load_sim