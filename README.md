# GetPyPostPy
## Test local and APIs with Python only GUI(Gaphical User Interface)
GetPyPostPy uses Tkinter for GUI interface and Python Requests module.

### Getting Started
You'll need a popular Requests package for sending HTTP/1.1 requests
pip install Requests package

**python -m pip install requests**

To test your local APIs you'll need to run GetPyPostPy GUI in a seperate terminal window or CLI (command line interface). For example you could run your local server in a code editor of choice (Vscode, PyCharm, etc) and run GetPyPostPy in CLI or another code editor window. 

### Sending GET Requests
On the left there are four buttons for different types of requests. 
Clicking on the specific button will chnage the type of request that will be sent. The label next url field will change indicating which request is being sent.

New parameter fields can be added using + button. Unfortunately when you click on the + button it does not retain the values that were entered in previous fields. ***Therefore first create the number of parameter fields you want.*** I will try to make a fix for that in the future.

Click on GET Button and then enter your API endpoint URL in the top field. Then add the number of parameter fields you'll need for your GET request before adding values to the parameter fields. Click SEND button to send your request. If successful you'll get a **JSON response in a Response field**, and a **response status code** will show up above the Response field. 
![Screen Shot](pics/GET.png)

### Sending POST Requests
Click on POST Button and then enter your API endpoint URL in the top field. Then add the number of parameter fields you'll need for your POST request before adding values to the parameter fields. 
![Screen Shot](pics/POST.png)

### Sending PATCH Requests
Click on PATCH Button and then enter your API endpoint URL in the top field. Then add the number of parameter fields you'll need for your PATCH request before adding values to the parameter fields. 
You can enter the ID for specific entry in the database as one of the parameters as shown in an example below. 
You can also enter the ID this way (*http://127.0.0.1:5000/update_reps/6*) depending on which API endpoint you have built. 
![Screen Shot](pics/PATCH.png)

### Sending DELETE Requests
Click on DELETE Button and then enter your API endpoint URL in the top field. Then add the number of parameter fields you'll need for your DELETE request before adding values to the parameter fields. 
This shows an example of passing an API-key in order to be able to delete an entry in the database. 
![Screen Shot](pics/DELETE.png)
