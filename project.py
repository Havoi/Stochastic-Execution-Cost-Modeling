import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. Global Parameters
# =========================
T = 1.0                  # Trading horizon
N = 100                  # Time steps
dt = T / N

S0 = 100.0               # Initial mid-price
sigma = 0.02             # Volatility

X0 = 1000                # Initial inventory

eta = 0.1                # Temporary impact coefficient
gamma = 0.01             # Permanent impact coefficient

np.random.seed(42)

# =========================
# 2. Ito Price Process
# =========================
def simulate_price_path():
    dW = np.sqrt(dt) * np.random.randn(N)
    S = S0 + np.cumsum(sigma * dW)
    return np.insert(S, 0, S0)  # length N+1

# =========================
# 3. Execution Cost Model
# =========================
def execution_cost(trades, prices):
    slippage = np.sum(trades * prices[:-1])
    temp_impact = eta * np.sum(trades**2) * dt
    perm_impact = gamma * np.sum(np.cumsum(trades)) * dt
    return slippage + temp_impact + perm_impact

# =========================
# 4. Optimal Liquidation Schedule
# =========================
def optimal_schedule(X0, lam):
    kappa = np.sqrt(lam * sigma**2 / eta)
    t = np.linspace(0, T, N + 1)  # N+1 inventory points

    inventory = X0 * np.sinh(kappa * (T - t)) / np.sinh(kappa * T)
    trades = -np.diff(inventory)  # length N

    return trades

# =========================
# 5. Monte Carlo Simulation
# =========================
def simulate_execution(lam, runs=500):
    costs = []
    for _ in range(runs):
        prices = simulate_price_path()
        trades = optimal_schedule(X0, lam)
        cost = execution_cost(trades, prices)
        costs.append(cost)
    return np.mean(costs), np.std(costs)

# =========================
# 6. Cost–Risk Frontier
# =========================
lambdas = np.linspace(1e-4, 1e-1, 15)

mean_costs = []
risk = []

for lam in lambdas:
    mean_c, std_c = simulate_execution(lam)
    mean_costs.append(mean_c)
    risk.append(std_c)

# =========================
# 7. Visualization
# =========================
plt.figure()
plt.plot(risk, mean_costs, marker='o')
plt.xlabel("Execution Risk (Std Dev)")
plt.ylabel("Expected Execution Cost")
plt.title("Execution Cost–Risk Frontier")
plt.grid(True)
plt.show()
