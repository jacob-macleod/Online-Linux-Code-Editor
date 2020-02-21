from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

#A function
import os
#def runCode(command) :
  #result = os.popen(command).readlines()
  #print (result)


#Determines the entry point, / means root of the website

#New route - go to /cakes to view
@app.route('/', methods=['post', 'get'])


            
def login():
    #Initialise some variables
    message = '>>>'
    fileCode = "";
    directory = '';
    defaultValue = "Enter code here"
    fileCode = defaultValue

    if request.method == 'POST':
        username = request.form.get('username')  # access the data inside 
        password = request.form.get('password')
        fileNameInput = request.form.get('fileNameInput')
        fileCode = defaultValue
        if username == 'root' and password == 'pass':
            message = "Hidden stuff unlocked - boss mode activated. You are one clever coder, that's for sure!"
            fileCode = defaultValue
        else:
            directory = 'Terminal:'
            message = "Wrong username or password"
            result = os.popen(username).readlines()
            strResult = str(result)
            message = '>>> ' + strResult 
            fileCode 
            if password != "No code":
              fileCode = password
            else:
              fileCode = "No code" 
            if(username == 'open') :
                file = open(fileNameInput, 'r') 
                fileCode = file.read()
                file.close()
                message = '>>> '
            elif (username == 'save') :
                f = open(fileNameInput, 'w')
                message = fileNameInput
                f.write(password)
                f.close()
                message = '>>> '
                    
 
    return render_template('index.html', message=message, fileCode=fileCode, directory=directory)  


#Runs the webserver and the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
