from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Elimina todas las ocurrencias de 'val' en 'nums' en su lugar.
        Retorna la nueva longitud de la lista sin los valores eliminados.
        
        Complejidad Temporal: O(n)
        Complejidad Espacial: O(1)
        """
        i = 0  # Puntero para colocar elementos válidos
        for j in range(len(nums)):
            if nums[j] != val:  # Si el elemento actual no es 'val'
                nums[i] = nums[j]  # Moverlo a la posición correcta
                i += 1  # Incrementar puntero de elementos válidos
        
        return i  # La nueva longitud de la lista sin 'val'

# Ejemplo de uso
nums = [3, 2, 2, 3, 4, 7, 9, 4, 3, 7]
val = 3
sol = Solution()
k = sol.removeElement(nums, val)
print(f"Lista después de eliminar {val}: {nums[:k]}")  
print(f"Nueva longitud de la lista: {k}")
