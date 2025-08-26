s1, s2, s3, s4 = map(int, input().split())
number_to_buy = 4 - len(set([s1, s2, s3, s4]))
print(number_to_buy)