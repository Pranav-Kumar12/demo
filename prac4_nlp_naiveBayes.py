def tokenize(s):
    tokens = []
    curr = ''
    for c in s:
        if str.isalpha(c):
            curr += c.lower()
        elif curr != '':
            tokens.append(curr)
            curr = ''
    if curr != '':
        tokens.append(curr)
    return tokens


def tokenizedStatementToFrequency(tokenizedStatement, uniqueWords):
    return [tokenizedStatement.count(word) for word in uniqueWords]


def nlp(statements, Y, testStatement):
    tokenizedStatements = [tokenize(statement) for statement in statements]
    uniqueWords = list(set(sum(tokenizedStatements, [])))
    frequencyStatements = [tokenizedStatementToFrequency(t, uniqueWords) for t in tokenizedStatements]
    frequencyTest = tokenizedStatementToFrequency(tokenize(testStatement), uniqueWords)

    outputClasses = list(set(Y))
    probabilities = []

    for outputClass in outputClasses:
        totalInputsWithClass = 0
        wordsFrequency = [0] * len(uniqueWords)

        for rowNum in range(len(statements)):
            if Y[rowNum] == outputClass:
                totalInputsWithClass += 1

                for wordNum in range(len(uniqueWords)):
                    wordsFrequency[wordNum] += frequencyStatements[rowNum][wordNum]

        totalWordsFrequency = sum(wordsFrequency)
        probability = totalInputsWithClass / len(statements)

        for wordNum in range(len(uniqueWords)):
            if frequencyTest[wordNum] != 0:
                probability *= (wordsFrequency[wordNum] + 1) / (totalWordsFrequency + len(uniqueWords))

        probabilities.append(probability)

    predictedClassIndex = probabilities.index(max(probabilities))
    predictedClass = outputClasses[predictedClassIndex]

    print('Predicted Class:', predictedClass)


statements = [
    "i loved, The movie",
    "i hated the movie",
    "a great movie, good movie",
    "poor acting",
    "great acting, a good movie"
]

Y = ["+", "-", "+", "-", "+"]
testStatement = "i hated the poor acting"

nlp(statements, Y, testStatement)
