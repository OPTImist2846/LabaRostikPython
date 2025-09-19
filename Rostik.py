import random

def check_point_in_region(x, y, R):

    distance_squared = x**2 + y**2
    r_squared = R**2


    in_first_quadrant = x >= 0 and y >= 0
    in_third_quadrant = x <= 0 and y <= 0


    if distance_squared <= r_squared:
        if in_first_quadrant or in_third_quadrant:
            return True


    return False

def generate_shot(R):

    x = random.uniform(-1.5 * R, 1.5 * R)
    y = random.uniform(-1.5 * R, 1.5 * R)
    return (x, y)

# Головна частина
def main():
    try:

        R = float(input("Enter the target radius R: "))
        if R <= 0:
            print("Radius must be a positive number.")
            return

        num_shots = 10

        print("\n")
        print(f"{'№ shot':<15}{'Shot coordinate':<25}{'Результат':<10}")

        for i in range(1, num_shots + 1):

            x, y = generate_shot(R)

            hit = check_point_in_region(x, y, R)

            result_text = "hit the target" if hit else "target is not damaged"

            print(f"{i:<15}({x:.2f}, {y:.2f}):{result_text:^25}")

    except ValueError:
        print("Error: Incorrect format of the entered data. Please enter a number..")

if __name__ == "__main__":
    main()