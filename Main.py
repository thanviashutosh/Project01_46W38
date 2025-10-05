# -*- coding: utf-8 -*-


def powercurve(u, inter_method = "Linear", cut_in=3, cut_out=25, u_rated=11, power_rated=15):
    """This function calculates power based on a power curve defined using u(wind speed), 
       interpolation method (inter_method), cut_in wind speed, cut_out wind speed, rated wind speed(u_rated)
       rated power (power_rated).
    
    Define a simple power curve using linear interpolation.

    Wind turbine power curve shape :
        
    1) 0 below cut_in speed
    2) inter_method*P_rated for wind speeds greater than equal to cut_in and less than u_rated, where inter_method
       can only take "Linear" or "Cubic" values
    3) For "Linear" interpolation method, inter_method = (u-cut_in)/(u_rated-cut_in)
    4) For "Cubic" interploation method,  inter_method = (u/u_rated)**3
    4) power_rated for wind speeds greater than equal to u_rated and less than cut_out
    4) 0 above cut_out
   
    Parameters
    ----------
    u         : wind speed at hub height m/s
    cut_in    : cut-in wind speed m/s (default is [3 m/s])  that denotes the minimal wind speed the turbine starts to generate power
    cut_out   : cut-out wind speed m/s (default is [25 m/s]) that denotes the wind speed the turbines stops generating power
    u_rated   : rated wind speed m/s (default is [11 m/s]) that denotes the wind speed the turbine reaches the rated power
    P_rated   : rated power MW, (default is [15 MW]) of the turbine
    inter_method : interpolation method (default is "Linear") , can be be "Linear" or "Cubic"
    

    Returns
    -------
            Power value in MW 
    """

    
   ## defining the power curve 
    if u < cut_in:            ## if the wind speed less than cut in then Power = 0
        Power = 0.0
        
    elif u >= cut_in and u < u_rated:  # if the wind speed greater than equal to cut in and less then rated wind speed
                                       # then interpolation method is used to calculate Power
        
        if inter_method == "Linear":
            Power = power_rated*(u-cut_in)/(u_rated - cut_in) # expression of linear interpolation method
        
            if inter_method == "Cubic":
                Power = power_rated*(u/u_rated)**3            # expression for cubic interpolation method
        
    elif u >= u_rated and u < cut_out:                        # if the wind speed is greater than equal to rated wind 
                                                              # wind speed then Power is equal to rated Power
        Power = power_rated
        
    elif u >= cut_out:
        Power = 0.0                                           # if the wind speed is greater than equal to cutout 
                                                              # then Power is 0.0
    return Power

# One example
if __name__ == '__main__': # runs only when executed as a script
    u_1 = 11
    p = powercurve(u_1)
    print(f'One Example - The power for wind speed of {u_1:.2f} m/s is {p:.2f}')



## asking user for the inputs for calculating the power

u = float(input("Enter wind speed in m/s : "))                # enter wind speed in m/s

inter_method = input("Select interpolation method from Linear or Cubic : ")          # input interpolation method

if inter_method != "Linear" and inter_method != "Cubic":                            #raise error incorrect input
   raise ValueError("Interploation method can only be Linear or Cubic, the default is Linear")

cut_in = float(input("Enter cut in wind speed in m/s : "))   # cut in wind speed in m/s

cut_out = float(input("Enter cut out wind speed in m/s : ")) # cut out wind speed in m/s

u_rated = float(input("Enter rated wind speed in m/s : "))   # rated wind speed in m/s

power_rated = int(input("Enter rated Power of the turbine in MW : ")) # rated power of the turbine

power_turbine = powercurve(u, inter_method, cut_in, cut_out, u_rated, power_rated)

print(f' The wind turbine power calculated for a turbine with rated Power of {power_rated:.2f}MW, cut in speed\
      of {cut_in:.2f} m/s , cut out speed of {cut_out:.2f} m/s, rated speed of {u_rated:.2f} m/s and using\
          {inter_method}interpolation method is {power_turbine:.2f} MW')



       
