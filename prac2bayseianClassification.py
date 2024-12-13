def bayesian(X, Y, xTest):
    noOfInputs = len(X)
    noOfFeatures = len(X[0])

    outputClasses = list(set(Y))
    probablities = []

    for outputClass in outputClasses:
        totalInputsWithClass = 0
        probablityFeature = [0] * noOfFeatures

        for rowNum in range(noOfInputs):
            if Y[rowNum] == outputClass:
                totalInputsWithClass += 1

                for featureNum in range(noOfFeatures):
                    if X[rowNum][featureNum] == xTest[featureNum]:
                        probablityFeature[featureNum] += 1

        probablity = totalInputsWithClass / noOfInputs

        for featureNum in range(noOfFeatures):
            probablityFeature[featureNum] /= totalInputsWithClass
            probablity *= probablityFeature[featureNum]

        probablities.append(probablity)

    print(outputClasses, probablities)

    predictedClassIndex = 0
    for i in range(len(outputClasses)):
        if probablities[i] > probablities[predictedClassIndex]:
            predictedClassIndex = i

    predictedClass = outputClasses[predictedClassIndex]
    print('PredictedClass:', predictedClass)


bayesian(
    [
        ["thick"],
        ["thick"],
        ["thin"],
        ["thin"],
        ["thin"],
        ["thick"],
        ["thick"],
        ["thick"]
    ],
    [
        "pos",
        "pos",
        "pos",
        "pos",
        "neg",
        "neg",
        "neg",
        "neg",
    ],
    ["thin"]
)
