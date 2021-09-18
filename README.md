# GetPyPostPy
## Test local and APIs with Python only GUI
GetPyPostPy uses Tkinter for GUI interface and Python Requests module.

### Getting Started
You'll need a popular Requests package for sending HTTP/1.1 requests
pip install Requests package
**python -m pip install requests**

### Sending GET Requests
On the left there are four buttons for different types of requests. 
Clicking on the specific button will chnage the type of request that will be sent. 
New parameter fields can be added using + button. Unfortunately when you click on the + button it does not retain the values that were entered in previous fields. ***Therefore first create the number of parameter fields you want.*** I will try to make a fix for that in the future.
![Screen Shot](pics/GET.png)

### Sending POST Requests
Click
![Screen Shot](pics/POST.png)

### Sending PATCH Requests
![Screen Shot](pics/PATCH.png)

### Sending DELETE Requests
![Screen Shot](pics/DELETE.png)
