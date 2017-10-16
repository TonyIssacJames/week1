def timec(x):
	xh=int(x/60)
	xm=x%60
	return str(xh)+"h"+" "+str(xm)+"m"


a=timec(100)
print(a)