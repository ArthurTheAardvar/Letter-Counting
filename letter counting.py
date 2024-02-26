n_cases = int(input())
for _ in range(n_cases):
    # write your code starting here. replace these lines as needed:
    line = input().rstrip()
    args = (val for val in line.split(" "))

    
    print(len(line) + 1)
