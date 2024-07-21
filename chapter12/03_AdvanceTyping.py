# typing module
from typing import List,Tuple,Dict,Union

# list of integers--
number:List[int]=[1,2,3,4,5]

#tuples of strings and Integers--
Employee:Tuple[str,int]=('rajdip',10000)

#dictionary with string keys and integers values--
score:Dict[str,int]={'virat':100,
                     'rohit':88,
                     'Boom Boom':3}


#union type for veriable that can hold multiple types---
identifier:Union[int,str]='id123'
identifier=12345#also valid..
identifier='adbdf'#also valid..