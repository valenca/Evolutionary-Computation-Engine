from pickle import load

with open('fixed5', 'rb') as f:
	results = load(f)
final_bests_f5 = [result['best_fitnesses'][-1] for result in results]

with open('fixed10', 'rb') as f:
	results = load(f)
final_bests_f10 = [result['best_fitnesses'][-1] for result in results]

with open('adapt', 'rb') as f:
	results = load(f)
results[-15] = results[-16]
final_bests_a = [result['best_fitnesses'][-1] for result in results]

with open('f5_f10.csv', 'w') as f:
	for i in range(len(final_bests_f5)):
		f.write(str(final_bests_f5[i]*10000000)+','+str(final_bests_f10[i]*10000000)+'\n')

with open('f5_a.csv', 'w') as f:
	for i in range(len(final_bests_f5)):
		f.write(str(final_bests_f5[i]*10000000)+','+str(final_bests_a[i]*10000000)+'\n')
