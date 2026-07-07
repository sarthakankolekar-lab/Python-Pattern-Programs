#Code
n = int(input())

for i in range(-n,n+1):
    if i > 0:
        print(" "*(n-i),"* "*i)
    elif i == 0:
        continue
    else:
        print(" "*(n+i),"* "*-i)

#Output
"""
5

 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
"""