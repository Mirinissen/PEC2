# Si es necesario, se instalan las librerías
pip install matplotlib
pip install matplotlib_venn
pip install seaborn 
pip install ptitprince

# DIAGRAMA DE VENN
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

French = {'Arthur', 'Leonard', 'Debby', 'Bernadette', 'Alice', 'Ron', 'Penny', 'Sheldon'}
Math = {'Amy', 'Leo', 'Ash', 'Brandon', 'Sara', 'Alice', 'Ron', 'Annie', 'Jake', 'Zac'}
df = French | Math

venn2([Math,French], set_labels = ('Math','French'), set_colors=("blue", "pink"))
plt.title('Relación de estudiantes que toman clases de Mates y Francés')
plt.show()

# PIE CHART
import pandas as pd

DF = pd.read_csv('dataset/titanic-1.csv', sep=',')

DF_gb = DF.groupby('CLASS').size()
DF_gb = DF_gb.rename("Count")
DF_gb = DF_gb.reset_index()

clase = DF_gb['CLASS'].tolist()
pasaj = DF_gb['Count'].tolist()
col = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.figure(figsize=(7, 7))
plt.pie(pasaj, labels=clase, colors=col, autopct='%1.1f%%', startangle=90)
plt.title('Número de pasajeros en cada clase')
plt.show()

# RAINCLOUD PLOTS
import ptitprince as pt
import seaborn as sns

data = sns.load_dataset('penguins')
peng = data.dropna()

rc = pt.RainCloud(x = 'species', y = 'bill_length_mm', data = peng, palette = "Set2", orient = "h")
plt.show()
