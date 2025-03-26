# Projeto MaxMin Select

## Descrição do Projeto

O projeto **MaxMin Select** implementa um algoritmo de seleção simultânea do maior e do menor elementos em um array de inteiros. Utilizando a abordagem de **divisão e conquista**, esse método é mais eficiente do que uma abordagem ingînua, reduzindo o número de comparações necessárias.

---

## Sobre o Algoritmo MaxMin Select

O algoritmo **MaxMin Select** funciona da seguinte forma:

1. **Caso base**: Se houver apenas um elemento, ele é tanto o maior quanto o menor.
2. **Caso de dois elementos**: Compará-los diretamente para definir o menor e o maior.
3. **Divisão e Conquista**:
   - O array é dividido ao meio.
   - O algoritmo é chamado recursivamente para encontrar o menor e o maior em cada metade.
   - Os resultados são combinados para obter o menor e o maior do array original.

### Complexidade Assintótica

- **Complexidade Temporal**: \(O(n)\)
- **Complexidade Espacial**: \(O(\log n)\) devido à pilha de recursão.

---

## Como Executar o Projeto

### 1. Criar e ativar um ambiente virtual (Opcional, mas recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 2. Executar o Script

Basta rodar o arquivo `main.py`:

```bash
python main.py
```

O programa solicitará o tamanho da lista e gerará números aleatórios para encontrar o menor e o maior elemento.

---

## Explicação do Código

Arquivo: **main.py**

```python
def max_min_select(arr, left, right):
    if left == right:
        return (arr[left], arr[right])
    
    if right == left + 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    
    mid = (left + right) // 2
    left_min, left_max = max_min_select(arr, left, mid)
    right_min, right_max = max_min_select(arr, mid + 1, right)
    
    overall_min = min(left_min, right_min)
    overall_max = max(left_max, right_max)
    
    return (overall_min, overall_max)

def main():
    import random
    
    n = int(input("Digite o tamanho da lista: "))
    arr = [random.randint(1, 1000) for _ in range(n)]
    
    print(f"\nLista gerada: {arr}")
    
    if not arr:
        print("Lista vazia!")
        return
    
    min_val, max_val = max_min_select(arr, 0, len(arr) - 1)
    
    print(f"\nMenor elemento: {min_val}")
    print(f"Maior elemento: {max_val}")
    print(f"\nVerificação (usando min/max do Python): Min: {min(arr)}, Max: {max(arr)}")

if __name__ == "__main__":
    main()
```

---

## Relatório Técnico

### Análise da Complexidade Assintótica

#### Pelo Método de Contagem de Operações

Cada chamada recursiva divide o problema ao meio, realizando duas chamadas recursivas e um pequeno número de comparações adicionais. O número total de comparações é aproximadamente:
\(C(n) = 2C(n/2) + 2\)
O que resulta em \(O(n)\) no final.

#### Pelo Teorema Mestre

A relação de recorrência é:
\(T(n) = 2T(n/2) + O(1)\)
Aqui:

- \(a = 2\) (número de subproblemas)
- \(b = 2\) (fator de redução por recursão)
- \(f(n) = O(1)\) (custo adicional por chamada)

Calculamos:
\(\log_b a = \log_2 2 = 1\)
De acordo com o Teorema Mestre, estamos no caso 1, o que nos dá:
\(T(n) = O(n)\)

---

## Conclusão

O algoritmo **MaxMin Select** apresenta um desempenho eficiente para encontrar o maior e o menor elemento de um array. Ele reduz o número de comparações necessárias, tornando-se uma abordagem superior à verificação ingînua de todos os elementos.

### Ponto Extra: Diagrama da Recursão

Adicionei um diagrama visual (disponível na pasta `assets/`) que representa como o algoritmo divide o array em subproblemas e combina os resultados.



---

## Entrega

O projeto foi hospedado no GitHub. Certifique-se de testar o link antes de enviá-lo no CANVAS.

