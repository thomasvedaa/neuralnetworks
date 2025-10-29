# M3 Financial Forecasting with Neural Networks

A semester project exploring time series prediction using a custom multilayer perceptron built from scratch.

---

## What I Built

This project forecasts **18 months ahead** for financial time series from the M3 Competition dataset. Instead of using off-the-shelf libraries, we implemented a custom neural network to understand the fundamentals of backpropagation and gradient descent.

### The Pipeline

**Data Preparation:**
- Loaded 50 monthly financial series from the M3C dataset
- Removed trends using 2nd-degree polynomial regression
- Applied 12-month seasonal differencing to handle seasonality
- Normalized everything using global scaling across all series

**The Neural Network:**
- Built a simple MLP from scratch (no TensorFlow/PyTorch)
- Used `tanh` activation for the hidden layer
- Implemented backpropagation with L2 regularization
- Added early stopping to prevent overfitting

**Training Strategy:**
- Combined sequences from all 50 series for training
- Grid search over hidden size, learning rate, and regularization
- Trained final model on best hyperparameters
- Forecasted iteratively: each prediction feeds into the next

**Results:**
- Generated 18-month forecasts for each series
- Reversed all transformations to get predictions in original scale
- Evaluated using MSE and MAPE metrics
- Visualized prediction quality across all series

---

## Key Files

- `processing.ipynb` - Main pipeline: preprocessing → training → forecasting → evaluation
- `plots_timeseries.ipynb` - Visualization of the raw time series
- `M3C.xls` - M3 Competition dataset (monthly financial data)

---


## Running the Project

Just open `processing.ipynb` and run all cells. The notebook is self-contained and walks through the entire process with progress bars and detailed output.

**Requirements:**
```
numpy, pandas, matplotlib, scikit-learn, tqdm
```

---

Built with curiosity and a lot of caffeine.