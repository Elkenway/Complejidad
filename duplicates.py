from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Si la lista está vacía, retornar 0
        
        i = 0 
        for j in range(1, len(nums)):  # Puntero rápido
            if nums[j] != nums[i]:  # Si encontramos un nuevo número único
                i += 1
                nums[i] = nums[j]  # Mover el número único hacia la posición correcta
        
        return i + 1  # La longitud de la lista sin duplicados

# Ejemplo de uso
nums = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 9, 8, 10] # La lista original
sol = Solution()
k = sol.removeDuplicates(nums)
print(f"Lista sin duplicados: {nums[:k]}")  
print(f"Longitud de la lista sin duplicados: {k}")  
