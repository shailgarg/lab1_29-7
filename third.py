def get_number_list(name):
   
    num_elements = int(input(f"Enter the number of elements for list a: "))
    
   
    numbers = []
    
    print(f"Enter {num_elements} numbers for list b")
    
    
    for i in range(num_elements):
        while True:
            try:
                number = int(input(f"Element {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
    
    return numbers

def find_common_elements(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    
    common_elements = set1.intersection(set2)
    
    return list(common_elements)

def main():
    print("List 1:")
    list1 = get_number_list("1")
    
    print("List 2:")
    list2 = get_number_list("2")
    
    common_elements = find_common_elements(list1, list2)
    
    print("Common elements:")
    print(common_elements)

if __name__ == "__main__":
    main()
