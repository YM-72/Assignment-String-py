# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player1='Ruud Gullit'
player2='Marco Van Basten'

goal_0 = 32
goal_1 = 54

scorers = f'{player1} {goal_0}, {player2} {goal_1}'

print(scorers)


report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute.'

print(report)




player= 'Marco van Basten'


first_name = player[0:player.find(' ')] 


last_name_len = len(player[player.find(' '):])



name_short = player[0] + '.' + player[player.find(' '):]

chant = (len(first_name)-1)*(first_name+'! ')+(first_name+'!')


good_chant = chant[-1] != ' ' 
