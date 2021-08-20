import random


def heapify(arr, arrLength, num):
  root = num  # Inicializando um número para ser a raiz
  left = 2 * num + 1  # Filho da esquerda
  right = 2 * num + 2  # Filho da direita

  # Verificando se o filho da esquerda existe e se é maior que o seu elemento raiz
  if left < arrLength and arr[root] < arr[left]:
    root = left

  # Verificando se o filho da direita existe e se é maior que o seu elemento raiz
  if right < arrLength and arr[root] < arr[right]:
    root = right

  # caso algum dos elementos filhos seja maior, a troca de elementos raiz é feita
  if root != num:
    arr[num], arr[root] = arr[root], arr[num]
    
    # Construindo um novo maxheap com as novas mudanças na árvore
    heapify(arr, arrLength, root)
  


# A função heapSort organiza um array dado como parâmetro
def heapSort(arr):  
  arrLength = len(arr)

  # Constrói o maxheap
  for i in range(arrLength//2 - 1, -1, -1):
    heapify(arr, arrLength, i)

  # Extraindo os elementos um por um
  for i in range(arrLength - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)


def generateArray(size):
  return random.sample(range(0, size + 1), size + 1)


arrSize = int(input("Digite o tamanho do array: "))
# Array que será organizado
arr = generateArray(arrSize)
# Chamada da função heapSort que vai organizar o array original
print(arr)
heapSort(arr)
print(arr)
