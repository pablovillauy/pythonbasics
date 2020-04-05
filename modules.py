# own modules
# third party modules
# python modules

# import module
import datetime

# https://docs.python.org/3/tutorial/modules.html
# https://docs.python.org/3/py-modindex.html

print(datetime.date.today())
print(datetime.timedelta(minutes=70))


from datetime import timedelta
print(timedelta(minutes=70))

from datetime import date as dt
print(dt.today())


import fmath

fmath.add(1,2)
fmath.substract(2,3)

# flask: framework for web apps
# django: framework
# tkinter
