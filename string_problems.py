import re


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        elif sorted(s) != sorted(goal):
            return False
        elif s == goal and len(set(s)) == len(goal):
            return False
        else:
            count = 0
            for i in range(len(s)):
                if s[i] != goal[i]:
                    count += 1
                    if count == 3:
                        return False
            return True
        # return self.budStrngsRec(s, goal, 0, len(s)//2, len(s) - 1)

    def budStrngsRec(self, s, goal, l, p, r, step=1):
        strList = list(s)
        resp = False
        while p != len(s):
            if resp:
                break
            for str in range(l, p + step, step):
                if (str == l):
                    continue
                tempList = strList.copy()
                tempList[l], tempList[str] = tempList[str], tempList[l]
                tempStr = ''.join(tempList)
                if tempStr == goal:
                    resp = True
                    break
            p += 1
        if (not resp):
            while p != 0:
                if resp:
                    break
                for str in range(r, p - step, -step):
                    if (str == r):
                        continue
                    tempList = strList.copy()
                    tempList[r], tempList[str] = tempList[str], tempList[r]
                    tempStr = ''.join(tempList)
                    if tempStr == goal:
                        resp = True
                        break
                p -= 1

        if resp or l == (len(s) - 1):
            return resp
        else:
            return self.budStrngsRec(s, goal, l + step, r - step, len(s)//2)

    def defangIPaddr(self, address: str) -> str:
        if address is not None:
            return address.replace('.', '[.]')

    def countValidWords(self, sentence: str) -> int:
        resp_arr = []
        for word in [word for word in sentence.split(" ") if word != ""]:
            resp = False
            test_regex = re.compile("^[a-z]+[-]{0,1}[a-z]+[!|,|.]{0,1}$|^[a-z]+[-]{0,1}[a-z]+$|^[a-z]*[!|,|.]{0,1}$")
            if  ''.join(test_regex.findall(word)) == word:
                resp = True
            resp_arr.append(resp)
        return len([resp for resp in resp_arr if resp is True])

sol = Solution()
print(sol.buddyStrings("ab", "ba"))
print(sol.buddyStrings("ab", "ab"))
print(sol.buddyStrings("aa", "aa"))
print(sol.buddyStrings("baab", "baba"))
print(sol.buddyStrings("aaaaaaabc", "aaaaaaacb"))
print(sol.buddyStrings("abab", "abab"))
print(sol.buddyStrings("acaaba", "acaaba"))
print(sol.buddyStrings("acba", "abca"))

print(sol.defangIPaddr('1.1.1.1'))
print(sol.defangIPaddr(None))

print(sol.countValidWords("cat and  dog"))
print(sol.countValidWords("stone-game18          ab-c"))
print(sol.countValidWords("alice and  bob are playing stone-game10"))
print(sol.countValidWords("! 10"))
print(sol.countValidWords("! c.b a-b alice bob! ,cd"))
print(sol.countValidWords("q-o  x-p! g-l- q-n  f-o, m-u. m-i! y-k, i-j, d-p! e-t, h-u  j-j- d-z- v-w, r-a  i-h. d-a! z-o, v-l, "))
print(sol.countValidWords("  r3  6bb!f el49 jq.law3  q vju5dg0 .mcxq54jjz a6 n az 8 9bbxyivnrbb g .c8  d e xy29upl var b  7! yqs z 10m t qm  .t3i8e2lp3- xf d pd.   t yy9rk4y, 8, 7 mxl-sn-n  etk.5n va d.pym3..ri0 g9a.dgz0k 5qqxs!a s    46csnc u ima p    "))

