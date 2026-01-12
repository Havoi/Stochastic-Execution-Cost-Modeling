# Stochastic Execution Cost Modeling

## Overview
This project implements a stochastic execution framework to study optimal liquidation of large asset positions
under market impact and price uncertainty. The asset mid-price is modeled as an Ito diffusion, execution costs
are decomposed into market impact and timing risk, and optimal trading schedules are derived using
continuous-time control theory. Monte Carlo simulations are used to estimate the execution cost–risk frontier
across multiple risk aversion regimes.

---

## Problem Statement
Large trade execution introduces a fundamental tradeoff between market impact and exposure to price risk.
Aggressive execution increases impact costs, while slower execution increases variance from adverse price
movements. This project models this tradeoff quantitatively and characterizes the resulting cost–risk frontier.

---

## Mathematical Model

### Price Dynamics
The mid-price \( S_t \) follows an Ito process:
\[
dS_t = \sigma dW_t
\]
where \( \sigma \) denotes volatility and \( W_t \) is standard Brownian motion. Drift is ignored due to the
short execution horizon.

### Execution Cost Decomposition
Total execution cost consists of:
- Slippage from stochastic execution prices
- Temporary market impact, quadratic in trading rate
- Permanent market impact, accumulating with inventory

---

## Optimal Liquidation Strategy
The execution problem is formulated as a continuous-time stochastic control problem that balances expected
execution cost against timing risk. The optimal inventory trajectory admits a closed-form solution:
\[
x(t) = X_0 \frac{\sinh(\kappa (T - t))}{\sinh(\kappa T)}
\]
where \( \kappa \) depends on risk aversion, volatility, and impact parameters. Increasing risk aversion
results in faster liquidation and reduced execution risk.

---

## Simulation Methodology
Monte Carlo simulation is used to evaluate execution performance:
- Stochastic price paths are generated using an Ito process
- Optimal trading schedules are executed over 100 time steps
- Expected cost and risk are estimated from 500+ simulated paths per regime

---

## Results
The simulation produces an empirical execution cost–risk frontier exhibiting a convex tradeoff:
- Higher risk aversion lowers execution risk but increases expected cost
- Lower risk aversion reduces impact cost at the expense of higher timing risk

Local non-monotonicity arises from finite Monte Carlo sampling noise and diminishes with increased simulations.

---

## Code Structure
