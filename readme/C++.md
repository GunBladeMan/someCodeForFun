# Список с описанием всех работ на C++

- [isPrime](https://github.com/GunBladeMan/someCodeForFun/blob/main/C%2B%2B/isPrime.txt) : функция для определения является ли число простым или нет
- [textEditorNumber](https://github.com/GunBladeMan/someCodeForFun/blob/main/C%2B%2B/textEditorNumber.txt) : редактирует набор строк, нумеруя каждую строку. Например, начальный набор строк: "A", "B", "C", "D"; конечный набор строк: "1: A", "2: B", "3: C", "4: D".
- [persistence](https://github.com/GunBladeMan/someCodeForFun/blob/main/C++/persistence.txt) : функция, которая принимает на вход положительное целое число, а на выход возвращает его мультипликативную персистентность. Мультипликативная персистентность - это количество последовательных операций умножения цифр числа, пока не получится однозначное число. Например, 39 --> 3 (т.к. 3*9 = 27, 2*7 = 14, 1*4 = 4 и у 4ки только одна цифра, т.о. только 3 перемножений)
- [likes](https://github.com/GunBladeMan/someCodeForFun/blob/main/C%2B%2B/likes.txt) : предположим, что есть пост с именами, кому этот пост понравился. Данная функция принимает на вход список имен, кому понравился пост, и возвращает сообщение с перичислением имен, кому понравился пост, в следующем виде:\n
[] --> "no one likes this"\n
["Peter"] -->  "Peter likes this"\n
["Jacob", "Alex"] --> "Jacob and Alex like this"\n
["Max", "John", "Mark"] --> "Max, John and Mark like this"\n
["Alex", "Jacob", "Mark", "Max"] --> "Alex, Jacob and 2 others like this"\n
