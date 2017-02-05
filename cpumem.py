import csv
namafile = ["After","After2","After3","Before","Before2","Before3","Cache","Cache2","Cache3","Memory","Memory2","Memory3"]
for j in range (len(namafile)):
	for i in range (1,11):
		f = open(namafile[j]+'/u'+str(i)+'0.csv',"rb")
		read = csv.reader(f)
		rownum = 0
		ofile = open('cpumem'+namafile[j]+'.csv',"a")
		writer = csv.writer(ofile, delimiter= ",", quoting= csv.QUOTE_ALL)
		for row in read:
			if rownum == 0:
				header = row
			else:
				colnum = 0		
				a = ['','']	
				for col in row:
					if colnum==1:
						a[0] = col
					elif colnum==2:
						a[1] = col
					colnum += 1
				b=a[0]
				writer.writerow([a[0],a[1]])
			rownum +=1
		writer.writerow([''])
		writer.writerow([str(i+1)+'0'])
		ofile.close()
		f.close()
		i+=1
	j+=1
