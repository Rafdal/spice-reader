import os
import ltspice
import matplotlib.pyplot as plt
import numpy as np
from libs.LTSpiceReader import ReadLTSpice
from libs.utils import searchMaxMinInRange, mean_spacing

import seaborn as sns
# Define a color palette with 5 colors
# palette = sns.color_palette("hsv", 100)

# Set the color palette
# sns.set_palette(palette)

# FILE INDEX TO OPEN
# No especificar el indice para que pregunte
data = ReadLTSpice(folder="data", idx=0)
data.info() # Imprime información del archivo LTSpice (variables, casos, etc)

# get index of strings appearning in list of strings in data.varListNames given a sublist of strings

def varNamesToIndex(varNames, data):
    return [i for i, x in enumerate(data.varListNames) if x in varNames]

var_index = varNamesToIndex(["I(C1)", "V(vin)"], data)

print(f"var_index: {var_index}")

fig, ax1 = plt.subplots()
ax2 = None


montecarloHist = []

if data.l._mode == "AC":
    for i in var_index:
        print(f"Plotting {data.varListNames[i]}")
        symbol = data.varListInfo[i]["symbol"]
        print(f"Symbol: {symbol}")
        c = data.colors[symbol]

        label = data.varListNames[i].upper()

        if data.is_montecarlo:

            for j, run in enumerate(data.varListData[i]):
                if j == 0:
                    showLabel = label
                else:
                    showLabel = None
                dB = 20 * np.log10(np.abs(run))
                phase = np.angle(run, deg=True)

                ax1.semilogx(data.x, dB, linewidth=0.2, alpha=1.0, label=showLabel)    

else:
    print("BAD")
    exit(1)
    for i in plot_VL_C1:
        print(f"Plotting {data.varListNames[i]}")
        symbol = data.varListInfo[i]["symbol"]
        print(f"Symbol: {symbol}")
        c = data.colors[symbol]

        label = data.varListNames[i].upper()

        if data.is_montecarlo:
            if ax2 == None:
                ax2 = ax1.twinx()

            for j, run in enumerate(data.varListData[i]):
                if j == 0:
                    showLabel = label
                else:
                    showLabel = None
                if data.varListInfo[i]["symbol"] == "I":
                    ax2.plot(data.x, run, linewidth=1.0, c=c, alpha=0.4, label=showLabel)
                    # maxs, mins = searchMaxMinInRange(data.x, run, 0.34, 0.36, c='black', s=3, ax=ax2, returnAxis='y', text = None)
                    # if mins[0] < -0.100:

                else:
                    ax1.plot(data.x, run, linewidth=1.0, c=c, alpha=0.4, label=showLabel)
        
        # NOT MONTECARLO
        else:
            x = data.x
            y = data.varListData[i]
            if data.varListInfo[i]["symbol"] == "I":
                ax2 = ax1.twinx()
                # [0:40]
                ax2.plot(x, y, linewidth=1.0, c=c, alpha=1.0, label=label)
                _, mins = searchMaxMinInRange(x, y, 0.04, 0.08, returnAxis='y', ax=ax2, c=c, text = "down", ignore = None)
            else:
                ax1.plot(x, y, linewidth=1.0, c=c, alpha=1.0, label=label)
                _, mins = searchMaxMinInRange(x, y, 0.04, 0.08, returnAxis='y', ignore = None, ax=ax1, c=c, text = "up")


if ax2 is not None:
    ax2.set_ylabel("Current (A)")  # Set the ylabel only if ax2 has been defined
ax1.set_ylabel("Voltage (V)")
ax1.set_xlabel('Time (s)')
ax1.set_title(data.filename)
ax1.grid()
if ax2 is not None:
    ax2.legend(loc="lower right")  # Set the legend only if ax2 has been defined
ax1.legend(loc="upper right")

# fig.subplots_adjust(right=0.85) # Adjust the right margin

    
plt.show()