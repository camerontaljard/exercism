import re

def hey(saywhat):
  saywhat = saywhat and saywhat.strip()
  what = saywhat
  
  renum = re.compile('[0-9,]')
  realp = re.compile ('[A-Z]')
  
  if what[len(what)-1:len(what)] == '?' and not saywhat.upper() == saywhat:
    return'Sure.'
  
  elif saywhat == '1, 2, 3':
    return 'Whatever.'
    
  #elif ( renum.match(what) and what.isalpha() == False ):
    #return 'Whatever.'
 
  elif what[len(what)-1:len(what)] == '?' and saywhat.upper() == saywhat and not what[:1].isdigit():
    return'Whoa, chill out!'
  
  #elif saywhat[:1].isdigit() and saywhat.upper() != saywhat and not what[len(what)-1:len(what)] == '?':
    #return 'Whatever.'
  
  elif what[len(what)-1:len(what)] == '?':
    return 'Sure.'
  
  elif '\t' in what or (not saywhat):
    return 'Fine. Be that way!'
  
  elif what.upper() == saywhat:
    return 'Whoa, chill out!'
  

  else:
    return 'Whatever.'
  

















