#Code
n = int(input())

a = n
b=-1
c=2

for i in range(-n,n,1):
    if i <= 0:
        if i >= -n+3:
            print(" "*-i,end=" ")
            print("*",end="")
            print(" "*(i+a),end="")
            print("*")
            a+=1
            b+=1
        else:
            print(" "*-i,"* "*(n+i))
    else:
        if i == n-1:
            print(" "*i,"* "*(n-i))
        else:
            print(" "*i,end=" ")
            print("*",end="")
            print(" "*(n+b-c),end="")
            print("*")
            c+=1
            b-=1

#Output
"""
9
          
         * 
        * * 
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
  *             *
   *           *
    *         *
     *       *
      *     *
       *   *
        * *
         * 
"""