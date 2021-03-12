from datasets import load_dataset

#dataset = load_dataset('squad')
dataset = load_dataset('squad', split='train[:10]+validation[:2]')
#dataset = load_dataset('json', data_files='data.json', field='data', split='train[:10]+validation[:2]')
print(dataset)
