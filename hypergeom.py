
from scipy.stats import hypergeom
import matplotlib.pyplot as plt
import numpy as np

"""
The problem is: we want to know how likely we are to catch an employee
turning up to work drunk depending on the number of tests during the year.
The number of working days is assumed to be 260 and that an employee
will turn up drunk 12 times

See code on Scipy for full documentation:
https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.hypergeom.html

"""
# Set up problem variables
No_of_Working_days = 260
No_of_potential_times_drunk = 12

No_of_tests = {'Daily':260,'Every other day':130, 'Weekly':52,'Monthly':12,
                 'Twice Yearly':2, 'Annual':1}

for testtype, tests in No_of_tests.items():
    
    
    # This is the number of arrivals - this will provide a value for 0 in
    # CDF/PMF calcs
    x = np.arange(0, No_of_potential_times_drunk+1)
    
    # Cummulative Density function - shows chances of getting away if 
    # the rules change e.g. if we are caught once we might just get a 
    # warning.
    cdf_drunk = hypergeom.cdf(x, No_of_Working_days, 
                              No_of_potential_times_drunk, tests)
    
    # Probability Mass function - the probability of turning up
    # a certain number of times drunk when the company is testing
    pmf_drunk = hypergeom.pmf(x, No_of_Working_days, 
                              No_of_potential_times_drunk, tests)
    
    # This is the inverse of the cdf as a percentile but gives slightly different results
    ppf_drunk = hypergeom.pmf(x, No_of_Working_days, 
                              No_of_potential_times_drunk, tests)
    
    # Set up the annotation to display on the graph
    # graph_text = 'Prob of being Caught = ' + str(ppf_drunk[0] * 100) + '%' 
    graph_text = 'Prob of being caught = ' + str(round((1 - cdf_drunk[0]),4) * 100) + '%'
    
    
    # Print the figure
    fig = plt.figure(figsize=(8,8))   
    fig.suptitle(testtype + ' test Frequency', fontsize=16)
    
    ax = plt.subplot(211)
    plt.annotate(graph_text, xy=(0 + 0.2, cdf_drunk[0] + 0.01), xytext=(2, 0.4),
                arrowprops=dict(facecolor='red', shrink=0.01),)
    
    ax.plot(x, cdf_drunk, marker = '.', mfc = 'red')
    ax.set_ylabel('Hypergeometric CDF and PMF')
    ax.set_xlabel('No of drunk of Arrivals')
    ax.plot(x, pmf_drunk, 'bo')
    ax.vlines(x, 0, pmf_drunk, lw=1)
    
    plt.show()
