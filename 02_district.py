from pprint import pprint

from district.central_street.house1 import room1 as c1
from district.central_street.house1 import room2 as c2
from district.central_street.house2 import room1 as c3
from district.central_street.house2 import room2 as c4
from district.soviet_street.house1 import room1 as s1
from district.soviet_street.house1 import room2 as s2
from district.soviet_street.house2 import room1 as s3
from district.soviet_street.house2 import room2 as s4

print('На районе живут > ', end='')
list_people = (','.join(c1.folks + c2.folks + c3.folks + c4.folks + s1.folks + s2.folks + s3.folks + s4.folks))
pprint(list_people)

# Зачёт!
