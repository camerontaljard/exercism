def word_count(words):
  counts = dict()
  words = words.split()
  
  for word in words:
    if word not in counts:
      counts[word] = 1
    else:
      counts[word] += 1 
  
  return counts
      
      

#import collections
#import string

#def word_count(text):
  #processed_text = text.translate(None, string.punctuation).lower()
  #return collections.Counter(processed_text.split())
    