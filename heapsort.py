import visualization
import random

arr = random.sample(range(512), 512)


def run():
  hp()


def update_display(swap1, swap2):
  visualization.update(swap1, swap2)


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
    update_display(arr[num], arr[root])
    
    # Construindo um novo maxheap com as novas mudanças na árvore
    heapify(arr, arrLength, root)
  

# A função heapSort organiza um array dado como parâmetro
def hp():  
  arrLength = len(arr)

  # Constrói o maxheap
  for i in range(arrLength//2 - 1, -1, -1):
    heapify(arr, arrLength, i)

  # Extraindo os elementos um por um
  for i in range(arrLength - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)