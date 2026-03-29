#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from data_process.data_clean import generate_sim_data
from data_process.data_align import align_spatiotemporal
from model.fuzzy_model import build_fuzzy_model
from control.hcd_control import run_hcd_control
from simulation.scenario_sim import run_all_scenario
from evaluation.hcd_metrics import calc_all_hcd_metrics
from evaluation.stat_test import run_stat_test

os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

if __name__ == "__main__":
    print("===== 农村户用光伏储能HCD仿真【修复版】开始 =====")
    generate_sim_data()       # 内置模拟数据，无需下载！
    align_spatiotemporal()
    model = build_fuzzy_model()
    control_res = run_hcd_control(model)
    sim_res = run_all_scenario(control_res)
    metrics = calc_all_hcd_metrics(sim_res)
    run_stat_test(metrics)
    print("===== ✅ 全流程完成！结果保存在 ./results/ =====")