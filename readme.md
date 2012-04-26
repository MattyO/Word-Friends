WordFriends
===========
So I came across this problem as a code challenge for the company Causes(www.causes.com).  I never ended up applying, so the problem sat on my desk for about 6 months.  When I finally got around to completing it, this problem proved to be a great place to test new technologies and ideas dealing with large maps of data.  I tried redis, celery, and concurrent processing methods.

Concept
-------
Given a dictionary of words, each word has a list of friends.  The set of level 1 levenshtein for a given word which are also words themselves are friends.  A level 1 levenshtein is the word in question, which has 1 letter changed, inserted, or deleted from it.   The social network of a word is that words friends, those word's friends, and so on until the network of friends is exhausted.
What is the network size of any particular word? 

Files
-----
Everything is pretty self explanatory.   The dictionary houses all of the functionality, EntryPoint will print out a quick go around of what to expect, and test.py houses test cases.  

TODO
----
I tried various multi-threading and concurrency solutions, pickling in the Dictionary object was a problem.  The overhead for Redis and Celery increased run time substantially.  More works needs to be done in this area.  The get friends call in network should become a map function later on.
Note: celery is best for large tasks.  I found overhead for tasks was close to .5 seconds, most likely due to messaging being routed and handled through the networking layer.  redis is fast, but had trouble keeping up with adding the large number of sets that made up a words friends.

I'm curious how many networks are in the unix dictionary.  I would guess that there are many 1 word networks mostly due to 's words in the dictionary.  
It would also be interesting to know the word with the most close friends.  
There is also an opportunity to implement Dijkstra’s algorithm for analysis of how close words are related  to other words.  .  

Outside resources
More about Levenshtein distance: http://en.wikipedia.org/wiki/Levenshtein_distance