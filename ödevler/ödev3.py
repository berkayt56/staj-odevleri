


# Soru: Bir listedeki en sık tekrar eden ardışık eleman grubunu bulan bir Python işlevi nasıl yazılır?
#Örnek 1: Girdi:[1,1,2,2,2,2,3,4,4,] Çıktı: [2,2,2,2]
#Örnek 2: Girdi: [1,2,2,3,4,4,4] Çıktı: [4,4,4]

def question1(list):
    if (len(list) == 0):
        return []
    count_dict = {}
    output_list = []
    for num in list:
        x = list.count(num)
        count_dict[num] = x
    numRepeat = max(count_dict.values())

    for key,value in count_dict.items():
        if (value == numRepeat):
            answerNum = key

    for i in range(numRepeat):
        output_list.append(answerNum)

    return output_list

print(question1([]))



print("************************************************")



#Soru 2: Bir metindeki palindrom kelimeleri bulan bir Python işlevi nasıl yazılır?
#Örnek 1: Girdi: "selam madam!!!! ama deneme" Çıktı: ["madam",ama]
#örnek 2: Girdi: "merhaba ben berkay" Çıktı: []



import string
def question2(str_input):
    clean_spaces_words = str_input.split()
    clean_words = []
    for word in clean_spaces_words:
        cleanWord = word.strip(string.punctuation)
        clean_words.append(cleanWord)

    output_list = []
    reverse_word = ""
    for word in clean_words:
        reverse_word = word[::-1]
        if(word==reverse_word):
            output_list.append(reverse_word)
    return output_list


print(question2("berkay asasttsasa??????? yani "))


