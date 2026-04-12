"""
Human-Centered Design Metrics Calculator
Implements Equations (1)-(4) from Scientific Reports submission
"""

import numpy as np
from typing import List, Tuple

def compute_C_target(S: float, K: float, T: float,
                     S_max: float = 12.0,
                     K_max: float = 100.0,
                     T_max: float = 100.0,
                     w_S: float = 0.4,
                     w_K: float = 0.3,
                     w_T: float = 0.3) -> float:
    """
    Equation (1): Cognitive Suitability Index

    Parameters
    ----------
    S : float
        Average operation steps (target ≤3)
    K : float
        NASA-TLX cognitive load (target 40)
    T : float
        Automatic misoperation correction rate (%)
    """
    term_S = 1 - (S - 1) / (S_max - 1)
    term_K = 1 - K / K_max
    term_T = T / T_max
    return w_S * term_S + w_K * term_K + w_T * term_T


def compute_D_sim(P_actual: np.ndarray,
                  P_expected: np.ndarray,
                  alpha: np.ndarray) -> float:
    """
    Equation (2): Demand Matching Index

    Parameters
    ----------
    P_actual : array_like
        Actual power supply at each timestep (kW)
    P_expected : array_like
        Expected power supply at each timestep (kW)
    alpha : array_like
        Priority weight per timestep (1.5 / 1.0 / 0.5)
    """
    numerator = np.sum(np.minimum(P_actual, P_expected) * alpha)
    denominator = np.sum(P_expected * alpha)
    if denominator == 0:
        return 0.0
    return numerator / denominator


def compute_P_target(E: float, tau_actual: float, R: float,
                     tau_std: float = 2.0,
                     w_E: float = 0.4,
                     w_tau: float = 0.3,
                     w_R: float = 0.3) -> float:
    """
    Equation (3): Subject Participation Index (design target)

    Parameters
    ----------
    E : float
        User-defined strategy execution success rate (%)
    tau_actual : float
        Actual response time (s)
    R : float
        Demand response participation rate (%)
    """
    term_E = E / 100.0
    term_tau = tau_std / tau_actual if tau_actual > 0 else 1.0
    term_R = R / 100.0
    return w_E * term_E + w_tau * term_tau + w_R * term_R


def compute_H_sim(D_sim: float, C_target: float, P_target: float,
                  w_D: float = 0.45,
                  w_C: float = 0.30,
                  w_P: float = 0.25) -> float:
    """
    Equation (4): Composite Human-Centered Score
    """
    return w_D * D_sim + w_C * C_target + w_P * P_target


def get_alpha_from_season_and_load_type(season: str, load_type: str) -> float:
    """
    Map season and load type to priority weight α_i
    """
    if season == 'busy' and load_type == 'productive':
        return 1.5
    elif season == 'slack' and load_type == 'flexible':
        return 0.5
    else:
        return 1.0