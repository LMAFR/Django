# import mymodule
from mymodule import *

# mymodule.func_in_module()
func_in_module()

# Notice the __pycache__ folder which is created when we import the module. It will contain the C version of the imported functions.
# import * (all) is not recommended as it could waste a lot of memory in importing everything which is inside the imported module.