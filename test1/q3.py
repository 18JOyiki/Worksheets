string1 = input()
string2 = input()
def str_comp(s1, s2):
    if s1 == s2:
        return True
    else:
        return False
    
if str_comp(string1, string2):
    print("Strings are the same")
else:
    print("String are different")