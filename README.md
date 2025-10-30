# Multilayer Perceptron for Financial Time Series Forecasting

A neural network implementation for forecasting monthly financial time series from the M3 Competition dataset.

## Overview

This project implements a custom multilayer perceptron (MLP) with:
- **Polynomial detrending** to remove long-term trends
- **Seasonal differencing** to handle monthly seasonality
- **Global standardization** across training series
- **Multi-step forecasting** for 18-month horizons

## Dataset

- **Source**: M3 Competition Monthly Financial Series
- **Training**: 100 series
- **Testing**: 45 completely unseen series
- **Forecast horizon**: 18 months

## Model Architecture

- **Input layer**: 12 features (lookback window)
- **Hidden layer**: Configurable size with tanh activation
- **Output layer**: 1 neuron (linear activation)
- **Regularization**: L2 weight penalty
- **Optimization**: Gradient descent with early stopping

## Methodology

### Data Preprocessing
1. Split dataset into 100 training and 45 test series
2. For each series, hold out last 18 months as forecast target
3. Apply polynomial detrending (degree 2) using only training period
4. Apply seasonal differencing (12-month lag)
5. Fit global scaler on all training data
6. Create 12-step sequences for model training

### Model Training
1. **Hyperparameter tuning**: 80/20 split of training sequences for grid search
2. **Grid search**: Hidden size [2, 3, 5], Learning rate [1e-4, 5e-4, 1e-3], L2 lambda [0.0, 1e-3, 1e-2]
3. **Final training**: Retrain on all training sequences with best hyperparameters
4. **Early stopping**: Patience-based with best weight restoration

### Evaluation
The model forecasts 18 months ahead for 45 completely unseen test series. Performance metrics include:
- **MSE** (Mean Squared Error)
- **MAPE** (Mean Absolute Percentage Error)
- Both mean and median MAPE reported across test series

## Files

- `processing.ipynb`: Main implementation (data processing, model training, evaluation)
- `plots_timeseries.ipynb`: Visualization of raw time series data
- `M3C.xls`: M3 Competition dataset

## Requirements

```
pandas
numpy
matplotlib
scikit-learn
tqdm
openpyxl
```

## Results

The model generates 18-month forecasts for each test series, with performance visualized through:
- Individual forecast plots for all test series
- MAPE distribution histogram
- Statistical summaries (mean, median, std dev, percentiles)
- Best/worst performing series identification