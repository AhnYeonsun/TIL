import copy

def main():
	dogs = (input()).split(" ")
	delivery = (input()).split(" ")
	A, B, C, D = int(dogs[0]), int(dogs[1]), int(dogs[2]), int(dogs[3])
	for i in range(3):
		cnt = 0
		flag = 0
		gt = A
		lte = gt + B
		tmp_delivery = int(delivery[i])
		while tmp_delivery > gt:
			if gt < tmp_delivery and tmp_delivery <= lte: # 쉼?
				flag = 1
				break
			gt = lte + A
			lte = gt + B
		if flag == 0: 
			cnt += 1
		flag = 0
		gt = C
		lte = gt + D
		while tmp_delivery > gt:
			if gt < tmp_delivery and tmp_delivery <= lte:
				flag = 1
				break
			gt = lte + C
			lte = gt + D
		if flag == 0:
			cnt += 1

		print(cnt)



if __name__ == "__main__":
	main()