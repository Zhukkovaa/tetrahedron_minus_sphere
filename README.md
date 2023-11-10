# Вращение фигуры "Тетраэдр минус сфера" с заданной угловой скоростью
[![Build, Test](https://github.com/Zhukkovaa/tetrahedron__minus__sphere/actions/workflows/python-app.yml/badge.svg)](https://github.com/Zhukkovaa/tetrahedron__minus__sphere/actions/workflows/python-app.yml)
[![License: MIT ](https://img.shields.io/badge/License-MIT-coral.svg)](https://opensource.org/licenses/MIT)
[![GitHub release](https://img.shields.io/github/release/Zhukkovaa/tetrahedron__minus__sphere.svg?color=pink)](https://github.com/Zhukkovaa/tetrahedron__minus__sphere/releases)
# Лабораторная работа по дисциплине "Компьютерная графика" №5. 
# Описание задачи
Вариант 14. Напишите программу, отображающую тетраэдр минус сфера. Предусмотрите возможность поворота тела вокруг основных осей.
### Демонстрация работоспособности программы
![Анимация](https://github.com/Zhukkovaa/tetrahedron__minus__sphere/blob/main/data/giffochka.gif)

## Используемые библиотеки
* pygame: Библиотека для разработки компьютерных игр и мультимедийных приложений. 
  Она предоставляет функции для работы с графикой, звуком, вводом устройств и другими аспектами, необходимыми для создания игр.
* OpenGL.GL: Модуль, который предоставляет прямой доступ к функциям и константам OpenGL для работы с 3D-графикой.
* OpenGL.GLU: Модуль, который предоставляет функции утилиты OpenGL (GLU), такие как создание и управление матрицами проекции 
  и моделирования, примитивами рисования и другими функциями упрощения работы с OpenGL.


## Описание реализации
Конечная цель - создать эффект вырезания сферы из тетраэдра при отображении на экране.

В коде используется буфер трафарета (stencil buffer), который представляет собой дополнительный буфер, содержащий значения 
для каждого пикселя экрана. Буфер трафарета использован для определения областей, в которых будут отрисовываться объекты.

Для достижения конечной цели выполняется следующее:
1. ```На экране рисуется тетраэдр, и каждый пиксель в его области помечается значением 1 в буфере трафарета;```
2. ```На экране рисуется, и каждый пиксель в её области помечается значением 2 в буфере трафарета;``` 
3. ```Устанавливается функция тестирования трафарета, которая проверяет, равно ли значение буфера трафарета 1.
   И тетраэдр рисуется только в области, где значение буфера трафарета равно 1; ```
4. ```При отображении результата будет виден только тетраэдр в области, где значение буфера трафарета равно 1, а сфера будет вырезана.```

## Инструкции по использованию
После запуска программы Вы можете вращать объект на экране с помощью клавиш со стрелками на клавиатуре. 
* Стрелка влево: Вращение объекта против часовой стрелки вокруг вертикальной оси.
* Стрелка вправо: Вращение объекта по часовой стрелке вокруг вертикальной оси.
* Стрелка вверх: Вращение объекта вперед вокруг горизонтальной оси.
* Стрелка вниз: Вращение объекта назад вокруг горизонтальной оси.

## Установка и запуск:
1. ```git clone https://github.com/Zhukkovaa/tetrahedron__minus__sphere.git```
2. ```cd tetrahedron__minus__sphere```
3. ```pip install -r requirements.txt```
4. ```pip install PyOpenGL PyOpenGL-accelerate```
5. ```python src/main.py```

