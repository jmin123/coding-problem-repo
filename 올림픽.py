n, k = map(int, input().split())

medals = []
target_medals = None

for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    medals.append((gold, silver, bronze))
    if country == k:
        target_medals = (gold, silver, bronze)

rank = 1

for medal in medals:
    if medal > target_medals:
        rank += 1

print(rank)