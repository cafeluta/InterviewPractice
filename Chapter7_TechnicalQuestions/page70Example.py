# Given a `s` string and a `b` string. Print the location of all permutations of `s` in string `b`

# frequency hash map for characters inside `s` string
arrf = {}

s = "abbc"
b = "cbabadcbbabbcbabaabccbabc"

# freq arr for string s
need = {}
for ch in s:
    need[ch] = need.get(ch, 0) + 1

window = {}
req_types = len(need)
matched_types = 0
n = len(s)

for i, ch in enumerate(b):
    # add new character in window to dict
    window[ch] = window.get(ch, 0) + 1
    # if char exists in string and freq is equal one charcter of the permutation is matched
    if ch in need and window[ch] == need[ch]:
        matched_types += 1

    # make window have length n
    if i >= n:
        left = b[i - n]
        # -1 from matched type only when the freq matches
        if left in need and window[left] == need[left]:
            matched_types -= 1
        # -1 always from window dict
        window[left] -= 1

        if window[left] <= 0:
            del window[left]

    # check for match on a permutation
    if matched_types == req_types and i+1 >= n:
        print(f"Permutation at pos: {i - n + 1}")

