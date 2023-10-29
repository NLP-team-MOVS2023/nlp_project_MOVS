# Проект "Выделение деталей из текста на русском языке, описывающего изображение, методами МО"

### Студенты:
Гераськина Надежда

Есипов Иван

Машковцева Полина

Горбатова Татьяна

### Руководитель: 
Полянская Анна

## 1. Описание данных

Датасет состоит из пересечения двух публичных датасетов - [COCO](https://cocodataset.org/#home) и [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) и содержит 50 тыс. наблюдений.
* Из датасета COCO были взяты аннотации к изображением. Каждое изображение содержит 5 вариаций аннотаций. Планируется из 5 аннотаций оставить одно с наибольшим кол-вом различных частей речи.
* Visual Genome содержит информацию об объектах на изображениях, их атрибутах и отношениях между объектами. Были использованы следующие части Visual Genome:
  -   objects_v1.2.0
  -   attributes_v1.2.0
  -   regional descriptions_v1.2.0
  -   relationships_v1.2.0

Для каждого наблюдения существуют следующие параметры:

* ``image_id`` - уникальный id изображения из visual_genome <br>
* ``coco_id`` - уникальный id изображения из coco <br>
* ``annt_id`` - номер аннотации (1-5)<br>

Параметры объектов на картинке (объектов и субъектов в описании):
* ``objects`` - уникальный id объекта
* ``names``: список имен, ассоциированных с объектом<br>
* ``synsets``: список синсетов [WordNet](https://www.tutorialspoint.com/synsets-for-a-word-in-wordnet-in-nlp)

 Параметры атрибутов объектов:
* ``attributes`` - список атрибутов

Параметры отношений между объектами:
* ``relationship_id``: уникальный id связи/отношения
* ``predicate``: предикат, описывающий отношения между объектами (субъектом и объектом)

Структура _objects_v1.2.0_:
* ``object_id``
* ``names``
* ``synsets``

Структура _attributes_v1.2.0_:
* ``object_id``
* ``names``
* ``synsets``
* ``attributes``

Структура _relationships_v1.2.0_:
* ``relationship_id``
* субъект:
  -   ``object_id``
  -   ``names``
  -   ``synsets``
* объект:
  -   ``object_id``
  -   ``names``
  -   ``synsets``
* ``predicate``

_Пример:_
```{
    "relationship_id": 15928, 
    "predicate": "wears", 
    "synsets": "['wear.v.01']", 
    "subject": 
        { "object_id": 1058529, 
        "names": [ "man" ], 
        "synsets": [ "man.n.01" ]}, 
    "object": 
        {"object_id": 5048, 
        "names": [ "sneakers" ], 
        "synsets": [ "gym_shoe.n.01" ]}}
```


Структура regional _descriptions_v1.2.0_:
* ``regional descriptions``<br>

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
   * топ встречаемых слов в Input и в Output;
   * топ встречаемых словосочетаний (n_grams).
   
Для выполнения вышеперечисленных задач необходимо провести:
* предобработку данных : лемматизацию, возможно удаление стоп-слов;
* построение гистограмм и графиков.

В итоге, после успешного прохождения данного этапа мы сможем:
1. Выявить потенциальные стоп-слова;
2. Определить средний размер текста, подаюегося на вход модели;
3. Понять характер данных, с которыми мы будем в дальнейшем работать

### 2.2. Этап ML

Предполагаемые задачи:
1. POS-разметка ([предобученными моделями](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-022-00561-y) - HMM, CRF, Наивный Байес, SVM) и One-hot encoding исходных текстов
2. Попытка relation extraction при помощи ML-классификатора (RandomForest, KNeighborsClassifier, AdaBoostClassifier, CatBoostingClassifier, Support Vector Machine)
3. [PCA](https://medium.com/@yashj302/principal-component-analysis-pca-nlp-python-ce9caa58bd7a) для входных данных
   
### 2.3. Этап DL

Наша модель будет делать relation extraction

Предполагаемые задачи:
1. Необходимая предобработка данных (из ML части в том числе) 
2. Изучение Embedding слоев в нейронных сетях
3. Обучение LSTM-подобной неройнной сети
4. Обучение BERT нейронных сетей (планируется изучение и сравнение минимум 4-ех моделей из семейства BERT в формате хакатона)
   
[Про relation prediction](https://towardsdatascience.com/nlp-deep-learning-for-relation-extraction-9c5d13110afa)

[Примеры relation extraction](https://nlpprogress.com/english/relationship_extraction.html)

[Обзор relation extraction](https://medium.com/@andreasherman/different-ways-of-doing-relation-extraction-from-text-7362b4c3169e)

### 2.4. Хотим сделать, но не успеем
1. Аугментация данных: изменение входных текстов ([Back Translation](https://amitness.com/2020/02/back-translation-in-google-sheets/), [Easy Data Augmentation](https://github.com/jasonwei20/eda_nlp), [NLP Aug](https://github.com/makcedward/nlpaug), [прочее](https://neptune.ai/blog/data-augmentation-nlp))
2. Подавать на вход текст где описания содержатся в разных предложениях - [coreference resolution](http://nlpprogress.com/english/coreference_resolution.html) (возможно МЛ)
3. [NER](http://nlpprogress.com/english/named_entity_recognition.html)-подобная разметка для объектов, атрибутов и отношений между ними
4. Предсказание количества объектов на картинке по ее описанию - для этого отдельным признаком добавить количество объектов (длина списка)

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
