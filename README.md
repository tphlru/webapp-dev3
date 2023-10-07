# webapp-dev3 fastAPI
$ pip install fastapi uvicorn

In order to see this message on the screen,
specifically any program that allows processing HTTP requests such as a browser, we have to open the server
associated with the previous application and this is where we use the previously installed uvicorn server; to do
this, from the terminal and root of the project, we use the following command:

$ uvicorn api:app --reload --port 8080

--reload
The server will be reloaded every time changes are made to the application.