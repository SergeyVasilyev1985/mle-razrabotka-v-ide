# mle-razrabotka-v-ide
## Описание проекта
Создан класс-инструмент `DataFrameReporter`, который может многократно переиспользоваться. Его можно подключать к разным проектам и создавать на его основе объекты для анализа любых новых датасетов.

Метод `show_report` для отчета:

   - принимает следующие переметры: Датасет, title (по умолчанию None)
   - выводит информацию:
       - Количество столбцов
       - количество строк 
       - количество дубликатов,
       - доля дубликатов
       - сводная статистика - принимает на вход include_all = True или False
       - количество пропусков
       - доля пропусков

Пример использования:
   - создать объект -  
```reporter = DataFrameReporter(float_format = '0.03f', percent_format = '0.01f', include_all = True)```
             Значения по умолчанию - float_format = '0.05f', percent_format = '0.02f', include_all = False

   - Вызов метода - 
```reporter.show_report(data, 'title:')```
        - data - Ваш Датафрейм
        - 'title' - заголовок

## Установка 
   Python версия 3.9+ 

Клонирование проекта

```git clone https://github.com/SergeyVasilyev1985/mle-razrabotka-v-ide```

```cd <Ваш/путь>```

Cоздание виртуального окружения

```python3 -m venv venv```

активация окружения

```source venv/Scripts/activate` или `.venv/Scripts/activate```- для Windows

```source venv/bin/activate`  или `.venv/bin/activate``` - для MacOS и Linux

установка библтотек

```pip install -r requirements.txt```

## Запуск проекта

```python3 main.py```

## Структура проекта:

 
```
├─ data/
│  ├─ payments.csv
│  ├─ README.md
├─ src/
│  ├─ reporter.py
│  ├─ README.md
├─ .gitignore
├─ main.py
├─ README.md
├─  requirements.txt
```