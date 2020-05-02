from flask import Flask

app = Flask(__name__)

@app.route('/namgil')
def helloworld():
    return "hi"

@app.route('/')
def default_function():
    return "default"

@app.route('/colour')
def colour():
    return "purple"

if __name__== '__main__':
    app.run()

a = [4, 2, 1, 9]
b = 0
for i in range(len(a)):
    if a[b] > a[i]:
        b = i
print("i b[i]", b, a[b])