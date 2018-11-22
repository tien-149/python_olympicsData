import csv
import matplotlib.pyplot as plt 

golds = []
silvers = []
bronzes = []

catagories = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print('tripping out catagories')
			catagories.append(row)
			line_count += 1
		else:
			if row[7] == "Gold":
				print('gold')
				golds.append(row[7])
			elif row[7] == "Silver":
				print('silver')
				silvers.append(row[7])
			elif row[7] == "Bronze":
				bronzes.append(row[7])
			line_count += 1


print(len(golds), 'gold medals were won since \'24')
print(len(silvers), 'silver medals were won since \'28')
print(len(bronzes), 'bronze medals were won since \'28')

totalMedals = len(golds) + len(silvers) + len(bronzes)

# percentage of all medals
gold_percentage = int(len(golds) / totalMedals * 100)
silver_percentage = int(len(silvers) / totalMedals * 100)
bronze_percentage = int(len(bronzes) / totalMedals * 100)

print(gold_percentage, silver_percentage, bronze_percentage)



print('processed', line_count, 'lines of data. Total medals', totalMedals)

labels = "Gold", "Silver", "Bronze"
sizes = [gold_percentage, silver_percentage, bronze_percentage]
colors = ('yellowgreen', 'lightgreen', 'red')
explode = (0.1, 0.1, 0.15)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.legend(labels, loc=1)
plt.title("Medals win ")
plt.xlabel("Medals since 1024")
plt.show()





















