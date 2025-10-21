# M3 Forecasting – Neural Network Semester Project

This project was developed as part of the **Neural Networks** course.  
It implements a complete time series forecasting pipeline for monthly financial data from the **M3 Competition dataset**, focusing on preprocessing, neural network training, and evaluation.

---

## Project Overview

The goal of this project is to forecast future values of financial time series using a **fully connected neural network (MLP)** trained on preprocessed data.  
We focus on removing deterministic trends and seasonality before modeling, following a clean, reproducible ML pipeline.

**Main steps:**
1. Load monthly financial time series from `M3Forecast.xls`
2. Apply **polynomial detrending** (2nd-degree)
3. Apply **12-month seasonal differencing**
4. Normalize the residuals using a `StandardScaler`.
5. Train a custom **MLP** using gradient descent.
6. Evaluate the model using a **12-month forecast horizon**
7. Visualize results and reconstruct forecasts to original scale
