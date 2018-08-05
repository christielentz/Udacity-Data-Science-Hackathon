import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from textwrap import wrap

mortality = pd.read_csv("C:/Users/Christina/Documents/Python/mortality.csv")
antenatal = pd.read_csv("C:/Users/Christina/Documents/Python/antenatal.csv")
csection = pd.read_csv("C:/Users/Christina/Documents/Python/csection.csv")
personnel = pd.read_csv("C:/Users/Christina/Documents/Python/personnel.csv")

mortality["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"] = mortality["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"].str.split().str[0]
mortality["Neonatal mortality rate (per 1000 live births)"] = mortality["Neonatal mortality rate (per 1000 live births)"].str.split().str[0]

mortality["Year"] = pd.to_numeric(mortality["Year"])
mortality["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"] = pd.to_numeric(mortality["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"])
mortality["Neonatal mortality rate (per 1000 live births)"] = pd.to_numeric(mortality["Neonatal mortality rate (per 1000 live births)"])
mortality = mortality.drop(mortality[mortality.Year < 2008].index)


mort = mortality.groupby('Country').mean()
combined_data_csection = mort.merge(csection, how='left', on='Country')
combined_data_csection = combined_data_csection.dropna()
combined_data_csection = combined_data_csection.drop(combined_data_csection[combined_data_csection.Country == "United Kingdom of Great Britain and Northern Ireland"].index)
combined_data_csection = combined_data_csection.drop(combined_data_csection[combined_data_csection.Country == "South Sudan"].index)
combined_data_csection["Births by caesarean section (%)"] = pd.to_numeric(combined_data_csection["Births by caesarean section (%)"])

combined_data_personnel = mort.merge(personnel, how='left', on='Country')
combined_data_personnel = combined_data_personnel.dropna()
combined_data_personnel["Births attended by skilled health personnel (%)"] = pd.to_numeric(combined_data_personnel["Births attended by skilled health personnel (%)"])

combined_data_antenatal = mort.merge(antenatal, how='left', on='Country')
combined_data_antenatal = combined_data_antenatal.dropna()
combined_data_antenatal["Antenatal care coverage - at least four visits (%)"] = pd.to_numeric(combined_data_antenatal["Antenatal care coverage - at least four visits (%)"])


plt.scatter(combined_data_csection["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"],combined_data_csection["Births by caesarean section (%)"])
plt.xlabel("Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)")
plt.ylabel("Births by caesarean section (%)")
title = "Infant Mortality Rate vs. Percentage of Births by Caesarean Section"
plt.title('\n'.join(wrap(title,60)))
plt.show()

plt.scatter(combined_data_csection["Neonatal mortality rate (per 1000 live births)"],combined_data_csection["Births by caesarean section (%)"])
plt.xlabel("Neonatal mortality rate (per 1000 live births)")
plt.ylabel("Births by caesarean section (%)")
title = "Neonatal Mortality Rate vs. Percentage of Births by Caesarean Section"
plt.title('\n'.join(wrap(title,60)))
plt.show()

plt.scatter(combined_data_personnel["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"],combined_data_personnel["Births attended by skilled health personnel (%)"])
plt.xlabel("Infant mortality rate (probabilityplt.title('\n'.join(wrap(title,60))) of dying between birth and age 1 per 1000 live births)")
plt.ylabel("Births attended by skilled health personnel (%)")
title = "Infant Mortality Rate vs. Percentage of Births Attended by Skilled Health Personnel"
plt.title('\n'.join(wrap(title,60)))
plt.show()

plt.scatter(combined_data_personnel["Neonatal mortality rate (per 1000 live births)"],combined_data_personnel["Births attended by skilled health personnel (%)"])
plt.xlabel("Neonatal mortality rate (per 1000 live births)")
plt.ylabel("Births attended by skilled health personnel (%)")
title = "Neonatal Mortality Rate vs. Percentage of Births Attended by Skilled Health Personnel"
plt.title('\n'.join(wrap(title,60)))
plt.show()

plt.scatter(combined_data_antenatal["Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)"],combined_data_antenatal["Antenatal care coverage - at least four visits (%)"])
plt.xlabel("Infant mortality rate (probability of dying between birth and age 1 per 1000 live births)")
plt.ylabel("Antenatal care coverage - at least four visits (%)")
title = "Infant Mortality Rate vs. Percentage of Women Receiving Antenatal Care"
plt.title('\n'.join(wrap(title,60)))
plt.show()

plt.scatter(combined_data_antenatal["Neonatal mortality rate (per 1000 live births)"],combined_data_antenatal["Antenatal care coverage - at least four visits (%)"])
plt.xlabel("Neonatal mortality rate (per 1000 live births)")
plt.ylabel("Antenatal care coverage - at least four visits (%)")
title = "Neonatal Mortality Rate vs. Percentage of Women Receiving Antenatal Care"
plt.title('\n'.join(wrap(title,60)))
plt.show()
