from sklearn import tree

# Caracteristicas
features = [[7, 0.6, 40], [7, 0.6, 40], [37, 0.8, 37], [37, 0.8, 38]]
labels = [0, 0, 1, 1]


classifier = tree.DecisionTreeClassifier()
classifier.fit(features, labels)

res = classifier.predict([[7, 0.6, 40]])

print(res)
