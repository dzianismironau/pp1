import matplotlib.pyplot as plt

xpoints = ['Car', 'Public transport', 'Bike', 'Foot']
ypoints = [25,19,32,7]

plt.bar(xpoints,ypoints)
plt.title('How do you commute to the work?')
plt.show()