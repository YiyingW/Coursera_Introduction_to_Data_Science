import MapReduce
import sys

"""
dna trimming Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    
    dna = record[1]
    key=''
    for i in range(0,len(dna)-10):
      key+=dna[i]
    mr.emit_intermediate(key,1)

def reducer(key, list_of_values):

    mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
