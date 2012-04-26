'''
Created on Jan 14, 2012

@author: matt
'''

from time import time
from  Dictionary import Dictionary


testDic = Dictionary("../words")
testDic.VERBOSE = True
testlistDic = testDic._dictonary

start = time()
levns =  testDic._levenshtein("test")
#for levn in levns:
#    print levn
end = time()
print 'found ' + str(len(levns)) + ' leviathens in ' + str(end - start) + "for the word 'test'"

start = time()
friends = testDic.friends('test')
#for friend in friends: 
#    print friend
end = time()
print 'found ' + str(len(friends)) + ' friends in ' + str(end-start) + "for the word 'test'" 

start = time()
network = testDic.network('test')
end = time()

print 'found ' + str(len(network)) + ' in the network in ' + str(end-start) + "for the word 'test'"

print 'Finished'




