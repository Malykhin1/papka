word = (input("Введите слово: ")) 
a = word.count('a') 
e = word.count('e') 
i = word.count('i') 
o = word.count('o') 
u = word.count('u') 
y = word.count('y') 

print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {len(word) - (a + e + i + o + u)}")

#ссылка на репозиторий в GitHub: https://github.com/Malykhin1/python_tasks
