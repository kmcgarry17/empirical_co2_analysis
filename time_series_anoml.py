def F_detrend(var):
    """ computes time series anomaly (remove the trend) for 1D dataset"""

    xi = np.arange(np.size(var))
    mask = ~np.isnan(var)  ## mask nans
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,var[mask])
    line_va = slope*xi+intercept
    var_anoml = var - line_var_x
    
    return  var_anoml
