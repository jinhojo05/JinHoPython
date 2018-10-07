import os
import sys
file = [ "fire.txt", "wheel.txt", "lever.txt", "agriculture.txt", "earthware.txt"]
for fi in file:
    f = open( fi, 'r')
    st = 0;
    st1 = 0;
    Word = 0;
    while True:
        line = f.readline()
        if not line:
            break
        st += line.count(' ');
        st1 += len(line);
        if line != '\n':
            Word += len( line.split( " " ) );
    St = st1 - st
    print(fi)
    print ('- total characters : ',St)
    print ('- total words : ',Word)
    K = St / Word
    print('- average characters per words : ', ("%.3f"% round(K, 3)))
    f.close()
####################################################
f = open("civilization.txt", "a")
for i in file:
    G = open( i, 'r')
    a = G.read()
    f.write(a)
f.close()