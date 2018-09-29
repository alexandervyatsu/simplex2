Problem
 NEXAMPLE
Minimize
 OBJ:   COL01 + 2 COL02 +  COL03
Subject To
 ROW01:   COL01 +  COL02 >= 2 	\ RANGE (2, 4)
     COL01 +  COL02 <= 4
 ROW02:  -  COL02 +  COL03 = 0
 ROW03:  -  COL01 -  COL03 = -3
Bounds
 COL01 <= 1
End
