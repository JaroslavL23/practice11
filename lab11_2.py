import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Завантаження даних із CSV-файлу у датафрейм
df = pd.read_csv('comptage_velo_2019.csv')

#Вивід основних характеристик датафрейму
print(df.head())
print(df.info())
print(df.describe())

#Визначення та вивід загальної кількість велосипедистів за рік на усіх велодоріжках
print()
print("Загальна кількість велосипедистів за рік на усіх велодоріжках:")
print(" ",df["nb_passages"].sum())
# Групування за ідентифікаторами велодоріжок
# та підрахунок загальної кількості велосипедистів на кожній велодоріжці
pass_sum = df.groupby("id_compteur")["nb_passages"].sum()

#Вивід загальної кількість велосипедистів за рік на кожній велодоріжці
print("Загальна кількість велосипедистів за рік на кожній велодоріжці:")
print(pass_sum,"\n")

print("Найбільш популярний місяць у велосипедистів, на кожній з трьох з обраних велодоріжок.")
#Вибір трьох id велодоріжок із датафрейму в масив
ids = [df.iloc[1]["id_compteur"], df.iloc[2]["id_compteur"], df.iloc[3]["id_compteur"]]
#Копіюємо три велодоріжки за id в датафрейму
df_selected = df[df["id_compteur"].isin(ids)].copy()
#Створення стовпця місяця та перетворення його у формат datetime
df_selected["month"] = df_selected["date"]
df_selected["month"] = pd.to_datetime(df_selected["month"]).dt.month
#Групування по id велодоріжки та місяцю + підрахунок сумарних проходів nb_passages 
df_month = df_selected.groupby(["id_compteur", "month"])["nb_passages"].sum().reset_index()
#Визначення максимального значення проходів nb_passages по кожній велодоріжці
df_max = df_month.groupby(["id_compteur"])["nb_passages"].max().reset_index()
#Отримання рядків з місяцям, що відповідають максимальним значенням nb_passages  
df_res = df_month[(df_month["nb_passages"].isin(df_max["nb_passages"]))]
#Виведення на екран місяць найбільш популярний у велосипедистів, на кожній з  трьох з обраних велодоріжок
print(df_res)

print(f"\nГрафік завантаженості однієї з велодоріжок({ids[0]}) по місяцям")
#Отимуємо дані для відображення по першій велодоріжці зі списку
df_print = df_selected[df_selected["id_compteur"] == ids[0]]
#Групування по місяцю суми проходів nb_passages для графіка
df_month_count = df_month.groupby("month")["nb_passages"].sum().reset_index()
#Побудова графіка завантаженості однієї з обраних велодоріжок
plt.figure(figsize=(7,7))
plt.plot(df_month_count)
plt.title(f"Завантаженість за рік велодоріжки {ids[0]}")
plt.xlabel("Номер місяця")
plt.ylabel("Кількість")
plt.show()

