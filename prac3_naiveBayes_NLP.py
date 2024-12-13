def bayesian(X, Y, xTest):
    noOfInputs = len(X)
    noOfFeatures = len(X[0])

    outputClasses = list(set(Y))
    probabilities = []

    for outputClass in outputClasses:
        totalInputsWithClass = 0
        probabilityFeature = [0] * noOfFeatures

        for rowNum in range(noOfInputs):
            if Y[rowNum] == outputClass:
                totalInputsWithClass += 1

                for featureNum in range(noOfFeatures):
                    if X[rowNum][featureNum] == xTest[featureNum]:
                        probabilityFeature[featureNum] += 1

        probability = totalInputsWithClass / noOfInputs

        for featureNum in range(noOfFeatures):
            probabilityFeature[featureNum] /= totalInputsWithClass
            probability *= probabilityFeature[featureNum]

        probabilities.append(probability)

    print("Output Classes:", outputClasses)
    print("Raw Probabilities:", probabilities)

    totalProbability = sum(probabilities)
    normalizedProbabilities = [prob / totalProbability for prob in probabilities]
    print("Normalized Probabilities:", normalizedProbabilities)

    predictedClassIndex = 0
    for i in range(len(outputClasses)):
        if normalizedProbabilities[i] > normalizedProbabilities[predictedClassIndex]:
            predictedClassIndex = i

    predictedClass = outputClasses[predictedClassIndex]
    print('Predicted Class:', predictedClass)


bayesian(
    [
        ["y", "n", "mild", "y"],
        ["y", "y", "no", "n"],
        ["y", "n", "string", "y"],
        ["n", "y", "mild", "y"],
        ["n", "n", "no", "n"],
        ["n", "y", "strong", "y"],
        ["n", "y", "strong", "n"],
        ["y", "y", "mild", "y"],
    ],
    [
        "n",
        "y",
        "y",
        "y",
        "n",
        "y",
        "n",
        "y",
    ],
    ["y", "n", "mild", "n"]
)
