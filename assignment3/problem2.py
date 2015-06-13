import MapReduce
import sys

"""
order_id = order_id problem in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    
    # value: document contents
    key = record[1]
    
    mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    total=list_of_values[0]
    for i in range(1,len(list_of_values)):
      mr.emit(total+list_of_values[i])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
