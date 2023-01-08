import matplotlib.pyplot as plt

# Define the data
data=[10,0,0,0,0,0,0,0,0,0,0,0,0,0]
names = ["Aidan","Bryce","Cow","Dog","Easter","Fstring","Gargantuan","H name name","Illidan","Jungler","absds","dfgsdfg","dfgd34t","g vbfd"]

# Sort the data in decreasing order
#data = sorted(data, reverse=True)

# Create the chart\

plt.rcParams["figure.figsize"] = (15,5)
plt.barh(names,data,color="royalblue")



#plt.plot(range(len(data)), data,"r+")
plt.savefig("QPoints.pdf",format="pdf")

plt.title('Quarterly Points (10)', fontweight="bold")

plt.ylabel('Students', fontweight="bold")
plt.xlabel('Points', fontweight="bold")

plt.show()
