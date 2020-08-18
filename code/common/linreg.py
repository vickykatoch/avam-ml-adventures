
def fit_uni_variate(x,y):
    # CALC MEAN OF X & Y
    x_mean=x.mean()
    y_mean = y.mean()

    # CALC STANDARD DEVIATION OF X & Y
    x_sd = x.std()
    y_sd = y.std()

    # CALC Z-SCORE OF X & Y
    x_zs = (x_mean - x)/x_sd
    y_zs = (y_mean - y)/y_sd

    # CALC CO-RELATION COFFICIENTS FOR X & Y
    cor_coff = (x_zs * y_zs).sum() / len(x)

    # CALC SLOPE
    # slope (m) = cor_coff * y_sd/x_sd
    slope_m = cor_coff * y_sd/x_sd

    # CALC INTERCEPT
    #intercept (b) = y_mean - slope * x_mean
    intercept_b = y_mean - slope_m * x_mean 
    return {
        'slope' : slope_m,
        'intercept': intercept_b
    }
