#make the function output bigger
#the input is now a list of names and genders like [('john','m'),('rachel','f')]
import mysql.connector
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
def large_name_plot(name_list):
    #create figure and subfigure
    fig = plt.figure(figsize=(10,10))
    sub = fig.subplots()
    sub.set_xlabel('Year')
    sub.set_ylabel('Numbe of People')
    max_max = 0
    for name,gender in name_list:
        #save the query as text
        query = "SELECT year(year), frequency FROM test2 WHERE name='"+name+"' AND sex='"+gender+"';"
        #perform query and get results
        cur.execute(query)
        data=cur.fetchall()
        #save results into two lists
        #year
        x_val = [x[0] for x in data]
        #number of people
        y_val = [x[1] for x in data]
        #maximum number of names
        y_max = max(y_val)
        #year where maximum numbe appeared
        x_max = data[y_val.index(y_max)][0]
        #annotate the maximum
        plt.annotate(str(name).capitalize()+' ('+str(gender)+')'+' peaked at '+str(y_max)+' in ' + str(x_max), 
                 xy=(x_max,y_max), xytext=(x_max+(x_max+100)/100,y_max+(y_max+1000)/2000),
             arrowprops=dict(facecolor='black', shrink=.1,width = 1,headwidth=10))
        #make a dot where the maximum is
        sub.plot(x_max,y_max,'bo')
        #plot the lists against each other
        sub.plot(x_val,y_val, label="Name="+name.capitalize()+", Gender="+gender)
        #create a legend
        sub.legend(fontsize=10,loc='center left')
