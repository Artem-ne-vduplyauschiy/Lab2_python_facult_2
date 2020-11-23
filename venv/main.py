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
            a = input('Регион: ')
            print(df.loc[df['ГОРОД/РЕГИОН '] == a])  # 3
            b = int(input('Введите число: '))
            if any(b >= df['ЧИСЛО ЗАБОЛЕВШИХ']) & any(b <= df['ЧИСЛО ЗАБОЛЕВШИХ']):
                print(df.loc[df['ЧИСЛО ЗАБОЛЕВШИХ'] > b])  # 4
            a = df.sort_values(by=['ЧИСЛО ЗАБОЛЕВШИХ'], ascending=False).head()
            b = df.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ'], ascending=False).head()
            c = df.sort_values(by=['ЧИСЛО УМЕРШИХ'], ascending=False).head()
            d = df.sort_values(by=['ЧИСЛО ЗАБОЛЕВШИХ']).head()
            e = df.sort_values(by=['ЧИСЛО ВЫЗДОРОВЕВШИХ']).head()
            f = df.sort_values(by=['ЧИСЛО УМЕРШИХ']).head()
            print('Tоп-5 регионов с максимальным числом заболевших\n', a)  # 5...
            print('Tоп-5 регионов с максимальным числом выздоровевших\n', b)
            print('Tоп-5 регионов с максимальным числом умерших\n', c)
            print('Tоп-5 регионов с минимальным числом заболевших\n', d)
            print('Tоп-5 регионов с минимальным числом выздоровевших\n', e)
            print('Tоп-5 регионов с минимальным числом умерших\n', f)  # ...5

            gridsize = (3, 2)  # 6...
            fig = plt.figure(figsize=(35, 16))  # В юпитерноутбуке вывод норм здесь не очень. Возможно нужно подогнать эти цифери
            # pl.xticks(range(5), xTicks, rotation=60)  # Не знаю как повернуть подписи оси х чтоб компактнее было
            ax1 = plt.subplot2grid(gridsize, (0, 0))
            ax1.set_title('Tоп-5 регионов с максимальным числом заболевших')
            ax1.bar(a['ГОРОД/РЕГИОН '].values, a['ЧИСЛО ЗАБОЛЕВШИХ'])
            ax2 = plt.subplot2grid(gridsize, (0, 1))
            ax2.set_title('Tоп-5 регионов с максимальным числом выздоровевших')
            ax2.bar(b['ГОРОД/РЕГИОН '].values, b['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
            ax3 = plt.subplot2grid(gridsize, (1, 0))
            ax3.set_title('Tоп-5 регионов с максимальным числом умерших')
            ax3.bar(c['ГОРОД/РЕГИОН '].values, c['ЧИСЛО УМЕРШИХ'])
            ax4 = plt.subplot2grid(gridsize, (1, 1))
            ax4.set_title('Tоп-5 регионов с минимальным числом заболевших')
            ax4.bar(d['ГОРОД/РЕГИОН '].values, d['ЧИСЛО ЗАБОЛЕВШИХ'])
            ax5 = plt.subplot2grid(gridsize, (2, 0))
            ax5.set_title('Tоп-5 регионов с минимальным числом выздоровевших')
            ax5.bar(e['ГОРОД/РЕГИОН '].values, e['ЧИСЛО ВЫЗДОРОВЕВШИХ'])
            ax6 = plt.subplot2grid(gridsize, (2, 1))
            ax6.set_title('Tоп-5 регионов с минимальным числом умерших')
            ax6.bar(f['ГОРОД/РЕГИОН '].values, f['ЧИСЛО УМЕРШИХ'])
            plt.show()# ...6
        else:
            print('Файл не найден')
    else:
        print('Файл не найден')
