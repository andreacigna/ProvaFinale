import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definizione della funzione
def funzione(TPR, TNR, Prev):
    return (TPR * Prev)/(TPR * Prev + (1 - TNR) * (1 - Prev))

# Generazione dei dati
TPR = np.linspace(0, 1, 100)
TNR = np.linspace(0, 1, 100)
Prev = np.linspace(0, 1, 50)
X, Y, Z = np.meshgrid(TPR, TNR, Prev)
valori_funzione = funzione(X, Y, Z)

# Creazione del grafico 3D e del grafico della sezione
fig = plt.figure(figsize=(12, 5))

# Subplot per il grafico 3D
ax3d = plt.subplot2grid((1, 2), (0, 0), projection='3d')
scat = ax3d.scatter(X, Y, Z, c=valori_funzione, cmap='viridis')
fig.colorbar(scat, ax=ax3d)
ax3d.set_xlabel('TPR')
ax3d.set_ylabel('TNR')
ax3d.set_zlabel('Prev')

# Prendere una sezione del grafico
sezione_z = 0.3
x_sezione, y_sezione = np.meshgrid(TPR, TNR)
valori_funzione_sezione = funzione(x_sezione, y_sezione, sezione_z)

# Subplot per il grafico della sezione
ax_sezione = plt.subplot2grid((1, 2), (0, 1))
contour = ax_sezione.contourf(x_sezione, y_sezione, valori_funzione_sezione, levels=100, cmap='viridis')
fig.colorbar(contour, ax=ax_sezione)
ax_sezione.set_xlabel('TPR')
ax_sezione.set_ylabel('TNR')

# Mostra il grafico
plt.tight_layout()
plt.show()
