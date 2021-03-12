INPUT_FILE='/Users/marikof/Documents/research/CTI/SQuAD/train.json'
KEYWORD1='"is_impossible": "false"'
KEYWORD2='"is_impossible": "true"'

f = open(INPUT_FILE, 'r')
data = f.read()
f.close()

num_impossible=data.count(KEYWORD1)
num_possible=data.count(KEYWORD2)

print(num_impossible)
print(num_possible)
print(str(num_possible/num_impossible))