
data = []

for context in open("input.txt").read().rstrip().split('\n\n'):
    data.append(context.split('\n'))

union = 0
intersection = 0
# I used sets
# Thank you Junior Year Probability class for teaching me venn diagrams
for perGroup in data:  
    ans_intersection = perGroup[0]
    for individual in perGroup:
        print(individual)
        ans_union = set(''.join(perGroup))
        ans_intersection = set(individual) & set(ans_intersection)     
    print('----------')
    union+= len(ans_union)
    intersection += len(ans_intersection)
    print(ans_union)
    print(ans_intersection)
print(f'Part 1 {union}')
print(f"Part 2 {intersection}")