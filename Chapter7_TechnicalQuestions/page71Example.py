# Design an algorithm to print all permutations of a string. For simplicity, assume all characters are unique
# Best case and Build
"""
    Build a recursion function that insert an aditional character at all position inside a known list of strings
    Example:
        p("abc") = insert "c" into all strings of p("ab") = {"ab", "ba"}
        p("abc") = merge({"cab", "acb", "abc}, {"cba", "bca", "bac"})
"""

def permutations(str):
    if(len(str) == 2):
        # when length is 2 the string and its reversed form can be returned
        return [str, str[::-1]]

    # get a list to all permutation from the previous level "abc", get from level "ab"
    perm_list = permutations(str[:-1])
    new_list = []

    # for each permutation string returned insert the last letter at every position possible
    letter = str[-1]
    for perm_str in perm_list:
        for i in range(len(perm_str) + 1):
            # insert letter at position i
            new_str = perm_str[:i] + letter + perm_str[i:]
            new_list.append(new_str)

    return new_list

res_list = permutations("abcd")
print(res_list)

# check result with wc -w , result should be n! where n = len(str)