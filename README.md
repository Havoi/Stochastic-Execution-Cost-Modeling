# Stochastic Execution Cost Modeling

## Overview
This project implements a stochastic execution framework to model and optimize the liquidation of a large asset position under market impact and price uncertainty.

The framework models the mid-price as an Ito diffusion and decomposes execution costs into **market impact** and **timing risk**. Using continuous-time control theory, we derive optimal liquidation schedules and utilize Monte Carlo simulations to estimate the execution cost–risk frontier across various risk aversion regimes.

## Problem Statement
Executing large orders in financial markets introduces a fundamental tradeoff:
* **Trading too quickly** increases market impact costs.
* **Trading too slowly** exposes the trader to adverse price movements (timing risk).

This project studies this tradeoff by modeling execution as a stochastic control problem to quantify the resulting cost–risk frontier.

## Mathematical Model

### 1. Price Dynamics
The asset mid-price $S_t$ follows an arithmetic Brownian motion (Ito process):

$$dS_t = \sigma dW_t$$

Where:
* $\sigma$: Volatility
* $W_t$: Standard Brownian motion
* *Note: Drift is ignored due to the short execution horizons typically involved in optimal execution.*

### 2. Execution Cost
Total execution cost is decomposed into three components:
* **Slippage cost:** Arising from executing trades at stochastic prices.
* **Temporary market impact:** Modeled as quadratic in the trading rate.
* **Permanent market impact:** Accumulating with inventory changes.

### 3. Optimal Liquidation Strategy
The liquidation problem is formulated as a continuous-time stochastic control problem balancing expected execution cost and variance. The optimal inventory trajectory admits a closed-form solution:

$$x(t) = X_0 \frac{\sinh(\kappa(T - t))}{\sinh(\kappa T)}$$

Where:
* $x(t)$: Inventory at time $t$
* $X_0$: Initial inventory
* $T$: Trading horizon
* $\kappa$: A parameter dependent on risk aversion, volatility, and liquidity parameters.

**Insight:** Higher risk aversion leads to larger $\kappa$, resulting in faster liquidation to minimize exposure to volatility (timing risk).

## Simulation Methodology
We employ Monte Carlo simulation to validate the theoretical model:
1.  **Generation:** Generate stochastic price paths using geometric or arithmetic Brownian motion.
2.  **Execution:** Apply the optimal trading schedule derived from the control problem.
3.  **Estimation:** Calculate the expected execution cost and the standard deviation (risk) of the cost.

* **Scale:** Each risk aversion parameter is evaluated using **500+ simulated execution paths** over **100 time steps**.

## Results
The simulation produces an empirical **Execution Cost–Risk Frontier** exhibiting a convex tradeoff:
* **High Risk Aversion:** Reduces execution risk (variance) but increases expected transaction costs (due to rapid trading impact).
* **Low Risk Aversion:** Lowers impact costs but exposes the portfolio to higher timing risk.

*Note: Minor non-monotonicity in the frontier may arise from finite Monte Carlo sampling noise, which can be smoothed with increased simulation runs.*

## Project Structure

```text
.
├── project.py        # End-to-end execution modeling and simulation script
├── README.md         # Project documentation
```
## Key Parameters

| Parameter | Value | Description |
| :--- | :--- | :--- |
| **Trading Horizon** | 1.0 | Normalized time period for execution |
| **Time Steps** | 100 | Granularity of the simulation |
| **Monte Carlo Runs** | 500 | Number of paths per risk regime |
| **Risk Regimes** | 15 | Number of distinct risk aversion levels tested |
| **Impact Model** | Quad/Lin | Quadratic temporary + Linear permanent impact |

## Skills Demonstrated
* **Stochastic Processes:** Ito calculus and Brownian motion modeling.
* **Optimal Control:** Continuous-time optimization and closed-form derivations.
* **Market Microstructure:** Modeling of liquidity, slippage, and impact.
* **Numerical Methods:** Monte Carlo simulation and variance estimation.
* **Python:** Scientific computing and data visualization.

## Extensions
Future improvements and extensions to this framework include:
* Comparison against **TWAP** and **VWAP** benchmarks.
* Inclusion of price drift (Alpha) or stochastic volatility.
* Discrete-time **LQR (Linear-Quadratic Regulator)** formulation.
* Calibration of transaction cost parameters using empirical market data.
