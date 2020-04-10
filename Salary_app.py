from sklearn.externals import joblib
model  = joblib.load("mymodel")
print()
print("Enter the number of years of experience of the user: ",end='')
print()
exp = input()
exp = float(exp)
x= model.predict([[exp]])
salary  = x[0]
print("The expected salary of the new employee will be ",salary)