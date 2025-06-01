from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letras_telefono = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []
        
        def backtrack(index: int, path: str):
            if index == len(digits):
                result.append(path)
                return
            
            for letter in letras_telefono[digits[index]]:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result

# Ejemplo de uso:
sol = Solution()
print(sol.letterCombinations("23"))  # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
