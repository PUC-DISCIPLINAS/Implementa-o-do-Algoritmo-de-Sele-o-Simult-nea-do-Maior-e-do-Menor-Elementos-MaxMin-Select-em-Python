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
