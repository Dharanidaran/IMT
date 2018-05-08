import matplotlib.pyplot as plt
import numpy as np

dice1 = np.random.randint(1,7,10)
print(dice1)
dice2 = np.random.randint(1,7,10)
print(dice2)
sum_of_dice = dice1 + dice2
print(sum_of_dice)



#Calculate bin size

num_of_bin = 11


#2,3,4,5,6,7,8,9,10,11,12



num_of_bins = 11
n,bins,patches =  plt.hist(sum_of_dice, num_of_bins, facecolor="blue",alpha=0.5)
plt.show()