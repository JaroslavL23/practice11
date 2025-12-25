import pandas as pd

#Задання словника погоди за місяць із лаб5
weather = {"month":["September", "September", "September", "December", "December", "Feb", "Feb"],
    "temp": [40, 10, 23, 10, 0, -11, -3],"opad": [150, 40, 1, 80, 20, 10, 110]}
#Перетворення словника weather у DataFrame
df = pd.DataFrame(weather)

#Виведення датафрейму на екран
print("Створений dataFrame:\n",df,"\n")
#Виведення перших 3-х рядків датафрейму
df.head(3)
#Виведення типу даних датафрейму, розмірність таблиці та описової статистики
print("Типи даних:\n", df.dtypes)
print("\nКількість рядків і стовпців:", df.shape, "\n")
print("Описова статистика:\n", df.describe())

#Задання нового стовпця для датафрейму
df["diff"] = df["opad"]-df["temp"]
print("\nПісля додавання нового стовпця\n", df)

#Фільтрація рядків, де опади більші за температуру
df_filt = df[df["diff"] > 0].reset_index()
print("\nПісля фільтрації\n", df_filt)

#Сортування від найменшого значення diff до найбільшого
df_sort = df_filt.sort_values(by="diff")
print("\nПісля сортування за зростанням\n", df_sort)

#Групування за місяцями і обчислення середнього значення температури
df_grp_mean = df_sort.groupby(["month"])["temp"].mean()
print("\nCереднє значення температури за місяць:\n", df_grp_mean)

#Групування за місяцями і визначення максимальних опадів
df_grp_max = df_sort.groupby(["month"])["opad"].max()
print("\nМаксимальна кількість опадів за місяць:\n", df_grp_max)

#Визначення кількості унікальних значень температури після фільтрації
df_uniq = df_sort["temp"].nunique()
print("\nКількість унікальних температур =", df_uniq)
