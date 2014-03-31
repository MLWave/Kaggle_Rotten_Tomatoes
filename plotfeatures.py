from pylab import *
import numpy as np
#Creates graph 
def show_most_informative_features(Y1W,Y1,Y2W,Y2,n=2):
	X = np.arange(n)
	axes([0.025,0.025,0.95,0.95])
	bar(X, Y1, facecolor='#ccccff', edgecolor='white')
	bar(X, Y2, facecolor='#ffcccc', edgecolor='white')
 
	for x,y,w in zip(X,Y1,Y1W):
		text(x+0.6, 0.2, '%.2f' % y, ha='center', va= 'center', rotation='vertical', size=7)
		text(x+0.4, max(Y1) + 0.2, '%s' % w, ha='center', va= 'bottom', rotation='vertical', size=10)
 
	for x,y,w in zip(X,Y2,Y2W):
		text(x+0.6, -0.2, '%.2f' % y, ha='center', va= 'center', rotation='vertical', size=7)
		text(x+0.4, min(Y2) - 0.4, '%s' % w, ha='center', va= 'top', rotation='vertical', size=10)
	xlim(-1,n), xticks([])
	ylim(min(Y2) - 1,max(Y1) + 1), yticks([])
 
	savefig('bar_informative_features.png', dpi=500)
	show()

#Formats data for graph
with open("rotten.varinfo.vw") as infile:
	d = {}
	for e, line in enumerate( infile.readlines() ):
		if e > 0:
			token = line.strip().split("\t")[0][2:].strip()
			value = line.strip().split("\t")[1].split(" ")[-1][:-1]
			d[token] = float(value)/float(100)

Y1W = sorted(d, key=d.get, reverse=True)[:100]
Y1 = [d[f] for f in sorted(d, key=d.get, reverse=True)[:100]]
Y2W = sorted(d, key=d.get)[:100]
Y2 = [d[f] for f in sorted(d, key=d.get)[:100]]

#do it
show_most_informative_features(Y1W,Y1,Y2W,Y2,len(Y1W))