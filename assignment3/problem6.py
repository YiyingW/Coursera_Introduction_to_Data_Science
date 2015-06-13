import MapReduce
import sys

"""
matrix multiplication in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0]=="a":
      for k in range(5):
        mr.emit_intermediate((record[1],k), (record[2], record[3]))
    else:
      for i in range(5):
        mr.emit_intermediate((i, record[2]), (record[1],record[3]))

def reducer(key, list_of_values):
    value=0
    
    for i in range(5):
      count=0
      ind_sum=1
      for item in list_of_values:
        
        if item[0]==i:
          count+=1
          ind_sum*=item[1]
      if count==2:
          value+=ind_sum



    
  
    mr.emit((key[0], key[1], value))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
