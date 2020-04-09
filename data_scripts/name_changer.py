#this script opens the files from ssa.gov and tacks on the year
#to the end of each line (the year is in the filename)
# 1880-2018
for year in range(1880,2019):
	with open('/home/uriel/test/baby_names/yob'+str(year)+'.txt','r') as istr:
		with open('/home/uriel/test/baby_names/yobb'+str(year)+'.txt','w') as ostr:
			for line in istr:
				line = line.rstrip('\n') + ',' + str(year)+'-01-01'
				print(line,file = ostr)
