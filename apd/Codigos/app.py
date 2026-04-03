#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Título de la aplicación
st.title('Mi Aplicación Streamlit')

# Mostrar texto
st.write('¡Hola, Mundo!')

# Crear un slider
valor = st.slider('Selecciona un número', 0, 100)
st.write(f'El número seleccionado es: {valor}')

# Mostrar un gráfico (usando matplotlib, por ejemplo)
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)

