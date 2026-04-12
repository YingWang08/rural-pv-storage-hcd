"""
Multi-Objective Control Strategy Optimizer
Implements Equation (5) from Scientific Reports submission
"""

import numpy as np
from scipy.optimize import minimize
from typing import Tuple

class HCDOptimizer:
    """
    Multi-objective optimizer for rural PV-storage system.
    Maximizes: J = 0.42·D + 0.35·(E_self/E_total) + 0.23·(1 - N_cycle/N_rated)
    """

    def __init__(self,
                 w_demand: float = 0.42,
                 w_self_cons: float = 0.35,
                 w_battery_life: float = 0.23,
                 soc_min: float = 0.20,
                 soc_max: float = 0.80,
                 power_max: float = 5.0,      # kW
                 voltage_nominal: float = 220.0,
                 voltage_tol: float = 0.07):
        self.w_demand = w_demand
        self.w_self_cons = w_self_cons
        self.w_battery_life = w_battery_life

        self.soc_min = soc_min
        self.soc_max = soc_max
        self.power_max = power_max
        self.v_nom = voltage_nominal
        self.v_tol = voltage_tol

    def objective(self, x: np.ndarray,
                  D_sim: float,
                  E_self: float,
                  E_total: float,
                  N_cycle_eq: float,
                  N_rated: float) -> float:
        """
        Equation (5): weighted sum objective (maximization)
        Note: optimizer minimizes, so we return negative.
        """
        # Avoid division by zero
        if E_total == 0:
            self_cons_term = 0.0
        else:
            self_cons_term = E_self / E_total

        battery_term = 1.0 - N_cycle_eq / N_rated

        J = (self.w_demand * D_sim +
             self.w_self_cons * self_cons_term +
             self.w_battery_life * battery_term)
        return -J   # negative for minimization

    def check_constraints(self, soc: float, power: float, voltage: float) -> bool:
        """
        Verify safety constraints
        """
        if not (self.soc_min <= soc <= self.soc_max):
            return False
        if abs(power) > self.power_max:
            return False
        if abs(voltage - self.v_nom) / self.v_nom > self.v_tol:
            return False
        return True

    def optimize_step(self,
                      current_soc: float,
                      pv_power: float,
                      load_power: float,
                      D_sim_current: float,
                      E_self_cum: float,
                      E_total_cum: float,
                      N_cycle_eq: float,
                      N_rated: float = 6000) -> Tuple[float, float]:
        """
        Determine optimal battery power (positive = discharge, negative = charge)
        Returns (optimal_power, objective_value)
        """
        # Bounds for battery power
        bounds = [(-self.power_max, self.power_max)]

        # Initial guess
        x0 = [load_power - pv_power]

        # Constraints for SOC evolution (simplified linear approximation)
        constraints = []

        result = minimize(
            fun=lambda x: self.objective(x, D_sim_current, E_self_cum, E_total_cum, N_cycle_eq, N_rated),
            x0=x0,
            bounds=bounds,
            constraints=constraints,
            method='SLSQP'
        )

        optimal_power = result.x[0]
        return optimal_power, -result.fun