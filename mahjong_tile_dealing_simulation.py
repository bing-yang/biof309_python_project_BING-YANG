import random 
import numpy as np 
import collections 

#mahjong tiles constitution and shuffling#
player_1_confirm = input ('Player_1, Press any button to start:') #prompt user to start# 
player_2_confirm = input ('Player_2, Press any button to start:') #prompt user to start# 
player_3_confirm = input ('Player_3, Press any button to start:') #prompt user to start# 
player_4_confirm = input ('Player_4, Press any button to start:') #prompt user to start# 

mahjong = []
for i in range(1,10):                                             #constitute a mahjong set# 
    for j in ['dot','character','bamboo']:
        mahjong.append(str(i) + '_' + j)                      
mahjong = mahjong * 4 
random.shuffle(mahjong)
print ('mahjong shuffling is all set') #shuffling the mahjong tiles randomly# 

#mahjong wall buidling by four players# 
player_1_mahjong_wall = mahjong[0:27]
player_2_mahjong_wall = mahjong[27:54]
player_3_mahjong_wall = mahjong[54:81]
player_4_mahjong_wall = mahjong[81:108]
mahjong_walls = {'player_1': player_1_mahjong_wall, 'player_2': player_2_mahjong_wall, 
                'player_3': player_3_mahjong_wall, 'player_4': player_4_mahjong_wall}
print (mahjong_walls)

#dice rolling to decide the dealer position# 
def dice_roll():
    dice_1 = random.sample(range(1,7),1)
    dice_2 = random.sample(range(1,7),1)
    dice_num = dice_1[0] + dice_2[0] 
    return dice_1, dice_2, dice_num, min(dice_1, dice_2) 
    

player_roster =['player_1','player_2','player_3','player_4']
roll_dict ={}
for i in player_roster: 
    print (input(i + ', Please roll your dice:'))
    roll = dice_roll()
    roll_dict.update({i:roll[2]})
    print (roll[0:2])
sorted_roll_dict = sorted((value,key) for (key, value) in roll_dict.items())
print ('the dealer position is:', sorted_roll_dict[-1])


#dealer rolls dices to decide where to break the wall# 
dealer_roll = dice_roll()
player_roster =['player_1','player_2','player_3','player_4']
wall_break_side = player_roster[dealer_roll[2]%4] 
#get an ordered mahjong walls dict for later indexing purposes# 
from collections import OrderedDict 
mahjong_walls_ordered = OrderedDict()
for k, v in mahjong_walls.items():
    mahjong_walls_ordered[k] = v 
print (mahjong_walls_ordered)

#one way to start to randomly draw tiles# 
def random_draws():    
   index = np.random.choice(range(len(mahjong)),13,replace = False)
   mahjong_hand = []
   for i in index: 
     mahjong_hand.append(mahjong[i])
   for i in index: 
      mahjong[i] = 0 
   for i in mahjong:
        if i == 0:
            mahjong.remove(i)
   return mahjong_hand 
    
player_1 = random_draws()
player_2 = random_draws()
player_3 = random_draws()
player_4 = random_draws()



#different types of melds# 
def melds():
    meld_chow = []
    for i in range(1,8):
        return meld_chow.append([i, i+1, i+3])
    meld_chow_array = np.array(meld_chow)   #chow# 
    
    meld_pong = []
    for i in range(1,10):
        return meld_pong.append([i,i,i])
    meld_pong_array = np.array(meld_pong)  

    meld_kong = []
    for i in range(1,10):
        return meld_kong.append([i,i,i,i])
    meld_kong_array = np.array(meld_kong)


print (player_1)
print (player_2)
print (player_3)
print (player_4)
    
