assert 1.2 == round(1.23, 1)
assert 1.23 == round(1.23, 2)
assert 1.230 == round(1.23, 3)
assert 1.3 == round(1.27, 1)
assert -1.3 == round(-1.27, 1)

assert 1627731 == round(1627731, 0)
assert 1627730 == round(1627731, -1)
assert 1627700 == round(1627731, -2)
assert 1628000 == round(1627731, -3)
assert 1630000 == round(1627731, -4)

# assert 2.1+4.2==6.3
from utils import myutils
myutils.print_all_attrs(float)
