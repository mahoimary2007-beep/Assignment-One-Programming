try:
    score1 = float(input("Enter first test score: "))
    score2 = float(input("Enter second test score: "))
    score3 = float(input("Enter third test score: "))
    average = (score1 + score2 + score3) / 3
    
    print("\n--- Results ---")
    print(f"Score 1: {score1}")
    print(f"Score 2: {score2}")
    print(f"Score 3: {score3}")
    print(f"Average score: {average:.2f}")
    
except ValueError:
    print("Error: Please enter numbers only")
