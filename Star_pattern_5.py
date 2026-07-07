#Code
n = int(input())

for i in range(n,0,-1):
    print(" "*2*(n-i),"* "*i)

#Output
"""
5


 * * * * * 
   * * * * 
     * * * 
       * * 
         * 
"""