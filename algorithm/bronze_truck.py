
def main():
	cost = (input()).split(" ")
	truck1 = (input()).split(" ")
	truck2 = (input()).split(" ")
	truck3 = (input()).split(" ")

	max_ = max(int(truck1[1]), int(truck2[1]), int(truck3[1]))
	sum = 0
	for time in range(1, max_+1):
		trucks_cnt = 0
		if int(truck1[0]) <= time and time < int(truck1[1]):
			trucks_cnt += 1
		if int(truck2[0]) <= time and time < int(truck2[1]):
			trucks_cnt += 1
		if int(truck3[0]) <= time and time < int(truck3[1]):
			trucks_cnt += 1
		
		if trucks_cnt == 0: continue
		elif trucks_cnt == 1: sum += int(cost[0])
		elif trucks_cnt == 2: sum += int(cost[1]) * 2
		elif trucks_cnt == 3: sum += int(cost[2]) * 3
	
	print(sum)

if __name__ == "__main__":
	main()