
import sys

sys.path.insert(0, r'c:\classroom\aug3\demo\mylib')
print(sys.path)

import string_funs as sf

print(sf.count_upper("AbcXZy"))
print(sf.has_digit("Abc3XZy"))