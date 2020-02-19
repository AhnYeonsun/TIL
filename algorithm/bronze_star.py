import sys

def main():
	cnt = int(input())
	if cnt < 0:
		print("")
		sys.exit()
	for i in range(1, cnt+1):
		star = ""
		for j in range(cnt-i): star += " "
		for k in range(i): star += "*"
		print(star)


if __name__ == "__main__":
	main()