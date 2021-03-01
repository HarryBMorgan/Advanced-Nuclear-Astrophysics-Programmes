# -----------------------------------------------------------------------------
# PHY3059
# Advanced Nuclear Astropysics
# University of surrey
# Harry Morgan

# -----------------------------------------------------------------------------
# PROGRAMME DESCRIPTION
# mean_mass.py
# This programme calculates the mean mass of a gas. It is done by altering the
# parameters X, Y and Z. Whether the gas is a plasma or not is also required.
# The X, Y and Z parameters represent the ratios of the Hydrogen, Helium and
# Metals in the gas.

# -----------------------------------------------------------------------------
# IMPORTS
from fractions import Fraction  #Used for displaying output nicely.

# -----------------------------------------------------------------------------
# FUNCTIONS
def mean_mass(X, Y, Z, plasma):
    # This function calculates the meas mass of the gas provided with the
    # parameters of X, Y, Z (which are of type float) and plasma (which is of
    # type boolean).
    
    # Check is the gas is ionised.
    if plasma == True: # The gas IS ionised.
        
        # Call __mean_molecular_mass__ function and __mean_electron_mass__
        # to calculate the total mean mass of the gas.
        mu_inverse = __mean_molecular_mass__(X, Y, Z) + \
                        __mean_electron_mass__(X)
        
    else:   # The gas is NOT ionised.
    
        # Call only the __mean_molecular_mass__ function as there is no
        # ionisatoin.
        mu_inverse = __mean_molecular_mass__(X, Y, Z)
    
    # Give these values to the user.
    return mu_inverse

def __mean_molecular_mass__(X, Y, Z):
    # This function calculates the mean molecular mass of the elements in the
    # gas.
    
    # Calculate the mean molecular mass provided the parameters.
    # Neglecting the last term in this equation for simplicity as it is very
    # small.
    mu_inverse = X + (Y / 4.0) #+ (Z * (1 / A))
    
    # Return the result.
    return mu_inverse

def __mean_electron_mass__(X):
    # This function calculates teh mean molecular mass of the free electrons.
    
    # Calculate the mean electron mass.
    # For a fully ionised plasma this equation will surfice.
    mu_e_inverse = 0.5 * (1.0 + X)
    
    # Return to user.
    return mu_e_inverse
    
# -----------------------------------------------------------------------------
# MAIN
if __name__ == "__main__":
    # Set the parameters.
    X = 0.0
    Y = 1.0
    Z = 0.0
    plasma = True
    
    # Call the function to calculate the mean mass.
    mu_inverse = mean_mass(X, Y, Z, plasma)
    mu = 1 / mu_inverse
    
    # Print the results to the user.
    print("The inverse mean mass =", '%.5f' %mu_inverse, "=", \
            Fraction(mu_inverse))
    print("Mean mass =", '%.5f' %(mu), "=", Fraction(mu))