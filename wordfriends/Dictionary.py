import string
from time import time

'''
Created on Jan 14, 2012

@author: matt
'''

class Dictionary():
    '''
    classdocs
    '''
    
    INITIAL_NETWORK_ID  = -1
    VERBOSE             = False
    
    def __init__(self,filename ):
       
        numWords = 0
        self._dictonary = {}
        dicFile = open(filename, 'r')    
        for line in dicFile:
            line = line.rstrip('\n')
            self._dictonary[line] = {'network' : self.INITIAL_NETWORK_ID, 'friends':None}

                
    def _levenshtein(self, word):
        rLev = [] 
        for i in range(0, len(word)) :
            rLev.append(word[0:i] + word[i+1:]) #--COMMENT--# delete cases
            for letter in string.lowercase:
                rLev.append(word[0:i] + letter + word[i:])   #--COMMENT--# insert cases
                rLev.append(word[0:i] + letter + word[i+1:]) #--COMMENT--# switch cases  
            i += 1   
        
        #--COMMENT--# get the last set of leviathens that you couldn't above due the indexes not being able to go past number of characters + 1    
        for letter in string.lowercase: 
            rLev.append(word + letter)
            
        return rLev
    
    def _nextNetworkId(self):
        rHighestNetworkNumber =  1
        for word in self._dictonary:
            if self._dictonary[word]['network'] > rHighestNetworkNumber:
                rHighestNetworkNumber = word['network']
        return rHighestNetworkNumber
    
    def friends(self, word):
        rFriends = set()
        
        if self._dictonary[word]['friends'] is None:
            for levenshtein in self._levenshtein(word):
                if self._dictonary.has_key(levenshtein) and levenshtein != word:                
                    rFriends.add(levenshtein)
            self._dictonary[word]['friends'] = rFriends
        else: 
            rFriends = self._dictonary[word]['friends']

        return rFriends
            
    def network(self, word):
        '''
        '''
        rNetwork        = set([word])
        iAdded          = set([word])
        counter         = 0
        newNetworkId    = self._nextNetworkId()
        while len(iAdded) > 0 :
            newAdded    = set()
            start       = time()
            counter     += 1

            for wordAdded in iAdded:
                if self._dictonary[wordAdded]['network'] == self.INITIAL_NETWORK_ID:
                    self._dictonary[wordAdded]['network'] = newNetworkId
                    newAdded.update(self.friends(wordAdded))    
                    
            rNetwork.update(newAdded)
            iAdded = newAdded

            end = time()
            if self.VERBOSE:
                print "iteration " + str(counter) + " completed in " + str(end - start) + ", network size: " + str(len(rNetwork))
        
        return rNetwork
