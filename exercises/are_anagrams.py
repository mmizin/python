def are_anagrams(str1: str, str2: str) -> bool:
    clean_str1 = str1.replace(' ', '').lower()
    clean_str2 = str2.replace(' ', '').lower()
    
    if len(clean_str1) != len(clean_str2):
        return False
    
    l_str1 = sorted(list(clean_str1))
    l_str2 = sorted(list(clean_str2))
    
    return l_str1 == l_str2


# print(are_anagrams("Listen", "Silent"))
# print(are_anagrams("A gentleman", "Elegant man"))
# print(are_anagrams("Hello", "World") )

def are_anagrams_manual(str1: str, str2: str) -> bool:
    
    for char in str1:
        if char == ' ':
            continue
        
    
    
     
    

print(are_anagrams_manual("Listen", "Silent"))
print(are_anagrams_manual("Worldld", "Worldhe"))

