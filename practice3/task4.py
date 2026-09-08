print("Sofia Zaharchuk, IT-32")

score = int(input("Enter your score (0-100): "))
missed = int(input("Enter number of missed classes: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
    elif score >= 82:
        grade = "B"
    elif score >= 74:
        grade = "C"
    elif score >= 64:
        grade = "D"
    elif score >= 60:
        grade = "E"
    else:
        grade = "F"

    passed = "passed" if score >= 60 else "failed"

    total_classes = 16
    missed_percentage = missed / total_classes * 100

    if missed_percentage > 30:
        print("Warning: you missed more than 30% of classes, not admitted to the test")
        passed = "failed"

    print(f"Score: {score}, grade: {grade}, result: {passed}")
