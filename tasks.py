#task 1
def sum_month(lts):
    return sum(lts)

# print(sum_month([1500,1900,2200,4300,1900,2300,300,900,5000,2300]))

#task 2
def remove_nu(txt):
    txt = txt.split(' ')
    new_txt = ''
    for t in txt:
        if t != 'ну':
            new_txt += t + " "
    
    return new_txt

#print(remove_nu('ну нускал хаз ма ду аьл хет сунам ну'))

# task 3
def palindrom(text):
    i = 0
    j = len(text) - 1
    text = text.upper()
    is_palindrom = False
    while i != len(text) - 1:
        if text[i] == text[j] :
            is_palindrom = True
        else:
            is_palindrom = False
        i+=1
        j-=1

    return is_palindrom

def palindrom2(text):
    text = text.lower()
    return text == text[::-1]

#print(palindrom('ЗакАз'))
#print(palindrom2('ЗакАз'))

# task 4  
def sort_by_freq(lists):
    dct = {}
    for num in lists:
        if num in dct:
            dct[num] +=1
        else:
            dct[num] = 1

    temp = 0
    for i in range(len(lists)):
        for j in range(len(lists) - i - 1):
            if dct[lists[j]] < dct[lists[j + 1]]:
                temp = lists[j]
                lists[j] = lists[j+1]
                lists[j+1] = temp
            if dct[lists[j]] == dct[lists[j + 1]]:
                if lists[j] < lists[j+1]:
                    temp = lists[j + 1]
                    lists[j + 1] = lists[j]
                    lists[j] = temp
                

    return lists

# print(sort_by_freq([19,19,33,33,19,19,33,28,19,28]))
# print(sort_by_freq([2,3,3,2,7]))


#task 5

def wave(txt):
    result = []
    txt = txt.lower()
    for i in range(len(txt)):
        if txt[i] != ' ':
            result.append(txt[:i] + txt[i].upper() + txt[i+1:])
    return result

# print(wave('Ахмат вперед'))


# task 6
def get_rarename(lst):
    names = {}
    lst = sorted(lst)
    for name in lst:
        if name in names:
            names[name] +=1
        else:
            names[name] = 1
    values = list(names.values())
    keys = list(names.keys())
    index = values.index(min(values))
    return  keys[index]


# print(get_rarename(["Шамиль", "Адам", "Адам", "Мохьмад", "Тимур", "Мохьмад", "Адам", "Мохьмад"])) 


#task 7
def check_password(password):
    flagD = False
    flagC = False
    for pas in password: 
        if pas.isdigit():
            flagD = True
        else: 
            flagC = True
        if pas.isalpha():
            flagC = True
        else:
            flagD = True
    if len(password) < 6:
        return 1
    if flagC and flagD and len(password) > 12 and '#' in password:
         return 5
    if flagC and flagD and '#' in password:
        return 4
    if flagD and flagC:
        return 3
    if password.isdigit() or password.isalpha():
        return 2    

#print(check_password("Chechen95"))
   
# task 8

def code(txt):
    chechen_alphabet_lower = [ 
"а", "аь", "б", "в", "г", "г1", "д", "е", "ё", "ж", "з", "и", "й", "к", "кх", "къ", "к1", "л", "м", "н", 
"о", "оь", "п", "п1", "р", "с", "т", "т1", "у", "уь", "ф", "х", "хь", "х1", "ц", "ц1", "ч", "ч1", "ш", "щ", "ъ", 
"ы", "ь", "э", "ю", "юь", "я", "яь", "1"] 
    result = ''
    i = 0
    while i != len(txt): 
        if txt[i] not in chechen_alphabet_lower:
                result += txt[i]
                i+=1
        else:
            if len(txt[i] + txt[i+1]) == 2 and txt[i] + txt[i+1] in chechen_alphabet_lower:
                index = chechen_alphabet_lower.index(txt[i] + txt[i+1]) + 1
                result +=  chechen_alphabet_lower[index]
                i+=2
            else:
                index = chechen_alphabet_lower.index(txt[i]) + 1 
                if index > len(chechen_alphabet_lower) - 1:
                    index = 0
                result +=  txt[i].replace(txt[i], chechen_alphabet_lower[index])
                i+=1

    return result

print(code('хьо мух ву?'))
print(code('дик ву!'))
print(code('ахь 1амина, я ца йина?'))



