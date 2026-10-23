print("CONCRETE SLAB VOLUME ESTIMATOR")

while True:
    try:
        length = float(input(
            "\nEnter slab length (meters): "))
        width = float(input(
            "Enter slab width (meters): "))
        thickness = float(input(
            "Enter slab thickness (meters): "))

        if length <= 0 or width <= 0 or thickness <= 0:
            print("Error: Measurements must be positive.")
            continue

        volume = length * width * thickness

        print(f"\nRequired concrete volume: "
              f"{volume:.2f} cubic meters")

    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    again = input(
        "\nCalculate another slab? (yes/no): "
    ).strip().lower()

    while again not in ("yes", "no"):
        again = input(
            "Please enter yes or no: "
        ).strip().lower()

    if again == "no":
        break

print("\nThank you for using the calculator!")