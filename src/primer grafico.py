import numpy as np
import matplotlib.pyplot as plt
plt.style.use("bmh")

datos = np.genfromtxt("datos_crudos_movil.txt")

theta = datos[:,0]
tiempo = datos[:,1]