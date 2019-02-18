#ask for a nme
a = input('Whats your name? ')

#add a .txt to that answer
f = open(a + '.txt','w')

#close the file you make
f.close()