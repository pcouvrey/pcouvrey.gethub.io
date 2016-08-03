import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os.path

movie_category = 'Drama'
year_min = 1920
year_max = 1995

directory = os.path.dirname(os.path.abspath(__file__))  

years=[]
total=[]
total_color = 'red'
award=[]
award_color = 'blue'
for year in range(year_min,year_max):
    years.append(year)
    total.append(0)
    award.append(0)

filename = os.path.join(directory, 'film.csv')
datafile = open(filename,'r')
next(datafile)
next(datafile)
for line in datafile:
    year,length,title,subject,actor,actress,director,popularity,awards,image = line.split(',')
    year = int(year)
    if year >= year_min and year < year_max:
        if movie_category == subject:
            total[year - year_min] = total[year - year_min]+1
            if awards == "Yes":
                award[year-year_min]=award[year-year_min]+1
datafile.close()

max_found = 0
for year in range(0, year_max - year_min):
    if total[year] > max_found:
        max_found = total[year]

fig, ax = plt.subplots(1,1)
axes = plt.gca()
axes.set_ylim([0,max_found*1.25])
ax.plot(years, total,total_color)
ax.plot(years, award,award_color)
total_patch = mpatches.Patch(color=total_color, label='Total '+movie_category)
award_patch = mpatches.Patch(color=award_color, label='Award Winning '+movie_category)
plt.legend(handles=[total_patch, award_patch])
ax.set_title('Number of '+movie_category+' Movies By Year from '+str(year_min)+' to '+str(year_max))
fig.show()
