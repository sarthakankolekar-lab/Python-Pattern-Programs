#Code
n = int(input())

for i in range(n,-n,-1):
    if i > 0:
        print(" "*i,"* "*(n-i))
    else:
        print(" "*-i,"* "*(n+i))

#Output
"""
6
       
      * 
     * * 
    * * * 
   * * * * 
  * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      * 
"""