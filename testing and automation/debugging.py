import pdb
import trace

"""
n next
c continue
l list
p print. (ie p a prints value of a)
q quit
"""

def buggy_function():
    a = 10
    b = 0
    pdb.set_trace()# stops here
    c = a/ b

#trace = trace.Trace(trace=True) # logs every line
# tracer.run("buggy_function()")

buggy_function()