# -*- coding: utf-8 -*-


def powercurve_linear(u, cut_in, cut_out, u_rated, power_rated):
    """This dunction calculates power for a power curve based on a linear interpolation function.
    
    Define a simple power curve using linear interpolation.

    Wind turbine power curve shape :
    1) 0 below cut_in speed
    2) g(u)*P_rated for wind speeds greater than equal to cut_in and less than u_rated
    3) g(u) = [(u-cut_in)/(u_rated-cut_in)]
    4) P_rated for wind speeds greater than equal to u_rated and less than cut_out
    4) 0 above cut_out
   
    Parameters
    ----------
    u         : wind speed at hub height m/s
    cut_in    : cut-in wind speed [m/s] that denotes the minimal wind speed the turbine starts to generate power
    cut_out   : cut-out wind speed [m/s] that denotes the wind speed the turbines stops generating power
    u_rated   : rated wind speed [m/s] that denotes the wind speed the turbine reaches the rated power
    P_rated   : rated power [MW] of the turbine
    
    

    Returns
    -------
            Power value in MW at wind speed provided in u
    """
    
    if u < cut_in:
        Power = 0.0
        
    elif u >= cut_in and u < u_rated:
        Power = power_rated*(u-cut_in)/(u_rated - cut_in)
        
    elif u >= u_rated and u < cut_out:
        Power = power_rated
        
    elif u >= cut_out:
        Power = 0.0               
    return Power

def powercurve_cubic(u, cut_in, cut_out, u_rated, power_rated):
    """This function calculates power for a power curve based on a cubic interpolation function.
    
    Define a simple power curve using cubic interpolation.


    Wind turbine power curve shape :
    1) 0 below cut_in speed
    2) g(u)*P_rated for wind speeds greater than equal to cut_in and less than u_rated
    3) g(u) = (u/u_rated)^3   cubic interpolation
    4) P_rated for wind speeds greater than equal to u_rated and less than cut_out
    4) 0 above cut_out
   
    Parameters
    ----------
    u         : wind speed at hub height m/s
    cut_in    : cut-in wind speed [m/s] that denotes the minimal wind speed the turbine starts to generate power
    cut_out   : cut-out wind speed [m/s] that denotes the wind speed the turbines stops generating power
    u_rated   : rated wind speed [m/s] that denotes the wind speed the turbine reaches the rated power
    P_rated   : rated power [MW] of the turbine
    
    

    Returns
    -------
            Power value in MW at wind speed provided in u
    """
    
    if u < cut_in:
        Power = 0.0
        
    elif u >= cut_in and u < u_rated:
        Power = power_rated*(u/u_rated)**3
        
    elif u >= u_rated and u < cut_out:
        Power = power_rated
        
    elif u >= cut_out:
        Power = 0.0               
    return Power
    

