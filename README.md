# Проект "Выделение деталей из текста на русском языке, описывающего изображение, методами МО"

### Студенты:
Гераськина Надежда

Есипов Иван

Машковцева Полина

Горбатова Татьяна

### Руководитель: 
Полянская Анна

## 1. Описание данных

Язык данных: английский

Датасет состоит из пересечения двух публичных датасетов - [COCO](https://cocodataset.org/#home) и [Visual Genome](https://homes.cs.washington.edu/~ranjay/visualgenome/index.html) и содержит 49312 наблюдений.
Данные в формате pickle доступны для скачивания по [ссылке](https://drive.google.com/file/d/1KTq20OiwUeXSc1KCu2tnmwcMk0qoY2_w/view?usp=sharing).

* Из датасета COCO были взяты аннотации к изображениям. Каждое изображение содержит 5 вариаций аннотаций. Планируется из 5 аннотаций оставить одно с наибольшим кол-вом различных частей речи (будет сделано после разведочного анализа даных).
* Visual Genome содержит информацию об объектах на изображениях, их атрибутах и отношениях между объектами. Были использованы следующие части Visual Genome:
  -   objects_v1.2.0
  -   attributes_v1.2.0
  -   regional descriptions_v1.2.0
  -   relationships_v1.2.0

Для каждого наблюдения существуют следующие параметры:

* ``image_id`` - уникальный id изображения из visual_genome <br>
* ``coco_id`` - уникальный id изображения из coco <br>

Параметры объектов на картинке (объектов и субъектов в описании):
* ``object_id`` - уникальный id объекта
* ``names`` - список имен, ассоциированных с объектом<br>
* ``synsets`` - список синсетов [WordNet](https://www.tutorialspoint.com/synsets-for-a-word-in-wordnet-in-nlp)

 Параметры атрибутов объектов:
* ``attributes`` - список атрибутов

Параметры отношений между объектами:
* ``relationship_id`` - уникальный id связи/отношения
* ``predicate`` - предикат, описывающий отношения между объектами (субъектом и объектом)

Структура _objects_v1.2.0_:
* ``object_id``
* ``names``
* ``synsets``

*Пример:*
```
{
    "object_id": 1058498,
    "names": [ "clock" ], 
    "synsets": [ "clock.n.01" ]
}
```

Структура _attributes_v1.2.0_:
* ``object_id``
* ``names``
* ``synsets``
* ``attributes``

*Пример:*
```
{
    "object_id": 1058498, 
    "names": [ "clock" ],
    "synsets": [ "clock.n.01" ],
    "attributes": [ "green", "tall" ]
}
```

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
```
{
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
        "synsets": [ "gym_shoe.n.01" ]}
}
```


Структура _regional descriptions_v1.2.0_:
* ``region_id`` - уникальный id региона
* ``image_id`` - уникальный id изображения (соответсвует vg_id)
* ``phrase``: фраза, описывающая регион

_Пример:_
```
{
    "region_id": 1382, 
    "image_id": 1, 
    "phrase": "the clock is green in colour"
}
```

Более подробное описание датасета представлено [здесь](https://github.com/NLP-team-MOVS2023/nlp_project_MOVS/edit/main/data.md).

## 2. План работ
### 2.1. Разведочный анализ данных и первичная аналитика данных
В данном блоке мы планируем выполнить следующие задачи:
1. **Количественный анализ**:
   * сколько слов, предложений в нашем наборе данных;
   * какой длины предложения (в смысле количества слов: общее и по частям речи);
   * средняя длина слов;
   * среднее количество слов в предложениях, подающихся на ввод;
   * распределение числа предложений по количеству слов в них (общее и по частям речи).
2. **Анализ встречаемости**:
   * топ встречаемых слов в Input и в Output;
   * топ встречаемых словосочетаний (n_grams).
   
Для выполнения вышеперечисленных задач необходимо провести:
* предобработку данных : лемматизацию, возможно удаление стоп-слов и стемминг;
* построение гистограмм и графиков.

**В итоге**, после успешного прохождения данного этапа мы сможем:
1. Выявить потенциальные стоп-слова для нашей задачи;
2. Определить средний размер текста (предложения), подаюегося на вход модели;
3. Понять характер данных, с которыми мы будем в дальнейшем работать;
4. Выбрать один из пяти annt_id.

### 2.2. Этап ML

Предполагаемые задачи:
1. POS-разметка ([предобученными моделями](https://journalofbigdata.springeropen.com/articles/10.1186/s40537-022-00561-y) - HMM, CRF, Наивный Байес, SVM) и One-hot encoding исходных текстов
2. Попытка relation extraction при помощи ML-классификатора (RandomForest, KNeighborsClassifier, AdaBoostClassifier, CatBoostingClassifier, Support Vector Machine)
3. Попытка [PCA](https://medium.com/@yashj302/principal-component-analysis-pca-nlp-python-ce9caa58bd7a) для входных данных
   
### 2.3. Этап DL

Наша модель будет делать **relation extraction**

Предполагаемые задачи:
1. Необходимая предобработка данных (из ML части в том числе) 
2. Изучение Embedding слоев в нейронных сетях
3. Обучение LSTM-подобной нейронной сети
4. Обучение BERT нейронных сетей (планируется изучение и сравнение минимум 4-ех моделей из семейства BERT в формате хакатона)

### 2.4. Хотим сделать, но не успеем
1. Аугментация данных: изменение входных текстов ([Back Translation](https://amitness.com/2020/02/back-translation-in-google-sheets/), [Easy Data Augmentation](https://github.com/jasonwei20/eda_nlp), [NLP Aug](https://github.com/makcedward/nlpaug), [прочее](https://neptune.ai/blog/data-augmentation-nlp))
2. Подавать на вход текст, где описания содержатся в разных предложениях - [coreference resolution](http://nlpprogress.com/english/coreference_resolution.html)
3. [NER](http://nlpprogress.com/english/named_entity_recognition.html)-подобная разметка для объектов, атрибутов и отношений между ними
4. Предсказание количества объектов на картинке по ее описанию - для этого отдельным признаком нужно добавить количество объектов

## 3. Итоговый продукт

Наша цель: реализовать веб-сервис, который будет иметь следующие функции:

1. Принимать на вход текстовую информацию;
2. Выводить текст с визуальной разметкой субъектов, объектов, их атрибутов и отношений между ними;
3. Предоставлять пользователю возможность выгружать размеченный текст в формате json. Пример выгрузки:
```
{
"background": "forest",
"objects": ["girl", "flower", "magic"],
"positions": ["center", "in human hand", "everywhere"]
"obj_descriptions": {
  "1": ["green eyes", "blond hair", "smile"],
  "2": ["purple"],
  "3": []
  }
}
```

Архитектура нашего сервиса планируется следующая:
![Project drawio](https://github.com/NGeraskina/nlp_project_MOVS/assets/35665662/4e927bd1-d0a4-4c60-89c2-e2599b20b38c)

Подробнее о сервисе можно почитать [в данном документе](https://github.com/NLP-team-MOVS2023/nlp_project_MOVS/blob/main/service.md)

## 4. Техническая реализация проекта
Для реализации проекта нам будут необходимы:
1. PostgreSQL база данных;
2. MlFlow сервер;
3. Airflow сервер;
4. Сервер для деплоя веб-сервиса;
5. Бакет на хранилище S3 от Яндекса.

Первичная схема пайплайна обучена планируется следующая:

![Pipeline](https://github.com/NLP-team-MOVS2023/nlp_project_MOVS/blob/main/assets/pipeline.drawio.svg)
