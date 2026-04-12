"""
Simulation Configuration for Rural PV-HCD Framework
Scientific Reports Submission (2026)
"""

# =============================================================================
# Simulation Settings
# =============================================================================
RANDOM_SEED = 42
PRIMARY_TIMESTEP = 60          # seconds (1 minute)
TRANSIENT_TIMESTEP = 1         # seconds
SIMULATION_DURATION_DAYS = 456 # 15 months approx

# =============================================================================
# PV and Battery Parameters
# =============================================================================
PV_CAPACITY_KW = 5.0           # kWp
BATTERY_CAPACITY_KWH = 10.0    # kWh
SYSTEM_VOLTAGE = 48            # V DC
CHARGE_DISCHARGE_RATE = 0.5    # C-rate
SOC_MIN = 0.20
SOC_MAX = 0.80
SOC_CONSERVATIVE_MIN = 0.22    # during pattern change
VOLTAGE_DEVIATION_ALLOWED = 0.07  # ±7%
THD_MAX = 0.05                 # 5%

# =============================================================================
# HCD Metric Weights (Equations 1, 4, 5)
# =============================================================================
# Composite HCD Score H_sim
WEIGHT_D = 0.45
WEIGHT_C = 0.30
WEIGHT_P = 0.25

# Cognitive Suitability C_target
WEIGHT_S = 0.4
WEIGHT_K = 0.3
WEIGHT_T = 0.3

S_MAX = 12
K_MAX = 100
T_MAX = 100.0

# Subject Participation P_target
WEIGHT_E = 0.4
WEIGHT_TAU = 0.3
WEIGHT_R = 0.3
TAU_STD = 2.0                # seconds

# Demand Matching Priority Weights α_i
ALPHA_PEAK = 1.5
ALPHA_NORMAL = 1.0
ALPHA_LOW = 0.5

# =============================================================================
# Multi-Objective Optimization Weights (Equation 5)
# =============================================================================
OPT_WEIGHT_DEMAND = 0.42
OPT_WEIGHT_SELF_CONS = 0.35
OPT_WEIGHT_BATTERY_LIFE = 0.23

BATTERY_RATED_CYCLES = 6000    # typical for LiFePO4

# =============================================================================
# Fuzzy Logic Controller Settings
# =============================================================================
FUZZY_INPUTS = ['season', 'time_of_day', 'farmer_type', 'irradiance']
FUZZY_OUTPUTS = ['load_prediction', 'control_action']
NUM_RULES = 25
COVERAGE_RATE = 0.953
MCU_PREDICTION_TIME_MS = 186
MCU_RAM_USAGE_KB = 27.4

# =============================================================================
# MCU Hardware Constraints
# =============================================================================
MCU_MODEL = "STM32F103C8T6"
MCU_RAM_LIMIT_KB = 20
MCU_CLOCK_MHZ = 72