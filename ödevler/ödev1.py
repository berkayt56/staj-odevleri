import pandas as pd

csv_path = r"C:\Users\toprak\Desktop\iris.data" #dataset yolu

csv_data = pd.read_csv(csv_path, delimiter=",", header=None) #dataset okuma
smp_csv_data = csv_data.sample(frac=1) #dataset karıştırma

smp_csv_data[4] = smp_csv_data[4].replace("Iris-setosa", "1")
smp_csv_data[4] = smp_csv_data[4].replace("Iris-virginica", "2")
smp_csv_data[4] = smp_csv_data[4].replace("Iris-versicolor", "3") #değerleri değiştirme

excel_path = r"C:\Users\toprak\Desktop\updateiriss.xlsx" #oluşacak dosyanın yolu
smp_csv_data.to_excel(excel_path, index=False) #excele çevirme