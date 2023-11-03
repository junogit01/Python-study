digits = "23"

# def letterCombinations(self, digits: str) -> List[str]:
#         letter_dict = {
#             "2": ["a", "b", "c"],
#             "3": ["d", "e", "f"],
#             "4": ["g", "h", "i"],
#             "5": ["j", "k", "l"],
#             "6": ["m", "n", "o"],
#             "7": ["p", "q", "r", "s"],
#             "8": ["t", "u", "v"],
#             "9": ["w", "x", "y", "z"]
#         }

#         def dfs(index, path):
#             if index == len(digits):
#                 combinations.append("".join(path))
#                 return

#             current_digit = digits[index]
#             for letter in letter_dict[current_digit]:
#                 path.append(letter)
#                 dfs(index + 1, path)
#                 path.pop()

#         combinations = []
#         if digits:
#             dfs(0, [])
#         return combinations


def letterCombinations(digits: str) -> list[str]:
        result = []
        letter_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        def dfs(word=""):
             if len(digits) == len(word):
                  result.appen(word)
                  return
             for i in letter_dict[digits[len(word)]]:
                  dfs(word+1)
        dfs()
        return result

print(letterCombinations(digits))