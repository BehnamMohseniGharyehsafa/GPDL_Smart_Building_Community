import numpy as np
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from scipy.stats import shapiro
import statsmodels.api as sm
from patsy import dmatrix

##########################################################################
### Define a function to calculate and display full evaluation metrics ###
##########################################################################

def calculate_full_metrics(y_true, y_pred, std_dev=None, model_name="Model"):
    """Calculate a comprehensive set of evaluation metrics for regression models."""
    # Initialize results dictionary
    results = {}

    # Basic metrics
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    # Advanced metrics
    y_non_zero = np.where(y_true == 0, np.finfo(float).eps, y_true)
    mape = np.mean(np.abs((y_true - y_pred) / y_non_zero)) * 100

    denominator = (np.abs(y_true) + np.abs(y_pred)) / 2
    denominator = np.where(denominator == 0, np.finfo(float).eps, denominator)
    smape = np.mean(np.abs(y_pred - y_true) / denominator) * 100

    mbe = np.mean(y_pred - y_true)
    mean_actual = np.mean(y_true)
    cv_rmse = (rmse / mean_actual) * 100

    range_actual = np.max(y_true) - np.min(y_true)
    r_rmse_range = (rmse / range_actual) * 100

    std_actual = np.std(y_true)
    r_rmse_std = (rmse / std_actual) * 100

    numerator = np.sqrt(np.mean((y_pred - y_true) ** 2))
    denominator_u = np.sqrt(np.mean(y_pred ** 2)) + np.sqrt(np.mean(y_true ** 2))
    theil_u = numerator / denominator_u

    # Prediction Interval Coverage Probability (PICP) & PINAW
    if std_dev is not None:
        confidence_interval = 1.96
        lower_bounds = y_pred - confidence_interval * std_dev
        upper_bounds = y_pred + confidence_interval * std_dev
        within_interval = np.logical_and(y_true >= lower_bounds, y_true <= upper_bounds)
        picp = np.mean(within_interval) * 100
        interval_widths = upper_bounds - lower_bounds
        pinaw = np.sum(interval_widths) / (len(y_true) * range_actual)
    else:
        picp = pinaw = np.nan

    # Negative Log Predictive Density (NLPD)
    if std_dev is not None:
        variance = std_dev ** 2
        nlpd = np.mean(((y_true - y_pred) ** 2) / (2 * variance) + 0.5 * np.log(2 * np.pi * variance))
    else:
        nlpd = np.nan

    # Shapiro-Wilk Test for Residual Normality
    residuals = y_true - y_pred
    stat, p_value = shapiro(residuals)
    shapiro_result = "Fail to reject H0" if p_value > 0.05 else "Reject H0"

    # Index of Agreement (Willmott’s d1)
    d1 = 1 - np.sum((y_pred - y_true) ** 2) / np.sum((np.abs(y_pred - np.mean(y_true)) + np.abs(y_true - np.mean(y_true))) ** 2)

    # Store results
    results = {
        "MSE": mse, "RMSE": rmse, "MAE": mae, "R²": r2,
        "MAPE": mape, "sMAPE": smape, "MBE": mbe,
        "CV(RMSE)": cv_rmse, "rRMSE (Range)": r_rmse_range, "rRMSE (Std)": r_rmse_std,
        "Theil's U": theil_u, "PICP": picp, "PINAW": pinaw, "NLPD": nlpd,
        "Shapiro-Wilk Test": (stat, p_value, shapiro_result),
        "Index of Agreement (d1)": d1
    }

    # Print metrics
    print(f"\nEvaluation Metrics for {model_name}:")
    for metric, value in results.items():
        print(f"{metric}: {value}")

    return results

