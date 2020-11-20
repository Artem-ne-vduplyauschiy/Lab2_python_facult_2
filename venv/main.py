import numpy as np
import pandas as pd
from PIL import Image
import os
from matplotlib import pyplot as plt

path = input('Введите путь: ')
if path:
    if os.path.exists(path):
        df = None  # чтоб меньше ошибок выскакивало
        if path.endswith('.csv'):
            df = pd.read_csv(path)
        elif path.endswith('.xlsx'):
            df1 = pd.ExcelFile(path)
            print(df1.sheet_names)  # see all sheet names
            sheet_name = input('Введите лист из списка выше: ')
            if sheet_name in df1.sheet_names:
                df = pd.read_excel(path, sheet_name)  # read a specific sheet to DataFrame
            else:
                print('Неверный лист')
        else:
            print('Неверное расширение файла')
        if df is not None:
            print(df.columns, '\n', 'Столбцов: ', len(df.columns), '\n', df.dtypes, '\n', 'Строк: ', len(df.index))  # 2
            a = input('Region:')
            print(df.loc[df['ГОРОД/РЕГИОН '] == a])  # 3
            b = int(input('Введите число'))
            if any(b >= df['ЧИСЛО ЗАБОЛЕВШИХ']) & any(b <= df['ЧИСЛО ЗАБОЛЕВШИХ']):
                print(df.loc[df['ЧИСЛО ЗАБОЛЕВШИХ'] > b])  # 4
            print('\n', df.sort_values(by=['ЧИСЛО ЗАБОЛЕВШИХ'], ascending=False).head())  # 5...
            print('\n', df.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ'], ascending=False).head())
            print('\n', df.sort_values(by=['ЧИСЛО УМЕРШИХ'], ascending=False).head())
            print('\n', df.sort_values(by=['ЧИСЛО ЗАБОЛЕВШИХ']).head())
            print('\n', df.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ']).head())
            print('\n', df.sort_values(by=['ЧИСЛО УМЕРШИХ']).head())  # ...5
            fig, axs = plt.subplots(2, 3, sharey=True, tight_layout=True)  # 6...
            axs[0][0].hist(df['ЧИСЛО УМЕРШИХ'].sort_values().head())
            axs[0][1].hist(df['ЧИСЛО УМЕРШИХ'].sort_values().tail())
            axs[0][2].hist(df['ЧИСЛО ЗАБОЛЕВШИХ'].sort_values().head())
            axs[1][0].hist(df['ЧИСЛО ЗАБОЛЕВШИХ'].sort_values().tail())
            axs[1][1].hist(df['ЧИСЛО ВЫЗДОРОВЕВШИХ'].sort_values().head())
            axs[1][2].hist(df['ЧИСЛО ВЫЗДОРОВЕВШИХ'].sort_values().tail())  # ...6
        else:
            print('Файл не найден')
    else:
        print('Файл не найден')
