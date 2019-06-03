def F_corr_coef_regr(var_x,var_y,p_crf,p_rgr):
    """Computes the correlations coefficient(p_crf=1 & p_rgr=0) and 
    regression slope(p_crf=0 & p_rgr=1) for 1D dataset for the time series anomaly
    
    e.g. corr_coeff_temp = F_orr_coef_regr(temp,1,0)
        regr_slope_temp = F_orr_coef_regr(temp,0,1)
    """
  
    ####Detrending
            
    # for var_x
    xi = np.arange(np.size(var_x))
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,var_x)
    line_var_x = slope*xi+intercept
    var_x_td = var_x - line_var_x
            
    ### for var_y
    slope, intercept, r_value, p_value, std_err = stats.linregress(xi,var_y)
    line_var_y = slope*xi+intercept
    var_x_td = var_y - line_var_y
       
    ### computes corelation and regression
    X = var_x_td
    Y = var_t_td
    (r, p) = stats.pearsonr(X, Y)
    slope, intercept, r_value, p_value, slope_std_error = stats.linregress(X,Y)
                                                                

    return r_value*p_crf + slope*p_rgr
