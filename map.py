import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
ax.set_xlim(0,20)
ax.set_ylim(0,10)

#cities
city_x = [2,5,6,7,8,9]
city_y = [8,9,6,9,6,9]
labels = ['SFN', 'CHI', 'ATL', 'MTL', 'WDC', 'NYC']
cubes = [0,0,1,0,3,0]
players = ['','K','','','','E']

#routes
route_x = [2,5,6,8,9,7,5,7,8]
route_y = [8,9,6,6,9,9,9,9,6]

plt.scatter(city_x,city_y,c='blue')
plt.plot(route_x,route_y)
for i, label in enumerate(labels):
    ax.annotate(label, (city_x[i], city_y[i]))
for i, value in enumerate(cubes):
    ax.annotate(value, (city_x[i], city_y[i])) #need to use additional args to place the value elsewhere
# annotate players on their locations
plt.show()