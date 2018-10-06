from tqdm import tqdm
import random

def barra_progresso():
    print()
    a = [x for x in range(2500)]
    random.shuffle(a)

    for i in tqdm(range(len(a))):
        for j in range(len(a) - i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
