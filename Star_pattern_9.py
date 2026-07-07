#Code
n = int(input())

for i in range(n,n*-1,-1):
    if i > 0:
        print(" "*i*2,"* "*(n-i))
    else:
        print(" "*-i*2,"* "*(n+i))

#Output
"""
5
           
         * 
       * * 
     * * * 
   * * * * 
 * * * * * 
   * * * * 
     * * * 
       * * 
         * 
"""
