import random

C = True # Cooperate
D = False # Defect
num_rounds = 1000
num_repetitions = 10

# Define the strategies
def cooperate(opponent_moves):
	return C

def defect(opponent_moves):
	return D

def tit_for_tat(opponent_moves):
	if not opponent_moves:
		return C
	else:
		return opponent_moves[-1]

def random_move(opponent_moves):
			return random.choice([C, D])
		
def grim_trigger(opponent_moves):
	if D in opponent_moves:
		return D
	else:
		return C

def pavlov(opponent_moves):
	if not opponent_moves:
		return C
	else:
		last_my_move = opponent_moves[-1]
		if last_my_move == C:
			return C
		else:
			return D
			
def always_defect(opponent_moves):
				return D
			
def always_cooperate(opponent_moves):
	return C

def tit_for_two_tats(opponent_moves):
	if len(opponent_moves) < 2:
		return C
	else:
		last_two_moves = opponent_moves[-2:]
		if last_two_moves == [D, D]:
			return D
		else:
			return C

def forgiving_tit_for_tat(opponent_moves):
	if not opponent_moves:
		return C
	else:
		last_opponent_move = opponent_moves[-1]
		if last_opponent_move == D:
			return C
		else:
			return D

def win_stay_lose_shift(opponent_moves):
	if not opponent_moves:
		return C
	else:
		last_my_move = opponent_moves[-1]
		if last_my_move == C:
			return C
		else:
			return D

def random_tit_for_tat(opponent_moves):
	if not opponent_moves:
		return C
	else:
		last_opponent_move = opponent_moves[-1]
		return C if last_opponent_move == C else random.choice([C, D])

def apply_strategy_except_first_last(strategy, opponent_moves):
	if len(opponent_moves) == 0 or len(opponent_moves) == num_rounds - 1:
		return C  # Cooperate in the first and last rounds
	else:
		return strategy(opponent_moves)  # Apply the desired strategy for other rounds

def apply_strategy_except_last_first(strategy, opponent_moves):
	if len(opponent_moves) == 0 or len(opponent_moves) == num_rounds - 1:
		return D  # Cooperate in the first and last rounds
	else:
		return strategy(opponent_moves)  # Apply the desired strategy for other rounds

def first_last_cooperate(opponent_moves):
	return apply_strategy_except_first_last(cooperate, opponent_moves)
			
def first_last_defect(opponent_moves):
	return apply_strategy_except_first_last(defect, opponent_moves)
	
def first_last_tit_for_tat(opponent_moves):
	return apply_strategy_except_first_last(tit_for_tat, opponent_moves)
	
def first_last_random_move(opponent_moves):
	return apply_strategy_except_first_last(random_move, opponent_moves)
	
def first_last_grim_trigger(opponent_moves):
	return apply_strategy_except_first_last(grim_trigger, opponent_moves)
	
def first_last_pavlov(opponent_moves):
	return apply_strategy_except_first_last(pavlov, opponent_moves)

def first_last_always_defect(opponent_moves):
	return apply_strategy_except_first_last(always_defect, opponent_moves)
	
def first_last_always_cooperate(opponent_moves):
	return apply_strategy_except_first_last(always_cooperate, opponent_moves)
		
def first_last_tit_for_two_tats(opponent_moves):
	return apply_strategy_except_first_last(tit_for_two_tats, opponent_moves)
	
def first_last_forgiving_tit_for_tat(opponent_moves):
	return apply_strategy_except_first_last(forgiving_tit_for_tat, opponent_moves)
	
def first_last_win_stay_lose_shift(opponent_moves):
	return apply_strategy_except_first_last(win_stay_lose_shift, opponent_moves)
	
def first_last_random_tit_for_tat(opponent_moves):
	return apply_strategy_except_first_last(random_tit_for_tat, opponent_moves)
#here			
def last_first_cooperate(opponent_moves):
	return apply_strategy_except_last_first(cooperate, opponent_moves)
			
def last_first_defect(opponent_moves):
	return apply_strategy_except_last_first(defect, opponent_moves)
	
def last_first_tit_for_tat(opponent_moves):
	return apply_strategy_except_last_first(tit_for_tat, opponent_moves)
	
def last_first_random_move(opponent_moves):
	return apply_strategy_except_last_first(random_move, opponent_moves)
	
def last_first_grim_trigger(opponent_moves):
	return apply_strategy_except_last_first(grim_trigger, opponent_moves)
	
def last_first_pavlov(opponent_moves):
	return apply_strategy_except_last_first(pavlov, opponent_moves)

def last_first_always_defect(opponent_moves):
	return apply_strategy_except_last_first(always_defect, opponent_moves)
	
def last_first_always_cooperate(opponent_moves):
	return apply_strategy_except_last_first(always_cooperate, opponent_moves)
		
def last_first_tit_for_two_tats(opponent_moves):
	return apply_strategy_except_last_first(tit_for_two_tats, opponent_moves)
	
def last_first_forgiving_tit_for_tat(opponent_moves):
	return apply_strategy_except_last_first(forgiving_tit_for_tat, opponent_moves)
	
def last_first_win_stay_lose_shift(opponent_moves):
	return apply_strategy_except_last_first(win_stay_lose_shift, opponent_moves)
	
def last_first_random_tit_for_tat(opponent_moves):
	return apply_strategy_except_last_first(random_tit_for_tat, opponent_moves)

#logic gates
def and_gate(a,b):
	return a and b

def or_gate(a, b):
	return a or b

def nand_gate(a,b):
	return not(a and b)
	
def nor_gate(a,b):
	return not(a or b)
	
def xor_gate(a, b):
	return a != b

def xnor_gate(a, b):
	return not(a != b)

# Define the tournament
strategies = [cooperate,
	defect,
	tit_for_tat,
	random_move,
	grim_trigger,
	pavlov,
	always_defect,
	always_cooperate,
	tit_for_two_tats,
	forgiving_tit_for_tat,
	win_stay_lose_shift,
	random_tit_for_tat,
	first_last_cooperate,
	first_last_defect,
	first_last_tit_for_tat,
	first_last_random_move,
	first_last_grim_trigger,
	first_last_pavlov,
	first_last_always_defect,
	first_last_always_cooperate,
	first_last_tit_for_two_tats,
	first_last_forgiving_tit_for_tat,
	first_last_win_stay_lose_shift,
	first_last_random_tit_for_tat,
	last_first_cooperate,
	last_first_defect,
	last_first_tit_for_tat,
	last_first_random_move,
	last_first_grim_trigger,
	last_first_pavlov,
	last_first_always_defect,
	last_first_always_cooperate,
	last_first_tit_for_two_tats,
	last_first_forgiving_tit_for_tat,
	last_first_win_stay_lose_shift,
	last_first_random_tit_for_tat
]

def default_logics(my_move,opponent_move,score):
	if my_move == C and opponent_move == C:
		score += 3
	elif my_move == C and opponent_move == D:
		score += 0
	elif my_move == D and opponent_move == C:
		score += 5
	elif my_move == D and opponent_move == D:
		score += 1
	return score
		
def and_logics(my_move,opponent_move,score):
	if and_gate(my_move,opponent_move) == C:
		score += 3
	elif my_move == C and opponent_move == D:
		score += 0
	elif my_move == D and opponent_move == C:
		score += 5
	elif and_gate(my_move,opponent_move) == D:
		score += 1
	return score
		
def or_logics(my_move,opponent_move,score):
	if or_gate(my_move,opponent_move) == C:
		score += 3
	elif or_gate(my_move, opponent_move) == D:
		score += 0
	elif or_gate(my_move, opponent_move) == C:
		score += 5
	elif or_gate(my_move,opponent_move) == D:
		score += 1
	return score

def nand_logics(my_move,opponent_move,score):
	if nand_gate(my_move,opponent_move) == C:
		score += 3
	elif nand_gate(my_move, opponent_move == D):
		score += 0
	elif nand_gate(my_move, opponent_move == C):
		score += 5
	elif nand_gate(my_move,opponent_move) == D:
		score += 1
	return score
		
def nor_logics(my_move,opponent_move,score):
	if nor_gate(my_move,opponent_move) == C:
		score += 3
	elif nor_gate(my_move,opponent_move) == D:
		score += 0
	elif nor_gate(my_move,opponent_move) == C:
		score += 5
	elif nor_gate(my_move,opponent_move) == D:
		score += 1
	return score
	
def xnor_logics(my_move,opponent_move,score):
	if xnor_gate(my_move,opponent_move) == C:
		score += 3
	elif xnor_gate(my_move, opponent_move) == D:
		score += 0
	elif xnor_gate(my_move, opponent_move) == C:
		score += 5
	elif xnor_gate(my_move,opponent_move) == D:
		score += 1
	return score

def xor_logics(my_move,opponent_move,score):
	if xor_gate(my_move,opponent_move) == C:
		score += 3
	elif xor_gate(my_move, opponent_move) == D:
		score += 0
	elif xor_gate(my_move, opponent_move) == C:
		score += 5
	elif xor_gate(my_move,opponent_move) == D:
		score += 1
	return score

def run(logic_type):
	# # Run the tournament
	results = {}
	total = []
	for strategy in strategies:
		scores = []
		for _ in range(num_repetitions):
			opponent_moves = []
			score = 0
			for _ in range(num_rounds):
				opponent_move = random.choice(strategies)(opponent_moves)
				opponent_moves.append(opponent_move)
				my_move = strategy(opponent_moves)
				if logic_type == "default":
					score = default_logics(my_move, opponent_move, score)
				elif logic_type == "and":
					score = and_logics(my_move,opponent_move,score)
				elif logic_type == "nand":
					score = nand_logics(my_move, opponent_move,score)
				elif logic_type == "or":
					score = or_logics(my_move, opponent_move,score)
				elif logic_type == "nor":
					score = nor_logics(my_move, opponent_move,score)
				elif logic_type == "xnor":
					score = xnor_logics(my_move, opponent_move,score)
				elif logic_type == "xor":
					score = xor_logics(my_move, opponent_move,score)
			scores.append(score)
		results[strategy.__name__] = scores
		avg_score = sum(scores) / num_repetitions
		total.append((strategy.__name__, avg_score))
	
	# Sort the strategies by score in descending order
	sorted_strategies = sorted(total, key=lambda x: x[1], reverse=True)
	return sorted_strategies

rounds = []
gates = ["default", "and", "nand", "or", "nor", "xnor", "xor"]
for g in gates:
	rs = []
	ro = f"{g}: Rounds: {num_rounds}:"
	table = None
	for r in run(g):
		rs.append((r[0],r[1]))
		from tabulate import tabulate
		table = tabulate(rs, tablefmt="grid")
	rounds.append((ro, table))

t = tabulate(rounds, tablefmt="grid")
print(t)