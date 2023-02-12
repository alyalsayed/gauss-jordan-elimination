def examples():
    sub = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    eq = int(input("Please enter the number of equation to be solved : "))
    file = open("user_manual.txt", 'w', encoding="utf-8")
    file.write("This file is your catalogue to use this program.\n\n")
    file.write(
        "First, Store your equations in a text file named 'equations.txt'.\n")
    file.write(
        f"If you have {eq} equations, Your text file should be like this:\n")
    file.write(f"Number of equations: {eq}")
    for i in range(1, eq+1):
        file.write("\n")
        file.write(f"eq{i}: ")
        for j in range(1, eq+1):

            file.write(f"a{i}{j}x{j} ".translate(sub))
            if j < eq:
                file.write("+ ")
            else:
                file.write("= ")

        file.write(f"a{i}0".translate(sub))
    file.write(
        "\n\n##########################################################################################")
    file.close()
    print(_file_.replace("getting_info.py", "examples.txt"))


if _name_ == "_main_":
    examples()