from PyVMF import *

v = load_vmf("test.vmf")

v.visgroups.new_visgroup("abcd")

for solid in v.get_solids():
    solid.move(0, 0, 64)
    v.add_to_visgroup("abcd", solid)
        
v.export("test2.vmf")