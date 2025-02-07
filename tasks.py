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


#print(palindrom('ЗакАз'))
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


def wave(txt):
    lts = []
    new_txt = ''
    for i in range(len(txt)):
        txt = txt[i].upper()
        for j in range(len(txt)):
            if txt[j].lower():
                txt = txt[j].lov
        

    return lts

print(wave('волна'))