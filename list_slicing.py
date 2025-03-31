def demonstrate_slicing():
    # Create initial list
    numbers = list(range(1, 11))
    print(f"Original list: {numbers}")
    
    # Extract first five elements
    first_five = numbers[:5]
    print(f"\nFirst five elements: {first_five}")
    
    # Reverse the extracted elements
    reversed_five = first_five[::-1]
    print(f"Reversed first five: {reversed_five}")
    
    # Additional demonstration
    print("\nAdditional slicing examples:")
    print(f"Every second element: {numbers[::2]}")
    print(f"Last three elements: {numbers[-3:]}")
    print(f"Elements 3-7: {numbers[2:7]}")

if __name__ == "__main__":
    demonstrate_slicing()