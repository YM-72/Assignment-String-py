# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line


player1='Ruud Gullit'
player2='Marco Van Basten'

goal_0 = 32
goal_1 = 54

scorers = f'{player1} {goal_0}, {player2} {goal_1}'



report = f'{player1} scored in the {goal_0} minute\n{player2} scorde in the {goal_1}nd minute.'

print(report)




player= 'Marco van Basten'


first_name = player[0:player.find(' ')] 

last_name_len =len(player[player.find(' '):])

name_short = name_short = player[0] + '.' + player[player.find(' '):]

chant = (len(first_name)-1)*(first_name+'! ')+(first_name+'!')

good_chant = (player[0:player.find(' ')] + '! ') * 5

print(chant)
print(good_chant)
print(good_chant != chant)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

