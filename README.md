На прошлом уроке мы научились добавлять контент на сайт: текст, изображения и др. С помощью CSS мы сможем стилизоваь этот контент.

План урока:

Узнаем, что такое CSS и как он используется в веб-разработке.
Научимся стилизовать HTML.
Ознакомимся с основными понятиями CSS.
🧠 CSS (Cascading Style Sheets, т.е. каскадные таблицы стилей) — то язык стилей, используемый для описания внешнего вида и форматирования документов, написанных на HTML. CSS позволяет отделить содержание документа от его представления, что делает его веб-страницы более гибкими и лёгкими для обновления.

С помощью CSS можно не только поменять цвета и шрифты на сайте, но и расставить элементы, адаптировать сайт под разные устройства, сделать анимации и т.д.



Начнём работать с CSS. Варианты того, как можно записывать стили:

самый неудобный: инлайн-стили, которые записываются в строчку с тегом.

Чтобы использовать инлайн-стили, нужно использовать атрибуты. Стили состоят из названия свойства и его значения, записанного через двоеточие (”название: значение; название: значение”). В среднем для одного тега задаётся три-четыре стиля. Строчка в таком случае получается длинной.

Из-за того, что этот способ нагромождает код, его практически не используют.

<p style="color: red;">Тестовый текст</p>
<p>Тестовый текст</p>
<p>Тестовый текст</p>
встроенные стили. При их использовании мы разделяем HTML и CSS, код выглядит более структурно. Неудобство только в том, что всё находится в одном месте. В этом случае мы должны прописать, к какому тегу применить стиль. Фигурные скобки в данном варианте обязательны, поскольку являются частью синтаксиса. 
<head>
    <style>
     p {
         color: pink;
     }
    </style>
</head>
вариант, удобный для больших сайтов — отдельный файл для CSS (style.css). Изначально в нём не должно быть ничего. Этот файл нужно связать с другим — в файле с кодом пишем:
<link rel="stylesheet" href="style.css">
# В href мы указываем путь к файлу (если в разных директориях) или название (если в одной директории)
В файле стилей пишем стили для какого-либо тега — например, для <body>

body {
    background-color: crimson
}

Разберёмся с тем, какие существуют стили и как их задавать.

Селектор — это то, что мы выбираем, для чего мы будем задавать стиль. Мы можем выбрать конкретный тег.

тег <body> влияет на весь сайт;
тег <p> — на отдельные блоки сайта.
Стили можно задавать не только тегам, но также классам и их ID, реже — к атрибутам.

Зададим стиль для ID тега:

ID тегов нужны для того, чтобы мы могли выделить определённый тег и задать стиль этому конкретному тегу — или чтобы сгруппировать теги.

В файле с кодом присваиваем тегам ID (уникальный, один для одного тега), класс (один и тот же для нескольких тегов):
<p id="test">Тестовый текст</p>
<p class="text">Тестовый текст</p>
<p class="text">Тестовый текст</p>
<p class="text">Тестовый текст</p>
<p>Тестовый текст</p>
<p>Тестовый текст</p>
<p>Тестовый текст</p>
2. В CSS-файле задаём стиль. Для обозначения ID тега перед названием ID используем символ #. Для обозначения класса перед названием класса используем точку. Символы, которые мы используем (или не используем) — это и есть селектор.

#est {
    background-color: royalblue;
}

.text {
    background-color: olivedrab;
}
Классы и ID мы можем задавать к любым тегам, любые теги мы можем группировать в сочетания, чтобы сделать им одинаковые стили.



Какие бывают стили:

цвет текста — color;
цвет заднего фона — background-color;
размер текста — font-size: 00px;
шрифт — font-family: [название шрифта];
жирность (насыщенность) текста — font-weight: [число 100-200-300-…-900 или normal/bold/lighter/bolder/etc.]. Для некоторых шрифтов невозможно изменить жирность (обычно это относится к дополнительным шрифтам, а не к стандартным);
изменение ширины — width: 00%;
🧠 Размер текста указывается либо в пикселях, либо в процентах от размера родительского объекта (внутри которого они находятся). Теги с блочной моделью отображения занимают 100% ширины всего сайта. Если мы указываем размер в пикселях, то размер элемента не будет адаптироваться под экран, если процентах — будет.

изменение высоты — height: 000px;
сделать видимыми рамки вокруг изображения, тега и т.д. Изначально рамки существуют, просто их толщина 0, и мы их не видим:
цвет рамки — border-color: deeppink;
стиль рамки — border-style: solid;
жирность рамки — border-width: 10px;
скругление углов рамки — border-radius: 20px.
Способы задать цвет:

по текстовому названию;
color red
по RGB-коду:
color rgb(220, 20, 60)
по шестнадцатеричному RGB-коду — самый распространённый способ. В начале названия такого цвета ставится #;
color #1E90FF
Цвета можно брать из таблицы на сайте, который указан в разделе “Дополнительные материалы”.

Создаём элементы в файле с HTML:
<div></div>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
<h1>Тестовый текст</h1>
2. В CSS-файле задаём оформление элемента:

div {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
}
Получается ровный розовый круг.



Для позиционирования нужно использовать свойство position, у которого есть несколько вариаций значения:

static — базовое статичное позиционирование;
относительное позиционирование — относительно своего изначального положения (левый верхний угол). Для его настройки указывают две стороны, отступы от той или иной стороны;
div {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
    position: relative;
    top: 500px;
    left: 300px;
}
абсолютное позиционирование — относительно всего своего родительского объекта;
div {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
    position: absolute;
    bottom: 100px;
    right: 100px;
}
фиксированное позиционирование — объект фиксируется в том месте, куда мы его поставим, и будет оставаться там даже при скролле;
div {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
    position: fixed;
    bottom: 100px;
    right: 100px;
}
липкое позиционирование.

Псевдоэлементы — такой элемент, который существует, но в HTML их нет. Они создаются в CSS с помощью ::

В HTML-файле создаём элемент:
<h1>Томск</h1>
2. В CSS-файле создаём псевдоэлемент, который стилизует первую букву:

h1::first-letter{
    color: deeppink;
    font-size: 50px:
    border-radius: 10px;
    background-color: bisque;    
}
3. Создаём псевдоэлемент, который добавляет что-то перед уже существующим элементом:

h1::before{
    content: 'Город '
    color: deeppink;
    font-size: 50px:
    border-radius: 10px;
    background-color: bisque;    
}
4. Создаём псевдоэлемент, который добавляет что-то после уже существующего элемента:

h1:after{
    content: 'Город '
    color: deeppink;
    font-size: 50px:
    border-radius: 10px;
    background-color: bisque;    
}
Псевдоклассы помогают с необычной стилизацией, например, для каких-либо событий. Указываются одним двоеточием (:).

Допустим, ссылка. Ссылка имеет состояния:

не посещённая (голубая);
посещённая (фиолетовая);
активная — то есть та, на которую мы вот сейчас кликаем;
на неё навели курсор.
Создаём псевдокласс:

Стилизуем тег:
div {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
}
2. Делаем для этого элемента псевдокласс, который сработает при наведении: 

div: {
    width: 100px;
    height: 100px;
    background-color: deeppink;
    border-radius: 50%;
    transition: 1s;
}

div:hover {
    background-color: #0080ff;
    width: 150px;
    height: 150px;
    # добавляем свойство для плавности:
    transition: 1s;
}
3. В файле HTML создаём ссылку:

<a href="<https://zerocoder.ru/>">Ссылка на Zerocoder</a>
4. В файле CSS создаём стили для разных событий ссылки:

a:link {
    color: deeppink;
}

a:visited {
    color: olivedrab;
}

a:active{
    color: royalblue;
}

Создадим карточку с персонажем.

Оставляем известную нам часть кода в HTML-файле:
<!doctype html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport"
         content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
   <meta http-equiv="X-UA-Compatible" content="ie=edge">
   <title>Первый сайт</title>
   <link rel="stylesheet" href="style.css">
</head>
<body>
2. Создаём див с классом “card” для карточки:

<div class="card">
3. В CSS-файле настраиваем стиль этого дива. Используем селектор класса (точка):

.card{
   width: 400px;
   height: 650px;
   background-color: burlywood;
   border-radius: 60px;
}
4. В HTML-файле заполняем карточку

<div class="card">
   <div class="photo">
       <img src="images.jpeg">
   </div>

   <div class="info">
       <h1>Гарри Поттер</h1>
       <p> литературный персонаж, главный герой серии романов английской писательницы Джоан Роулинг.
           На одиннадцатый день рождения Гарри узнаёт, что является волшебником, и ему уготовано
           место в школе волшебства «Хогвартс», в которой он будет практиковать магию под руководством
           директора Альбуса Дамблдора и других школьных профессоров. </p>
   </div>
</div>
5. В CSS-файле настраиваем стиль дивов внутри главного дива. Используем селекторы класса (точка):

Для размещения элементов лучше использовать не position, а flexbox — его можно изучить самостоятельно, воспользовавшись ссылкой из раздела “Дополнительные материалы”.
.photo {
   height: 40%;
   padding: 40px;
   # padding - это внутренний отступ
   # Для внешних отступов используется margin
}
.info {
   padding: 40px;
   height: 40%;
}
img {
   position: relative;
   left:17%;
   border-radius: 20px;
}
Таких карточек можно сделать несколько.


