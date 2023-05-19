def check_probability_distribution(probabilities):
    # Check if all probabilities are non-negative
    if any(p < 0 for p in probabilities):
        return False

    
    if sum(probabilities) != 1: #to check for sum=1
        return False

    return True

probabilities_x = [0.4, 0.4,0.2]
is_valid_distribution_x = check_probability_distribution(probabilities_x)

if is_valid_distribution_x:
    print("The given probabilities for X represent a valid probability distribution.")
else:
    print("The given probabilities for X do not represent a valid probability distribution.")

probabilities_x = [0.1,0.5,0.2,-0.1,0.3]
is_valid_distribution_x = check_probability_distribution(probabilities_x)

if is_valid_distribution_x:
    print("The given probabilities for X represent a valid probability distribution.")
else:
    print("The given probabilities for X do not represent a valid probability distribution.")


# Test probability distribution for Y
probabilities_y = [0.6,0.1, 0.2]
is_valid_distribution_y = check_probability_distribution(probabilities_y)

if is_valid_distribution_y:
    print("The given probabilities for Y represent a valid probability distribution.")
else:
    print("The given probabilities for Y do not represent a valid probability distribution.")

# Test probability distribution for Z
probabilities_z = [0.3, 0.2, 0.4, 0.1, 0.05]
is_valid_distribution_z = check_probability_distribution(probabilities_z)

if is_valid_distribution_z:
    print("The given probabilities for Z represent a valid probability distribution.")
else:
    print("The given probabilities for Z do not represent a valid probability distribution.")

