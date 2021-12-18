# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player1='Ruud Gullit'
player2='Marco Van Basten'

goal_0 = 32
goal_1 = 54

scorers = player1 + ' '+  str(goal_0) , player2 + ' '+ str(goal_1)



report = player1 + ' scored in the ' + str(goal_0)+'nd'+ ' ' + 'minute\n' + player2 + ' scored in the ' + str(goal_1)+'nd ' + 'minute'



player= 'Marco van Basten'


first_name = player[0:player.find(' ')] 

last_name_len =len(player[player.find(' '):])

name_short = name_short = player[0] + '.' + player[player.find(' '):]

chant = (player[0:player.find(' ')] + '!\t') * 3

good_chant = 1



x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

