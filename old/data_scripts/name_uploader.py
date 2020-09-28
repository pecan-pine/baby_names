#make file which will upload all baby name files into 
#one mysql database
# 1880-2018
with open('/home/uriel/test/baby_names/name_uploader.txt','w') as ostr:
	print('use baby_names;', file = ostr)
	for year in range(1880,2019):
		line = "load data local infile 'yobb"+str(year)+".txt' into table test2 fields terminated by ',';"
		print(line, file = ostr)
'''for line in istr:
				line = line.rstrip('\n') + ',' + str(year)+'-01-01'
				print(line,file = ostr)'''
ostr.close()
print(ostr.closed)
