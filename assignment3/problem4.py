import MapReduce
import sys

"""
friend symmetric problem in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):   
    for i in range(2):
    	key=(record[i], record[1-i])
    	value=(record[1-i],record[i])
    	mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    if len(list_of_values)==1:
    	mr.emit([key[0],key[1]])


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
