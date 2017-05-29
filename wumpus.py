from random import choice

cave_numbers = range(1,51)
wumpus_location = choice(cave_numbers)
wumpus_found = False
wumpus_friend_location = choice(cave_numbers)
wumpus_friend_found = False
player_location = choice(cave_numbers)
last_player_location = ()
block_count = 0
move_count = 0
wumpus_block_location = 0
wumpus_friend_block_location = 0
double_wumpus_block_location = ()
tools = {'radar':3,'block':2}
# create a dict() for 'help' or 'info' or 'rules' about this game... Figure out how to manage dict().
skip = False
skip_intro = False
while player_location == wumpus_location or player_location == wumpus_friend_location:
	player_location = choice(cave_numbers)

if skip_intro == False:
	print ""
	print "---------->Hunt the Wumpus!<----------"
	print ""
	print "There are", len(cave_numbers),"caves in this quary."
	print "Type the number of the cave you want to enter."
	print "Type 'block <cave #>' to trap a Wumpus."
	print "Type 'done' to exit the game."
	# print "Wumpus = ", wumpus_location
	# print "Wumpus Friend = ", wumpus_friend_location
	print ""
	skip_intro = True


while True:
	if skip == False:
		print "You're in cave", player_location
		print "You have", 2 - block_count,"block(s) remaining."
		last_player_location = player_location
		if (player_location == wumpus_location - 1 or player_location == wumpus_location + 1): print "This cave is clear, but I smell a wumpus!"
		elif (player_location == wumpus_friend_location - 1 or player_location == wumpus_friend_location + 1): print "This cave is clear, but I smell a wumpus!"
		else: print "This cave is clear."
	else: 
		skip = False

	player_input = raw_input("---> ")
	move_count = move_count + 1
	if player_input == 'done': break
	if player_input == 'loc' or player_input == 'location':
		print "You're in cave", player_location
		skip = True
		continue	
	if player_input == 'tools':
		for tool in tools:
			print tool.title(), ' - ', tools.get(tool)
		skip = True
		continue		
	if player_input == 'radar':
		if tools['radar'] > 0:
			move_count = move_count + 1
			tools['radar'] -= 1
			# print 'count of radar =',tools['radar'] #test decrement of uses: this works, feel free to clean up rems
			if abs(wumpus_location - player_location) < 5 or abs(wumpus_friend_location - player_location) < 5: print "RADAR: A wumpus is very close."
			elif abs(wumpus_location - player_location) < 15 or abs(wumpus_friend_location - player_location) < 15: print "RADAR: There's a wumpus not too far away."
			elif abs(wumpus_location - player_location) >= 15 or abs(wumpus_friend_location - player_location) >= 15: print "RADAR: No wumpuses around here."
			skip = True
			continue
		else:
			print "Sorry, you don't have any radar left."
			skip = True
			continue
	if int(player_input[-2:]) == wumpus_block_location or int(player_input[-2:]) == wumpus_friend_block_location: 
		print "That cave is blocked; you can't go in there."
		skip = True
		continue
	if (player_input[:5] == 'block' and int(player_input[-2:]) == wumpus_location) and (player_input[:5] == 'block' and int(player_input[-2:]) == wumpus_friend_location):
		double_wumpus_block_location = int(player_input[-2:])
		print "\nGrand slam! You trapped both wumpuses in cave", double_wumpus_block_location,"in",move_count,"moves\n"
		break
	elif player_input[:5] == 'block' and int(player_input[-2:]) == wumpus_location:
		wumpus_found = True
		wumpus_block_location = int(player_input[-2:])
		if wumpus_found == True and wumpus_friend_found == True:
			print "\nThat's it! You got both of them in",move_count,"moves!\n"
			block_count = block_count + 1
			tools['block'] -= 1
			break
		else:
			wumpus_location = wumpus_block_location + max(cave_numbers)
			print "You trapped the wumpus in cave", wumpus_block_location
			block_count = block_count + 1
			tools['block'] -= 1
			if abs(player_location - wumpus_friend_location) < 5: print "Be careful, his friend is close by."
			elif abs(player_location - wumpus_friend_location) < 15: print "His friend is not too far away."
			elif abs(player_location - wumpus_friend_location) >= 15: print "His friend is out there somewhere."
			skip = True
	elif player_input[:5] == 'block' and int(player_input[-2:]) == wumpus_friend_location:
		wumpus_friend_found = True
		wumpus_friend_block_location = int(player_input[-2:])
		if wumpus_found == True and wumpus_friend_found == True:
			print "\nThat's it! You got both of them in",move_count,"moves!\n"
			break
		else:
			wumpus_friend_location = wumpus_friend_block_location + max(cave_numbers)
			print "You trapped the wumpus' friend in cave", wumpus_friend_block_location
			block_count = block_count + 1
			tools['block'] -= 1
			if abs(player_location - wumpus_location) < 5: print "Be careful, the wumpus is close by."
			elif abs(player_location - wumpus_location) < 15: print "The wumpus is not too far away."
			elif abs(player_location - wumpus_location) >= 15: print "The wumpus is out there somewhere."
			skip = True
	elif player_input[:5] == 'block' and int(player_input[-2:]) != (wumpus_location or wumpus_friend_location):
		block_count = block_count + 1
		tools['block'] -= 1
		if block_count == 1: print "Sorry, there's no wumpus in cave", int(player_input[-2:]), "and you've wasted one block..."
		if block_count == 2: print "Sorry, there's no wumpus in cave", int(player_input[-2:]), "and now you are out of blocks..."
	elif not player_input[-2:].isdigit() or int(player_input[-2:]) not in cave_numbers:
		print player_input,"is not a cave..."
	else:
		player_location = int(player_input)
		if player_location == wumpus_location or player_location == wumpus_friend_location: 
			print "Aargh!!!! You've been eaten by a wumpus!\n"
			break


