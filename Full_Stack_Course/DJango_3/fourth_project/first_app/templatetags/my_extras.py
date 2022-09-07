from django import template

# We store this file as a library
register = template.Library()

# @register.filter(name="cutting")
def cut_x(value, x):

    """
    This function cuts out all x substrings from the string.
    """

    return value.replace(x,"")

# Now we define the name of the filter as a template_tag (the second argument is the function whose template tag name we will assign).
# This could also be done by adding the decorator commented above the definition of the cut_x function (notice that cut_x is passed as a function itself,
# as we saw it is usually done for decorators in the Python_others part).
register.filter("cutting", cut_x)