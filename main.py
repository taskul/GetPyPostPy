from tkinter import *
import requests
from tkinter.ttk import Separator
from tkinter.scrolledtext import ScrolledText

class PostPyGetPy(Tk):
    
    def __init__(self):
        super().__init__()
        self.minsize(width=900, height=600)
        self.title('Test your APIs with PostPyGetPy')  
        self.config(padx=5, pady=1, bg='DarkSeaGreen1')
        #Vertical Seperator
        Separator(self, orient=VERTICAL).grid(column=1, row=0, rowspan=10, sticky='ns')
        #Labels for Requests
        self.requestLabel = Label(text='GET', font=('Arial', 10, 'bold'), bg='DarkSeaGreen1')
        self.requestLabel.grid(column=2, row=0)
        self.responseCodeLabel = Label(text='', font=('Arial', 10, 'bold'), bg='DarkSeaGreen1')
        self.responseCodeLabel.grid(column=7, row=0)
        #buttons for GET Requests
        self.getButton = Button(text='GET', bg='DarkOliveGreen1', font=('Arial', 10, 'bold'), 
                                command=self.getRequest)
        self.getButton.grid(column=0, row=0, padx=10, pady=5)
        #buttons for POST Requests
        self.postButton = Button(text='POST', bg='DarkOliveGreen1', font=('Arial', 10, 'bold'), 
                                command=self.postRequest)
        self.postButton.grid(column=0, row=1, padx=10, pady=5)
        #Buttons for PATCH Requests:
        self.patchButton = Button(text='PATCH', bg='DarkOliveGreen1', font=('Arial', 10, 'bold'),
                                command=self.patchRequest)
        self.patchButton.grid(column=0, row=2, padx=10, pady=5)
        #Buttons for Delete Requests:
        self.deleteButton = Button(text="DELETE", bg='DarkOliveGreen1', font=('Arial', 10, 'bold'),
                                command=self.deleteRequest)
        self.deleteButton.grid(column=0, row=3, padx=10, pady=5)
        #Button for Sending Request:
        self.requestSend = Button(text='Send', bg='DarkOliveGreen1', font=('Arial', 10, 'normal'), 
                                command=self.sendGetRequest)
        self.requestSend.grid(column=6, row=0, padx=10)
        # Add new entry field for parameters button
        self.addNewField = Button(text='+', bg='DarkOliveGreen1', font=('Arial', 14, 'normal'), 
                                command=self.addField)
        self.addNewField.grid(column=6, row=1)
        #Entries for API endpoint
        self.requestEntry = Entry(width=50)
        self.requestEntry.grid(column=3, row=0, columnspan=3)
        #List contating keys and values items for parameters
        self.keyLabels = []
        self.valueLabels = []
        #sets the number of the initial fields for parameters
        self.numberOfFields = 1
        #Create a field for parameters
        self.createFields()
        #JSON Response Text output field
        self.jsonResponseLabel = Label(text='Response field', font=('Arial', 10, 'bold'), bg='DarkSeaGreen1')
        self.jsonResponseLabel.grid(column=7, row=3)
        self.textResponse = ScrolledText(self, width=50, height=20)
        self.textResponse.grid(column=7, row=4, rowspan=10, padx=10)
       
    def createParameters(self):
        '''
        Created a disctionary of parameters 
        '''
        paramDict = {}
        for kv_Params in range(len(self.keyEntries)):
            param_key = self.keyEntries[kv_Params].get()
            param_value = self.valueEntries[kv_Params].get()
            paramDict[param_key] = param_value
        return paramDict

    def processRequests(self, func):
        '''
        Processes request buy taking a request function and depending on the type of request executes that function
        '''
        requestParams = self.createParameters()
        url = self.requestEntry.get()
        if len(url) > 0:
            if len(requestParams) > 0:
                if func is requests.get or func is requests.patch:
                    response = func(url, params=requestParams)
                elif func is requests.post:
                    response = func(url, data=requestParams)
                elif func is requests.delete:
                    response = func(url, params=requestParams)
            else:
                response = func(url)
            #Parsing JSON response and displaying it in the response window. 
            print(response.headers)
            if response.headers['Content-Type'] == 'application/json':
                jsonResponse = response.json()
                self.textResponse.insert(INSERT, chars=str(jsonResponse))
            self.responseCodeLabel.config(text=f'Status code: {response.status_code}')
    
    def sendGetRequest(self):
        self.processRequests(requests.get)

    def sendPostRequest(self):
        self.processRequests(requests.post)

    def sendPatchRequest(self):
        self.processRequests(requests.patch)

    def sendDeleteRequest(self):
        self.processRequests(requests.delete)

    def getRequest(self):
        '''
        Assigned to the GET Button, and changes SEND button funcion
        '''
        self.requestLabel.config(text='GET')
        self.requestSend.config(command=self.sendGetRequest)
        self.clearFields()

    def postRequest(self):
        '''
        Assigned to the POST Button, and changes SEND button funcion
        '''
        self.requestLabel.config(text='POST')
        self.requestSend.config(command=self.sendPostRequest)
        self.clearFields()

    def patchRequest(self):
        '''
        Assigned to the PATCH Button, and changes SEND button funcion
        '''
        self.requestLabel.config(text='PATCH')
        self.requestSend.config(command=self.sendPatchRequest)
        self.clearFields()

    def deleteRequest(self):
        '''
        Assigned to the DELETE Button, and changes SEND button funcion
        '''
        self.requestLabel.config(text='DELETE')
        self.requestSend.config(command=self.sendDeleteRequest)
        self.clearFields()

    def createFields(self):
        '''
        Creates entry fields for parameters
        '''
        #labels for keys and values 
        for kv_Labels in range(0, self.numberOfFields):
            self.keyLabels.append(Label(text=f'Key', bg='DarkSeaGreen1'))
            self.keyLabels[kv_Labels].grid(column=2, row=kv_Labels+1, pady=5)
            self.valueLabels.append(Label(text=f'Value', bg='DarkSeaGreen1'))
            self.valueLabels[kv_Labels].grid(column=4, row=kv_Labels+1)
        #Entries for Keys and Values for API call parameters
        self.keyEntries = []
        self.valueEntries = []
        for kv_Entries in range(0, self.numberOfFields):
            self.keyEntries.append(Entry(width=20))
            self.keyEntries[kv_Entries].grid(column=3, row=kv_Entries+1)
            self.valueEntries.append(Entry(width=20))
            self.valueEntries[kv_Entries].grid(column=5, row=kv_Entries+1)
            
    
    def addField(self):
        '''
        Adds up to 15 entry field for parameters
        '''
        if self.numberOfFields <= 15:
            self.numberOfFields += 1
            self.createFields()
    
    def clearFields(self):
        '''
        Clears all of the entry fields when the type of requst is changed using GET, POST, PATCH or DELETE buttons.
        Also clears the response field, and satus code gets errased from the board.
        '''
        self.requestEntry.delete(0, END)
        for k in self.keyEntries:
            k.delete(0,END)
        for v in self.valueEntries:
            v.delete(0,END)
        self.textResponse.delete('0.0', END)
        self.responseCodeLabel.config(text='')

    

appbase = PostPyGetPy()
appbase.mainloop()

