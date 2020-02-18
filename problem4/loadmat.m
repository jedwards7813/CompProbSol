% Starting point for Problem 4
load('smallperiodictable')
readtable('smallperiodictable')
d1=find(density>1);%atomic numbers of elements w/ density>1
d2=names(x)%names of elements w/ density>1
num=numel(x)%# of elements w/ density>1
