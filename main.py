# -*- coding: utf-8 -*-
import qsoptex
import time
filename = 'afiro.mps'
p = qsoptex.ExactProblem()
p.read(filename, filetype='MPS')
p.write('lp_' + filename[0:-4] + '.lp', filetype="LP")
string = ''
for line in open('lp_' + filename[0:-4] + '.lp'):
    string += line
print (string)
p.set_param(qsoptex.Parameter.SIMPLEX_DISPLAY, 1)
start=time.clock()
status = p.solve()
stop=time.clock()
if status == qsoptex.SolutionStatus.OPTIMAL:
    print('Решилось за')
    print (stop-start)
    print('Вектор X:')
    print(map(float, p.get_values()))
    print('Экстремум:')
    print(float(p.get_objective_value()))
else:
    print("Не решилось")
