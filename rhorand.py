import random
import math
import matplotlib.pyplot as plt

period=int(input("Enter the time period: "))

channel_vacancy={'1':0.1,'2':0.2,'3':0.3,'4':0.4,'5':0.5,'6':0.6,'7':0.7,'8':0.8,'9':0.9,'10':0.95}
num_channel=[1,2,3,4,5,6,7,8,9,10]
users=[1,2,3,4,5]
best_channels=[6,7,8,9,10]

# channel_vacancy={'1':0.06,'2':0.12,'3':0.18,'4':0.24,'5':0.30,'6':0.36,'7':0.42,'8':0.48,'9':0.54,'10':0.60,'11':0.66,'12':0.72}
# num_channel=[1,2,3,4,5,6,7,8,9,10,11,12]
# users=[1,2,3,4,5,6]
# best_channels=[7,8,9,10,11,12]


times_played = {'1':1,'2':1,'3':1,'4':1,'5':1}
reward_arms = {'1':0,'2':0,'3':0,'4':0,'5':0}
regret_arms = {'1':0,'2':0,'3':0,'4':0,'5':0}
X_bar = {'1':0,'2':0,'3':0,'4':0,'5':0}
A_bias = {'1':0,'2':0,'3':0,'4':0,'5':0}
B_index = {'1':0,'2':0,'3':0,'4':0,'5':0}
rnd=round(random.uniform(0,1),2)

graph={}

max_achievable = 0
for key,value in channel_vacancy.items():
    if value >= max_achievable:
        max_achievable = value


for ff in range(20):
    fixed={}
    regret_calc=0
    t=len(num_channel)+1

    while t<period+1:
        channel_selected_by_users={}
        frequency={}
        for i in range(len(users)):
            if(i+1 in fixed):
                continue
            channel_selected=random.choice(num_channel)
            if (channel_selected in frequency):
                frequency[channel_selected] += 1
            else:
                frequency[channel_selected] = 1
            channel_selected_by_users[i+1]=channel_selected

        for ch in users:
            if(len(fixed)==len(users)):
                regret_calc+=0
                continue   
            if(ch in fixed):
                regret_calc+= max_achievable - channel_vacancy[str(fixed[ch])]
                # regret_calc+=0
                rnd=round(random.uniform(0,1),2)
                continue
            if(channel_selected_by_users[ch] in fixed.values()):
                regret_calc+=max_achievable
                continue

            if(rnd<=channel_vacancy[str(channel_selected_by_users[ch])] and frequency[channel_selected_by_users[ch]]==1 and channel_selected_by_users[ch] in best_channels):
                regret_calc+=max_achievable - channel_vacancy[str(channel_selected_by_users[ch])]
                fixed[ch]=channel_selected_by_users[ch]
                rnd=round(random.uniform(0,1),2)
            else:
               regret_calc += max_achievable    
               rnd=round(random.uniform(0,1),2)

        if(t in graph):
            graph[t]+=regret_calc
        else:
            graph[t]=regret_calc
        t+=1

# for key,value in graph.items():
#     graph[key]=value/10
print(fixed)

x=graph.keys()
y=graph.values()
plt.plot(x,y,'k--',label='Regret Plot')


plt.xlabel('Time Period')
plt.ylabel('Values')
plt.title('Cumulative Regret Plot')
plt.legend()
plt.grid(True)
plt.show()
