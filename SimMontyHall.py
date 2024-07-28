import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(46) #per la riproducibilità dei risultati
def monty_hall():
    selectedDoor, winningDoor = np.random.randint(low=1, high=4, size=2)

    door_options = [1, 2, 3]

    if selectedDoor == winningDoor:
        #se la scelta iniziale del concorrente è la porta con l'auto, il conduttore
        #sceglie in modo casuale dalle due porte rimanenti quale aprire, entrambi
        #contenenti una capra
        door_options.remove(selectedDoor)
        open_door = np.random.choice(door_options)

        #La switchingDoor conterrà una capra
        switchingDoor = [door for door in door_options if door != open_door][0]
    else:
        #quando il concorrente sceglie inizialmente una porta con una capra,
        #il conduttore apre l'altra porta contenente la capra, lasciando
        #l'auto dietro la switchingDoor

        door_options.remove(selectedDoor)
        door_options.remove(winningDoor)
        open_door = door_options[0]

        switchingDoor = winningDoor

    # l'1 indica una vittoria dell'auto, 0 invece una sconfitta
    if switchingDoor == winningDoor:
        switch = 1.
        non_switch = 0.
    else:
        switch = 0.
        non_switch = 1.

    return switch, non_switch

def simulate_monty_hall(simulations):
    switching_results = []
    not_switching_results = []

    for i in range(simulations):
        switch, non_switch = monty_hall()

        switching_results.append(switch)
        not_switching_results.append(non_switch)

    return switching_results, not_switching_results

switching_results, not_switching_results = simulate_monty_hall(100)
print('La percentuale di vincita quando si è cambiata scelta è del: {:.2f}%'.format(sum(switching_results) / len(switching_results) * 100))
print('La percentuale di vincita quando non si è cambiata scelta è del: {:.2f}%'.format(sum(not_switching_results) / len(not_switching_results) * 100))

df = pd.DataFrame(np.column_stack((switching_results, not_switching_results)), columns=['switching_win', 'non_switching_win'])
df['switch_pct'] = df['switching_win'].expanding().mean() * 100
df['not_switch_pct'] = df['non_switching_win'].expanding().mean() * 100
df = df[['switch_pct', 'not_switch_pct']]
df.columns = ['Cambia scelta', 'Non cambia scelta']

# Plotting the results
fig, ax = plt.subplots()
df.plot(ax=ax)
ax.set_title("Percentuali di vittoria per ogni scelta")
ax.set_ylabel("Percentuale di vittoria")
ax.set_xlabel("Numero di simulazioni")
#plt.savefig('/Users/andreacigna/Downloads/poche.svg')
plt.show()
