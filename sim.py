# documentation


class space():
  #doc
  def __init__(self, move=0):
    self.left = None
    self.right = None
    self.chute = None
    self.ladder = None
  
class game():
  
  def __init__(self, board_size=100):
    for i in range(board_size):
      
class spinner():
  
  def __init__(self, min=1, max=6):
    self.min=min
    self.max=max
  
  def roll(self):
    #create random
    from random import randrange
    return randrange(self.min, self.max)
  
 
  
#check out http://markov.yoriz.co.uk
# maybe get R and R-studio
#could you estimate landing probs by summing incoming probs + prior probs * a weight + prior prior probs * smaller weight, etc?
# or something like the sumproduct for n generations of all incoming probs?
  
###ver 2
from random import randrange
ladders = {1:38, 4:14, 9:31, 21:42, 28:84, 36:44, 51:67, 71:91, 80:100}
chutes = {98:78, 95:75, 93:73, 87:24, 64:60, 62:19, 56:53, 49:11, 47:26, 16:6}
location = 0
max=6
min=1
warp = None
while location<=100:
  r = randrange(min, max)
  location += r
  warp = 
