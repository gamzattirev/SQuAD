#INPUT_FILE='/Users/marikof/Documents/research/CTI/SQuAD/train.json'
INPUT_FILE='/Users/marikof/Documents/research/CTI/squad_org/train-v2.0.json'
KEYWORD1='"is_impossible": false'
KEYWORD2='"is_impossible": true'

f = open(INPUT_FILE, 'r')
data = f.read()
f.close()

num_possible=data.count(KEYWORD1)
num_impossible=data.count(KEYWORD2)

print(num_possible)
print(num_impossible)
print(str(num_possible/(num_possible+num_impossible)))