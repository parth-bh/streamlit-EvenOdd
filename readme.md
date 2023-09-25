## EVEN or ODD

This application or personal project is created to explore the Streamlit framework and understand how to deploy it both on Heroku and Streamlit Sharing.


### Objective.

The objectives of this project are as follows:
1. To learn how to utilize Streamlit as a user interface for a web application.
2. To implement a Streamlit application that can identify whether a given number is even or odd.
3. To gain practical experience in deploying the application on both Heroku and Streamlit Sharing.

In this project, Streamlit has been used to create a simple user interface that checks whether a provided number is even or odd.


### How to run the application:

**1. Run on LocalHost:** 

Step1: Install the dependencies by using the following command:
```
pip install -r requirements.txt
```
Step2: Run the Streamlit app by using the command:
```
streamlit run app.py
```
Ensure that you are in the correct directory, and pip is installed on your machine.



**2. Deploy on Heroku:** 

I have already created the Procfile and setup.sh file, which will be used for deployment on Heroku. The Procfile specifies the command or process that should be executed to start your application. This is crucial because it enables the platform to understand how to run the application correctly. Different platforms may have slightly different requirements or use cases for Procfiles. 

I have included the following commands in the Procfile:
```
web: sh setup.sh && streamlit run app.py
```
Here's a breakdown of the commands:

* 'web' is a process type typically used for web applications.
* 'sh setup.sh' is used to execute the setup file, which is a shell script.
* 'streamlit run app.py' is used to run the Streamlit framework.


I am going to use the Heroku CLI to deploy the application:

**Step1:** Log In to Heroku

To begin, log in to the Heroku account via the CLI using the following command:
```
heroku login
```
This command will open a web page where you we enter the Heroku credentials. Once logged in, return to the terminal.


**Step2:** Prepare the application.

Ensure that you are in the local Git repository of your project, and your code is up-to-date. Additionally, make sure the Python application resides in a directory containing a requirements.txt file (listing the project's dependencies) and a Procfile (specifying how to run the application).


**Step3:** Create a Heroku App

Use the following command to create a new Heroku app, replacing app-name with a unique name of any choice:
```
heroku create app-name
```



**Step4:** Deploy the Application.

Deploy the application to Heroku using Git. This command will push the code to Heroku's servers:

```
git push heroku master
```


**Step5:** Open the Application.

After the deployment is complete, we can open the application in the web browser with the following command:
```
heroku open
```

That's it! The Python or Streamlit application, which we have already pushed to Git, is now deployed on Heroku and accessible on the internet.

**Note:** We can make updates to the code and redeploy by pushing changes to the Heroku remote repository (git push heroku master), and Heroku will automatically handle the deployment process.

Additionally, we can scale the application. By default, Heroku may start the app with only one web dyno (a lightweight container). Depending on the app's requirements, we may need to scale it to multiple dynos for better performance. To increase the number of dynos, use the following command:

```
heroku ps:scale web=2
```
This command scales the app to have 2 dynos. We can adjust the number as needed.


**What is dyno here:**

A web dyno is a container that can handle multiple users and requests simultaneously, depending on its capacity and the nature of the application. Adding more web dynos can help the application handle a larger number of concurrent users and traffic. The capacity of each dyno depends on its type and the allocated resources. Heroku offers different dyno types with varying levels of CPU and memory, allowing us to choose the type that best suits the application's needs.



**3. Deploy on Streamlit Share:**

I've explored the Streamlit Share CLI, but it appears to be unavailable currently. As a result, I've opted for GUI-based deployment and documented the simple steps I used.

**Step1:** Begin by logging in to Streamlit Share.

**Step2:** Create a new app and authorize it with the GitHub account. This step grants access to all our repositories, from which we will need to select the relevant one.

**Step3:** Once we have selected the repository, provide the domain details we wish to use. If available, we can acquire the desired domain.

This process offers a straightforward deployment experience. However, it's important to be aware of certain limitations. Streamlit Share may not be suitable for large-scale applications due to a 1GB resource limit allocated for each app.

The application is accessible at the following domains:
*   For Streamlit Share deployment: https://app-evenodd.streamlit.app/
*   For Heroku deployment: https://even-odd-finder.herokuapp.com/
