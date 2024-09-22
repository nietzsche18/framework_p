import pandas as pd

# Liste des noms de fichiers CSV
#csv_files = [r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat1_s.csv", r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat1.csv", r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat2_s.csv", r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat2.csv",r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat3_s.csv", r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat3.csv",]
csv_files = [r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat1.csv",r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat3_s.csv", r"C:\Users\33670\Desktop\framework\backtest\data\trades\final_df_strat3.csv",]

# Liste pour stocker les DataFrames chargés à partir des fichiers CSV
dataframes = []

# Charger chaque fichier CSV dans un DataFrame et les stocker dans la liste
for file in csv_files:
    df = pd.read_csv(file)
    dataframes.append(df)

# Concaténer les DataFrames en un seul
consolidated_df = pd.concat(dataframes, ignore_index=True)

# Enregistrer le DataFrame consolidé dans un nouveau fichier CSV
consolidated_df.to_csv("consolidated.csv", index=False)

print("Les fichiers CSV ont été consolidés avec succès en 'consolidated.csv'.")
