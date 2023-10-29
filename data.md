# СТРУКТУРА ДАТАСЕТА
Датасет состоит из пересечения двух публичных датасетов - COCO и VisualGenome и содержит 50 тыс. наблюдений.
Для каждого наблюдения существуют следующие параметры:

``image_id`` - уникальный id изображения из visual_genome <br>
``coco_id`` - уникальный id изображения из coco <br>
``annt_id`` - номер аннотации (1-5)<br>
``objects``<br>
``attributes``<br>
``relationships``<br>
``regional descriptions``<br>

## COCO
Из датасета COCO были взяты аннотации к изображением. Каждое изображение содержит 5 вариаций аннотаций. Планируется из 5 аннотаций оставить одно с наибольшим кол-вом различных частей речи.

## VisualGenome 
Были использованы следующие части датасета:
- objects_v1.2.0
- attributes_v1.2.0
- regional descriptions_v1.2.0
- relationships_v1.2.0

Все примеры ниже произведены для ![этого изображения](https://huggingface.co/datasets/visual_genome/viewer/attributes_v1.2.0?row=0&image-viewer=image-0-0CC2DCEE6FA307D330BD85DD3826A9B055277CE1):


### 1. Objects 
``object_id``: уникальный id объекта <br>
``names``: список имен, ассоциированных с объектом<br>
``synsets``: список WordNet synsets [прочитать, что это такое](https://www.tutorialspoint.com/synsets-for-a-word-in-wordnet-in-nlp) <br>

*Пример:*

```
[{
    "object_id": 1058498,
    "names": [ "clock" ], 
    "synsets": [ "clock.n.01" ], 
    }, 
{
    "object_id": 5046,
    "names": [ "street" ],
    "synsets": [ "street.n.01" ] 
    },
{
    "object_id": 5045,
    "names": [ "shade" ],
    "synsets": [ "shade.n.01" ]}, 
{
    "object_id": 1058529, 
    "names": [ "man" ],
    "synsets": [ "man.n.01" ]},
{
    "object_id": 5048, 
    "names": [ "sneakers" ],
    "synsets": [ "gym_shoe.n.01" ]}, 
    
    ...

]
```

### 2. Attributes
По смыслу это:
- прилагательные (какой?)<br>
> **tall** building
- (какого рода?)<br>
> **apartment** building

<br>

Структура:

*часть описывающая **объект**:*<br>

``object_id``: уникальный id объекта<br>
``names``: список имен, ассоциированных с объектом<br>
``synsets``: список WordNet synsets<br>

*часть, описывающая **атрибуты** объекта:*<br>

``attributes``: список атрибутов объекта

*Пример:*
```
[{
    "object_id": 1058498, 
    "names": [ "clock" ],
    "synsets": [ "clock.n.01" ],
    "attributes": [ "green", "tall" ]},
{
    "object_id": 5046,
    "names": [ "street" ],
    "synsets": [ "street.n.01" ],
    "attributes": [ "sidewalk" ]},
{
     "object_id": 5045, 
     "names": [ "shade" ],
     "synsets": [ "shade.n.01" ],
     "attributes": null },
{
    "object_id": 1058529,
    "names": [ "man" ], 
    "synsets": [ "man.n.01" ],
    "attributes": null }, 
{
    "object_id": 5048,
    "names": [ "sneakers" ],
    "synsets": [ "gym_shoe.n.01" ],
    "attributes": [ "grey" ]}, 
{
    "object_id": 5050, 
    "names": [ "headlight" ],
    "synsets": [ "headlight.n.01" ],
    "attributes": [ "off" ]}

    ...

]
```

### 2. Relationships
Глаголы и глагольные производные, описывающие связь объект-субъект. <br>
Объект и субъект - это ``objects``.

> street sign **shows** miles

<mark> НЕ ЯСНО: все ли объекты и субъекты содержаться в objects?

<br>

Структура:

``relationship_id``: уникальный id связи/отношения

*часть, описывающая **объект**:*

``object_id``: уникальный id объекта<br>
``names``: список имен, ассоциированных с объектом<br>
``synsets``: список WordNet synsets<br>

*часть, описывающая **субъект**:*

``object_id``: уникальный id объекта<br>
``names``: список имен, ассоциированных с объектом<br>
``synsets``: список WordNet synsets<br>

``predicate``: предикат, описывающий отношения между субъектом и объектом 

*Пример:*
```
[{
    "relationship_id": 15927, 
    "predicate": "ON", 
    "synsets": "['along.r.01']", 
    "subject": 
        { "object_id": 5045, 
        "names": [ "shade" ], 
        "synsets": [ "shade.n.01" ]}, 
    "object": 
        { "object_id": 5046, 
        "names": [ "street" ], 
        "synsets": [ "street.n.01" ]}}, 
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
        "synsets": [ "gym_shoe.n.01" ]}}, 
{ 
    "relationship_id": 15929, 
    "predicate": "has", 
    "synsets": "['have.v.01']", 
    "subject": 
        {"object_id": 5049, 
        "names": [ "car" ], 
        "synsets": [ "car.n.01" ]}, 
    "object": 
        {"object_id": 5050, 
        "names": [ "headlight" ], 
        "synsets": [ "headlight.n.01" ] }}, 
{ 
    "relationship_id": 15930, 
    "predicate": "ON", 
    "synsets": "['along.r.01']", 
    "subject": 
        {"object_id": 1058507, 
        "names": [ "sign" ], 
        "synsets": [ "sign.n.02" ] }, 
    "object": 
        { "object_id": 1058508, 
        "names": [ "building" ], 
        "synsets": [ "building.n.01" ] } }
]
```


### 2. Region description

``region_id`` - ??<br>
``image_id`` - ??<br>
``phrase``: фраза описывающая регион
<hr>

*пример:*

```
[{
    "region_id": 1382, 
    "image_id": 1, 
    "phrase": "the clock is green in colour"}, 
{ 
    "region_id": 1383, 
    "image_id": 1, 
    "phrase": "shade is along the street "}, 
{
    "region_id": 1384, 
    "image_id": 1, 
    "phrase": "man is wearing sneakers"}, 
{ 
    "region_id": 1385,
    "image_id": 1,
    "phrase": "cars headlights are off"}
]
```

# Итого
Мы **НЕ** имеем:
- positions
- background

Предлагаю пересмотреть output: <br>

```
{
    'background': 'лес', 
    'objects': ['девушка', 'цветок', 'магия'], 
    'positions': ['центр', 'в руке человека', 'везде'] 'obj_descriptions': 
        {'1': ['зеленые глаза', 'рыжие волосы', 'улыбка'], 
        '2' : ['фиолетовый', 'в руке'], 
        '3' : []
        }
}
```
У нас нет разметки для фона, но фон вполне может оказаться в объектах, тогда возникает вопрос - как его выделить? 

У нас нет разметки для ``positions``, зато у нас есть ``relationships``

В ``obj_descriptions`` содержатся не только прилагательные и описательные слова, поэтому ``obj_descriptions`` не равно нашему ``attributes``.
Например, у них описанием цветка является "в руке", у нас эта информация будет содержаться в ``relationships``
аналогично, "рыжие волосы" у них - описание девушки, у нас "волосы" - это отдельный объект, а "рыжие" - их атрибут.
Если мы хотим аутпут, как выше, имеет смысл рассмотреть такую цепочку:
С помощью ``relationships`` определить субъект (девушка) и объект (волосы) (через предикат has мб?)  и далее скокатить объект (волосы) с его атрибутом (рыжие) и в итое получим такой итоговый набор:

объект - "девушка"<br>
атрибут - "рыжие волосы"<br>

Но как понять, что объект первостепенен (девушка), ведь суммарно объектов очень много..

МЫ МОЖЕМ
1. объекты (по смыслу субъект)
2. список объектов, которые связаны с субъектами
3. предикаты, с помощью которых они связаны
4. атрибуты каждого объекта

вот далее мы это можем уже **каким-то образом** преобразовать в следующий вид:

```
{
    'background': 'лес', 
    'objects': ['девушка', 'цветок', 'магия'], 
    'positions': ['центр', 'в руке человека', 'везде'] 'obj_descriptions': 
        {'1': ['зеленые глаза', 'рыжие волосы', 'улыбка'], 
        '2' : ['фиолетовый', 'в руке'], 
        '3' : []
        }
}
```