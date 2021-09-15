import random
import os
import pygame

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

arr = random.sample(range(700), 700)

arr.reverse()

dimensions = (len(arr) * 2, len(arr)) # valor de y deve ser igual ao tamanho do array


# Inicialização do Pygame
pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("black"))


def heapify(arr, arrLength, num):
  root = num              # Inicializando um valor para ser a raiz
  left = 2 * num + 1      # Filho da esquerda
  right = 2 * num + 2     # Filho da direita

  # Verificando se o filho da esquerda existe e se é maior que o seu elemento raiz
  if left < arrLength and arr[root] < arr[left]:
    root = left

  # Verificando se o filho da direita existe e se é maior que o seu elemento raiz
  if right < arrLength and arr[root] < arr[right]:
    root = right

  # caso algum dos elementos filhos seja maior, a troca de elementos raiz é feita
  if root != num:
    arr[num], arr[root] = arr[root], arr[num]
    update(arr[num], arr[root])

    # Construindo um novo maxheap com as novas mudanças na árvore
    heapify(arr, arrLength, root)
  

# A função heapsort organiza um array de tamanho 700
def heapsort():  
  arrLength = len(arr)

  # Constrói um maxheap
  for i in range(arrLength//2 - 1, -1, -1):
    heapify(arr, arrLength, i)

  # Extraindo os elementos um por um
  for i in range(arrLength - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)


def check_events():
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()


def update(swap1=None, swap2=None, display=display):
  display.fill(pygame.Color("black"))
  pygame.display.set_caption(
    "Sorting Visiualiser        Algorithm: HeapSort"
  )

  k = int(dimensions[0] / len(arr))
  for i in range(len(arr)):
      colour = "white"
      if swap1 == arr[i]:
          colour = "green"
      elif swap2 == arr[i]:
          colour = "red"
      pygame.draw.rect(display, colour, (i * k, dimensions[1] - arr[i], k, arr[i]))
  check_events()
  pygame.display.update()


def keep_open():
  pygame.display.set_caption(
    "Sorting Visiualiser        Algorithm: HeapSort"
  )

  while True:
    check_events()
    pygame.display.update()


def main():
  heapsort()
  keep_open()


main()
