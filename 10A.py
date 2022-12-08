#  Write a method that takes in an array as a parameter and counts the repetition of each element. That is, if an element has appeared in the array more than once, then its ‘repetition’ is its number of occurrences. The method returns true if there are at least two elements with the same number of ‘repetition’. Otherwise, return false.
# Input: {4,5,6,6,4,3,6,4} Output: True
# Explanation: Two numbers repeat in this array: 4 and 6. 4 has a repetition of 3, 6 has a repetition of 3. Since two numbers have the same repetition output is True.
# Input: {3,4,6,3,4,7,4,6,8,6,6} Output: False
# Explanation: Three numbers repeat in this array:3,4 and 6 .3 has a repetition of 2, 4 has a repetition of 3, 6 has a repetition of 4. Since no two numbers have the same repetition output is False.
def repetation(source):
    count = 0
    temp = 0
    increment = 0
    narray = [None]*len(source)
    new = [None]* len(narray)
    for i in range(len(source)):
        count = 1
        for j in range((i+1), len(source)):
            if source[i] == source[j]:
                count += 1

                narray[j] = temp

        if narray[i] != temp:
            narray[i] = count
    #print(narray)

    for elm in narray:
        if elm > 1:
            for i in new:
                if i ==elm:
                    return True
        new[increment] = elm
        increment += 1
    return False
source = [4,5,6,6,4,3,6,4] 
print(repetation(source))
