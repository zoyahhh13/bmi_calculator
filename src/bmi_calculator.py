def calculate_bmi(weight_kg, height_m):
    """
    Calculate Body Mass Index (BMI).
    """
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    """
    Returns BMI category string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

if __name__ == "__main__":
    weight = float(input("Enter weight in kilograms: "))
    height = float(input("Enter height in meters: "))
    try:
        bmi_value = calculate_bmi(weight, height)
        category = bmi_category(bmi_value)
        print(f"Your BMI is {bmi_value:.2f}. Category: {category}.")
    except ValueError as e:
        print(f"Error: {e}")
