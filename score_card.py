def pins_knocked_over(score_card: str) -> int:
  scores = score_card.split(" ")
  total = 0 

  for frame in scores: 
    total += calculate_frame(frame)            

  return total

"""
  This function runs as usual for all but the last run, it checks if there is an X or a / in the frame, if so return 10.

  Then for numbers scores it totals the numbers and returns the total.

  Then on the last there are 6 posibilities

  XXX
  XX3
  X8/
  8/X
  8/2
  52

  The way we deal with this, if we find a X in out frame and there is more than one roll, remove and run the function over the rest of the frame.

  If there is a spare in the frame and there is more than 2 rolls, remove the roll and the previous roll, the run the function over the rest of the frame.
"""
def calculate_frame(frame: str) -> int:
  total = 0
  length = len(frame)
  if 'X' in frame:
    """ Only on last frame """
    if length > 1:
      index = frame.index('X')
      reduced = frame[:index] + frame[index+1:]
      total += calculate_frame(reduced)
    total += 10

    return total
  if '/' in frame:
    """ Only on last frame """
    if length > 2:
      index = frame.index('/')
      reduced = frame[:index-1] + frame[index+1:]
      total += calculate_frame(reduced)
    total += 10

    return total
    
  for i in frame:
    if i == "-":
      continue
    total += int(i)
  return total


"""
	A little post challenge fun, revisited the challenge challenge :)

	We deal with it in reverse so we only need to parse each roll once.

	Then we keep an active stack of future rolls to use when we get a strike and spare.
"""
def full_score(score_card: str) -> int:
	reversedScores = score_card.split(" ")[::-1]
	rolls = []
	total = 0
	for _, frame in enumerate(reversedScores):
		total += calculate_score(frame, rolls)
	
	return total

"""
	This is the meat of the challenge.

	In here we deal with the frame roll by roll.
		- If it is a strike, we append 10 to the score and roll, and add the next two rolls
		- If it is a spare we add 10 - previous successful roll (not a gutter ball) to both the score and rolls, with the next roll.
		- Then if it is a number we call calc_roll.

	We deal with roll in order to create less complexity with spares.
"""
def calculate_score(frame: str, nextRolls: list) -> int: 
	rolls = []
	score = 0

	for roll in iter(frame):
		if roll == 'X':
			rolls.append(10)
			score += sum(nextRolls[-2:])
			score += 10

		elif roll == '/':
			knockedPinsInSpare = 10 - get_previous_roll(rolls)
			rolls.append(knockedPinsInSpare)
			score += knockedPinsInSpare
			score += sum(nextRolls[-1:])

		else:
			rollVal = calc_roll(roll)
			score += rollVal
			rolls.append(rollVal)

	nextRolls.extend(rolls[::-1])
	return score

"""
	This is used for spares, to calculate the amount of pins knocked over we need
	the previous successful rolls pins knocked.
"""
def get_previous_roll(rolls: list) -> int:
	for roll in iter(rolls):
		if roll == '-':
			continue
		return int(roll)

	"""
		Should never reach this, just for LSP to be happy.
	"""
	return 0

"""
Small helper funciton to deal with rolls that aren't strikes or spares
"""
def calc_roll(roll: str) -> int:
	if roll == '-':
		return 0
	return int(roll)
