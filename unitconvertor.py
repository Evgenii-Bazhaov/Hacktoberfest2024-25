def cm_to_inches(cm):
    return cm / 2.54

cm = float(input("Enter length in cm: "))
print(f"{cm} cm = {cm_to_inches(cm):.2f} inches")
