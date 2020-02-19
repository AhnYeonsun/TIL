import sys

def main():
	cnt = int(input())
	if cnt <= 0:
		sys.exit()
	quiz = []
	for i in range(cnt): quiz.append(input())
	
	for a_quiz in quiz:
		sum = 0
		score = 0
		for char in a_quiz:
			if char == 'O':
				score += 1
				sum += score
			elif char == 'X':
				score = 0
		print(sum)

if __name__=="__main__":
	main()