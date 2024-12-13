p_w1 = int(input("Enter a priori percentage of Covid patients: ")) / 100
p_w2 = int(input("Enter a priori percentage of Non-Covid patients: ")) / 100

print("p_w1 =", p_w1)
print("p_w2 =", p_w2)

a1 = "medication"
a2 = "non-medication"

print("\na1 =", a1)
print("a2 =", a2)

print("\nLoss Matrix")

print("For action alpha1 i.e. medication")
lossMatrix_11 = int(input("Enter loss value for w1 i.e. Covid: "))
lossMatrix_12 = int(input("Enter loss value for w2 i.e. Non-Covid: "))

print("\nFor action alpha2 i.e. non-medication")
lossMatrix_21 = int(input("Enter loss value for w1 i.e. Covid: "))
lossMatrix_22 = int(input("Enter loss value for w2 i.e. Non-Covid: "))

print("\nSo loss matrix is:")
print(f"{lossMatrix_11} {lossMatrix_12}")
print(f"{lossMatrix_21} {lossMatrix_22}")


def getBayesianRiskOptimalAction():
    R_a1 = (lossMatrix_11 * p_w1) + (lossMatrix_12 * p_w2)
    R_a2 = (lossMatrix_21 * p_w1) + (lossMatrix_22 * p_w2)
    print("\nR_a1 =", R_a1)
    print("R_a2 =", R_a2)
    return a1 if R_a1 < R_a2 else a2


def getConditionalRiskOptimalAction():
    print("\nClass conditional probability table:")

    print("For blood test sample +ve i.e. x1")
    p_x1_by_w1 = int(input("Enter percentage value for w1 i.e. Covid: ")) / 100
    p_x1_by_w2 = int(input("Enter percentage value for w2 i.e. Non-Covid: ")) / 100

    print("\nFor blood test sample -ve i.e. x2")
    p_x2_by_w1 = int(input("Enter percentage value for w1 i.e. Covid: ")) / 100
    p_x2_by_w2 = int(input("Enter percentage value for w2 i.e. Non-Covid: ")) / 100

    R_a1_by_x1 = lossMatrix_11 * (p_x1_by_w1 * p_w1) + lossMatrix_12 * (p_x1_by_w2 * p_w2)
    R_a2_by_x1 = lossMatrix_21 * (p_x1_by_w1 * p_w1) + lossMatrix_22 * (p_x1_by_w2 * p_w2)

    print("\nR_a1_by_x1 =", R_a1_by_x1)
    print("R_a2_by_x1 =", R_a2_by_x1)

    x1_optimal_action = a1 if R_a1_by_x1 < R_a2_by_x1 else a2
    print(f"For x1 (+ve blood test sample), optimal action = {x1_optimal_action}")

    R_a1_by_x2 = lossMatrix_11 * (p_x2_by_w1 * p_w1) + lossMatrix_12 * (p_x2_by_w2 * p_w2)
    R_a2_by_x2 = lossMatrix_21 * (p_x2_by_w1 * p_w1) + lossMatrix_22 * (p_x2_by_w2 * p_w2)

    print("\nR_a1_by_x2 =", R_a1_by_x2)
    print("R_a2_by_x2 =", R_a2_by_x2)

    x2_optimal_action = a1 if R_a1_by_x2 < R_a2_by_x2 else a2
    print(f"For x2 (-ve blood test sample), optimal action = {x2_optimal_action}")


print("\nBayesian Risk")
print(getBayesianRiskOptimalAction(), "is the optimal action")

print("\nConditional Risk")
getConditionalRiskOptimalAction()

# 30, 70, 5, 15, 25, 5, 85, 20, 15, 80