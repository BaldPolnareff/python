import array
import numpy
import scipy 
import math
import matplotlib

# Debunking flat-earthers claiming that "if the Earth was a globe then the drop to the horizon would be
# 8 inches per mile squared"

# trying to reverse engineer this claim, the equation for the vertical drop is r*(1 - cos(d/r)), where r is the
# Earth radius and d is the distance (on a spherical surface) to get from points A to B, comprised by an angle theta

# their equation would instead be something like 8 * d²

# The claim is debunked by many considerations including the fact that an observer on the earth is not 
# looking at the horizon tangentially to the earth surface, but rather from the height of its eyes, not to 
# mention all the issues involving diffraction, lensing and any optical phenomena involving the presence of the 
# atmosphere, which makes it impossible to directly correlate a purely geometrical vertical drop rate with 
# what the eyes of a human observer actually see

# Let's pretend all these issues don't exist, seeing the problem from a purely mathematical perspective

# On a very local distance, the approximation is actually fairly decently accurate (it's a parabola, whereas the real 
# result is a trigonometric cosine like function that periodically repeats as you cycle through the earth surface)


miles_to_inches = 63360
earth_radius = 3958.8 # mi
domain = numpy.array([inf, sup])
resolution = 1000



def flat_claim(radius, d_span, resolution):
    d_space = numpy.linspace(d_span[0], d_span[1], resolution)
    vdrop_space = 8 * (d_space ** 2)
    
        


def actual_drop(radius, d_span, resolution):
    d_space = numpy.polynomial.chebyshev.Chebyshev.linspace(d_span[0], d_span[1], resolution)
    vdrop_space = miles_to_inches * radius * (1 - numpy.cos(d_space / radius)) # numpy automatically knows that 1 in this case should be an array of ones of the appropriate length, nice
