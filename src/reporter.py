class DataFrameReporter:
    def __init__(self, float_format = '0.05f', percent_format = '0.02%', include_all = False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    def show_report(self, df, title = None):
        if title:
            print(title)

        # Вывод количества строк и столбцов
        print('Количество столбцов:', df.shape[1])
        print('Количество строк:', df.shape[0])

        # Вывод количества дубликатов
        duplicates = df.duplicated().sum()
        print('Количество дубликатов:', duplicates)

        # Вывод доли дубликатов
        print('Доля дубликатов:', format(duplicates / df.shape[0], self.percent_format))

        # Вывод описательной статистики
        print(df.describe(include='all' if self.include_all else None))
        
        # вывод количества пропусков во всем датафрейме одним числом
        null_data = df.isna().sum().sum()
        print(f'Количество пропусков:', null_data)
        
        # вывод доли пропусков во всем датафрейме одним числом с плавающей точкой
        print('Доля пропусков:', format(null_data / df.size, self.float_format))

