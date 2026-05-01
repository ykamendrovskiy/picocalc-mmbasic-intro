# Урок 01 — Язык: тур по MMBasic

Цель: за один присест увидеть, чем MMBasic отличается от QBasic — что выкинуто, что переделано, что добавлено. Это «карта местности», а не справочник: погружаться в детали будем в следующих уроках.

Если ты QBasic не открывал лет двадцать — не переживай, всё, что нужно, по дороге напомнится.

## Главное за минуту

| Аспект | QBasic | MMBasic |
|--------|--------|---------|
| Номера строк | По желанию | Не нужны (метки вместо них) |
| `GOSUB ... RETURN` | Основной способ модулировать | Не нужно — есть `SUB` и `FUNCTION` |
| `DEFINT`, `DEFSTR`… | Префиксы по букве переменной | `OPTION DEFAULT INTEGER`/`FLOAT`/`STRING`/`NONE` |
| Целые | 16-bit `INTEGER`, 32-bit `LONG` | **64-bit** `INTEGER`, всё через одно слово |
| Числа с плавающей | `SINGLE` / `DOUBLE` | `FLOAT` (всегда double) |
| Имена переменных | До 40 символов | До 32+ символов, можно `_` |
| `PRINT USING` | Есть | Есть, плюс функция `FORMAT$()` |
| Многомерные массивы | `DIM a(10, 10)` | То же + `OPTION BASE 0/1` |
| Графика | На VGA | Прямо на встроенном экране |
| `IF ... THEN ... ELSE` однострочный | Да | Да + многострочный с `ENDIF` |
| `SELECT CASE` | Да | Да, плюс `CASE 1 TO 5` и `CASE IS > 10` |
| Файлы | `OPEN ... FOR ...` | То же, плюс встроенные функции SD-карты |

В целом, если ты пишешь на QBasic — переходишь на MMBasic за полчаса. Дальше — детали и вкусняшки.

## Никаких номеров строк

В QBasic было нормально:

```basic
10 PRINT "Hi"
20 GOTO 10
```

В MMBasic так тоже работает, но это устаревший стиль. Современный код пишут с **метками**:

```basic
loop_start:
  PRINT "Hi"
  PAUSE 500
  GOTO loop_start
```

И всё же `GOTO` — это последнее средство. Реальный MMBasic-код использует циклы и подпрограммы.

## Типы данных

Три типа:

| Тип | Суффикс | Что это |
|-----|---------|---------|
| `INTEGER` | `%` | 64-битное целое со знаком (~ ±9.2 квинтиллионов) |
| `FLOAT` | `!` | Double precision (15–16 значащих цифр) |
| `STRING` | `$` | Строка переменной длины |

```basic
DIM count%               ' целое
DIM ratio!               ' float
DIM name$                ' строка
DIM steps AS INTEGER     ' эквивалент DIM steps%
DIM x AS FLOAT
DIM s AS STRING
```

По умолчанию переменная без суффикса — это `FLOAT`. Это часто не то, что хочешь. Поэтому **в начале каждой программы** обычно ставят:

```basic
OPTION EXPLICIT          ' все переменные надо объявить через DIM
OPTION DEFAULT NONE      ' нельзя без явного типа
```

Это экономит часы отладки: опечатался в имени переменной — компилятор сразу скажет, а не молча создаст новую.

## Объявление и присваивание

```basic
DIM lives AS INTEGER = 3
DIM player_name AS STRING = "Alice"
DIM pi AS FLOAT = 3.14159

LET score = 0           ' LET — необязательно, можно просто:
score = score + 10
```

Несколько переменных в одной строке:

```basic
DIM x AS INTEGER, y AS INTEGER, z AS INTEGER
```

## Арифметика и строки

Арифметика обычная: `+ - * /`. Целочисленное деление — `\`, остаток — `MOD`:

```basic
PRINT 17 \ 5    ' 3
PRINT 17 MOD 5  ' 2
```

Логические операторы: `AND`, `OR`, `NOT`, `XOR` — работают и побитово, и булево (через `IF`).

Строки клеятся `+`:

```basic
DIM greeting$ = "Hello, " + "PicoCalc!"
```

Полезные строковые функции:

```basic
LEN("abc")              ' 3
LEFT$("hello", 2)       ' "he"
RIGHT$("hello", 3)      ' "llo"
MID$("hello", 2, 3)     ' "ell"
INSTR("hello", "ll")    ' 3 (позиция, 1-based) или 0 если нет
UCASE$("abc")           ' "ABC"
LCASE$("ABC")           ' "abc"
STR$(42)                ' "42"
VAL("3.14")             ' 3.14
CHR$(65)                ' "A"
ASC("A")                ' 65
```

## Управляющие конструкции

### IF

Однострочный:

```basic
IF lives = 0 THEN PRINT "Game over"
IF score > best THEN best = score : PRINT "New record!"
```

Многострочный:

```basic
IF lives = 0 THEN
  PRINT "Game over"
  GAME_OVER_SOUND
ELSEIF lives = 1 THEN
  PRINT "Last life!"
ELSE
  PRINT "Lives left:"; lives
ENDIF
```

### SELECT CASE

```basic
SELECT CASE key$
  CASE "w", "W"
    y = y - 1
  CASE "s", "S"
    y = y + 1
  CASE " "
    SHOOT
  CASE ELSE
    PRINT "Unknown key: " + key$
END SELECT
```

Поддерживает диапазоны и выражения:

```basic
SELECT CASE age
  CASE 0 TO 12:    PRINT "Ребёнок"
  CASE 13 TO 17:   PRINT "Подросток"
  CASE IS >= 18:   PRINT "Взрослый"
END SELECT
```

### FOR

```basic
FOR i = 1 TO 10
  PRINT i
NEXT i

FOR i = 100 TO 0 STEP -5
  PRINT i
NEXT i
```

Из цикла можно выйти досрочно:

```basic
FOR i = 1 TO 1000
  IF found THEN EXIT FOR
NEXT i
```

### DO ... LOOP

Бесконечный цикл и выход:

```basic
DO
  k$ = INKEY$
  IF k$ <> "" THEN EXIT DO
LOOP
```

С условием — в начале или в конце:

```basic
DO WHILE lives > 0
  PLAY_TURN
LOOP

DO
  PLAY_TURN
LOOP UNTIL lives = 0
```

## SUB и FUNCTION

Это то, чего катастрофически не хватало в старом BASIC. Никаких `GOSUB 1000`.

```basic
' Процедура: ничего не возвращает
SUB greet(name$)
  PRINT "Hello, " + name$ + "!"
END SUB

' Функция: возвращает значение через имя
FUNCTION square(x AS FLOAT) AS FLOAT
  square = x * x
END FUNCTION

' Использование:
greet("PicoCalc")
PRINT square(7)         ' 49
```

Локальные переменные внутри SUB/FUNCTION:

```basic
SUB count_down(n AS INTEGER)
  LOCAL i AS INTEGER
  FOR i = n TO 1 STEP -1
    PRINT i
    PAUSE 500
  NEXT i
END SUB
```

Параметры по умолчанию **передаются по ссылке** — внутри SUB можно изменить значение, и оно изменится у вызывающего. Если хочется по значению — используй `BYVAL`:

```basic
SUB increment(BYREF x AS INTEGER)   ' BYREF — по умолчанию, можно опускать
  x = x + 1
END SUB

SUB don_t_touch(BYVAL x AS INTEGER)  ' x — копия
  x = x + 1
END SUB
```

## Комментарии

Двумя способами:

```basic
' Это комментарий (одинарная кавычка)
REM Это тоже комментарий
PRINT "Hi" : ' и в конце строки
```

## Чего в MMBasic не делай (хотя теоретически работает)

- **`GOSUB ... RETURN`** — работает, но для модульности используй `SUB`.
- **`DEF FN`** — устаревший способ объявить функцию. Используй `FUNCTION`.
- **Имена переменных типа `A1`, `B2`** — давай нормальные имена: `score`, `enemy_x`, `is_paused`.
- **`PRINT USING "###.##"; x`** — работает, но `FORMAT$(x, "%6.2f")` обычно читабельнее.

## Маленький пример, демонстрирующий стиль

```basic
' guess.bas — простая угадайка для разогрева
OPTION EXPLICIT
OPTION DEFAULT NONE

DIM secret AS INTEGER
DIM guess AS INTEGER
DIM tries AS INTEGER

RANDOMIZE TIMER
secret = INT(RND * 100) + 1     ' 1..100
tries = 0

PRINT "Я загадал число от 1 до 100. Угадай!"

DO
  INPUT "Твой вариант: ", guess
  tries = tries + 1
  IF guess < secret THEN
    PRINT "Больше."
  ELSEIF guess > secret THEN
    PRINT "Меньше."
  ELSE
    PRINT "В точку! Попыток: "; tries
    EXIT DO
  ENDIF
LOOP
```

Запусти, поиграй. Этот же пример мы расширим в [Уроке 02](02-data-and-control.md), когда углубимся в типы и управляющие конструкции.

## Упражнение

1. Перепиши `guess.bas` так, чтобы программа:
   - перед стартом спросила имя игрока и потом обращалась к нему по имени;
   - после выигрыша предлагала сыграть ещё раз (`Y/N`);
   - вела счёт побед в текущей сессии.
2. Используй хотя бы одну `SUB` и одну `FUNCTION`. Например, `SUB greet(name$)` и `FUNCTION random_secret() AS INTEGER`.
3. В начале программы обязательно `OPTION EXPLICIT` и `OPTION DEFAULT NONE`. Если что-то не объявил — компилятор подскажет.

Когда `OPTION EXPLICIT` стал нормой, типы — рефлексом, а структура программы — `SUB main: …: END SUB` плюс набор хелперов, можно идти дальше — в **[Урок 02 — Данные и управление](02-data-and-control.md)**.
