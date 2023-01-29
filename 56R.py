def Len_Rec(word):
    if word == '':
        return 0
    else:
        return 1 + Len_Rec(word[1::])
    
word = 'abcdc'
print(Len_Rec(word))