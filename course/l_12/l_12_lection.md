1. збудувати функцію генератор  за допомогою yield, котра приймає послідовність та повертає пару 
індек та єлемент.
   
   _Відповідь_.
   ```def enumerate(sequence, start=0):
   	n = start
   	for elem in sequence:
   	yield n, elem
   	n += 1
   
