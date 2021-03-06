import pandas as pd
import matplotlib.pyplot as plt

#Reads CSV raw file on Github
df = pd.read_csv ("https://raw.githubusercontent.com/ryan-j-hope/Shielding-models/master/2020%20Uk%20Population%20By%20Age%20Demographics.csv", encoding='UTF')

#Removes row 10
df.drop(10,inplace = True)

print(df)

#Plots and lables chart
ag = df["Age Group"]

pop = df["Population (%)"]

plt.ylabel("Population (%)")

plt.xlabel("Age Group")

plt.bar(ag, pop)

#Removes axes spines so that the "39 %" annotation is not outside the boundary of the graph
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

#Annotates columns
index1 = 6
index2 = 9
h = max(pop[index1:index2+1]) # maximum of the involved bar heights
bx = [index1-0.5, index1-0.5, index2+0.5, index2+0.5] 
by = [h + 0.5, h + 1, h + 1, h + 0.5]
plt.plot(bx, by, 'k-', lw=2)
plt.text((index1 + index2) / 2, h + 1.5, f'{sum(pop[index1:index2+1]):.0f} %', size=20, ha='center', va='bottom')

index3 = 7
index4 = 9
h = max(pop[index3:index4+3]) # maximum of the involved bar heights
bx = [index3-0.5, index3-0.5, index4+0.5, index4+0.5]
by = [h + 0.5, h + 1, h + 1, h + 0.5]
plt.plot(bx, by, 'k-', lw=2)
plt.text((index3 + index4) / 2, h + 1.5, f'{sum(pop[index3:index4+3]):.0f} %', size=20, ha='center', va='bottom')

index5 = 8
index6 = 9
h = max(pop[index5:index6+5]) # maximum of the involved bar heights
bx = [index5-0.5, index5-0.5, index6+0.5, index6+0.5]
by = [h + 0.5, h + 1, h + 1, h + 0.5]
plt.plot(bx, by, 'k-', lw=2)
plt.text((index5 + index6) / 2, h + 1.5, f'{sum(pop[index5:index6+5]):.0f} %', size=20, ha='center', va='bottom')

index7 = 5
index8 = 9
h = max(pop[index7:index8+7]) # maximum of the involved bar heights
bx = [index7-0.5, index7-0.5, index8+0.5, index8+0.5]
by = [h + 0.5, h + 1, h + 1, h + 0.5]
plt.plot(bx, by, 'k-', lw=2)
plt.text((index7 + index8) / 2, h + 1.5, f'{sum(pop[index7:index8+7]):.0f} %', size=20, ha='center', va='bottom')




plt.show() 