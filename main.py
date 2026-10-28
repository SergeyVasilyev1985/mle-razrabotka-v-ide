# Импортируем pandas
import pandas as pd
# Импортируем наш класс
from src.reporter import DataFrameReporter

def main():
    #Загружаем Dataset
    data = pd.read_csv('data/payments.csv')
    
    # Создаем тестовые объекты
    reporter_1 = DataFrameReporter(float_format = '0.02f', percent_format = '0.03f')
    reporter_2 = DataFrameReporter(float_format = '0.03f', percent_format = '0.01f', include_all = True)

    # выводим результат работы класса через созданный метод
    reporter_1.show_report(data, 'Отчет в формате 1:')
    print()
    reporter_2.show_report(data, 'Отчет в формате 2:')


# вызов функции:
if __name__ == "__main__":
    main()