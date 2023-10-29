# Проект "Выделение деталей из текста на русском языке, описывающего изображение, методами МО"

### Студенты:
Гераськина Надежда

Есипов Иван

Машковцева Полина

Горбатова Татьяна

### Руководитель: 
Полянская Анна

## 1. Описание данных
## 2. План работ
### 2.1. Разведочный анализ данных и первичная аналитика данных
В данном блоке мы планиурем выполнить следующие задачи:
1. Количественный анализ:
   * сколько слов, предложений в нашем наборе данных;
   * какой длины предложения (в смысле количества слов: общее и по частям речи);
   * средняя длина слов;
   * среднее количество слов в предложениях, подающихся на ввод;
   * среднее количество предложений в тексте, подающемся на ввод;
   * распределение числа предложений по количеству слов в них.
2. Анализ встречаемости:
   * топ встречаемых слов в Input и в output;
   * топ встречаемых словосочетаний (n_grams).
   
Для выполнения вышеперечисленных задач необходимо провести:
* предобработку данных : лемматизацию, возможно удаление стоп-слов;
* построение гистограмм и графиков.

В итоге, после успешного прохождения данного этапа мы сможем:
1. Выявить потенциальные стоп-слова;
2. Определить средний размер текста, подаюегося на вход модели;
3. Понять характер данных, с которыми мы будем в дальнейшем работать

### 2.2. Этап ML
### 2.3. Этап DL
Наша модель будет делать relation prediction

Предполагаемые задачи:
1. One-hot encoding
2. Обучение LSTM-подобной неройнной сети
3. Изучение Embedding слоев в нейронных сетях Transformer
4. Обучение BERT нейронных сетей (планируется изучение и сравнение 4-ех моделей из семейства BERT в формате хакатона)
   
[Про relation prediction](https://towardsdatascience.com/nlp-deep-learning-for-relation-extraction-9c5d13110afa)

### 2.4. Хотим сделать, но не успеем
1. Аугментация данных: изменение входных текстов
2. Подавать на вход текст где описания содержатся в разных предложениях - coreference resolution (возможно МЛ)

## 3. Итоговый продукт
Наша цель: реализовать веб-сервис, который будет иметь следующие функции:
1. 

Архитектура нашего сервиса планируется следующая:
![Project drawio](https://github.com/NGeraskina/nlp_project_MOVS/assets/35665662/4e927bd1-d0a4-4c60-89c2-e2599b20b38c)
Подробнее о сервисе можно почитать [в данном документе](https://github.com/NLP-team-MOVS2023/nlp_project_MOVS/blob/main/service.md)
## 4. Техническая реализация проекта
Для реализации проекта нам будут необходимы:
1. PostgreSQL база данных
2. MlFlow сервер
3. Airflow сервер
4. Сервер для деплоя веб-сервиса
