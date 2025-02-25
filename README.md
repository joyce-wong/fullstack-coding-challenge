## Joyce Wong

## Learning Resources
- [Django, React, SQLite learning series](https://www.youtube.com/playlist?list=PLOLrQ9Pn6caw0PjVwymNc64NkUNbZlhFw)
- [Django React Medium article](https://medium.com/@taohidulii/serving-react-and-django-together-2089645046e4#:~:text=Run%20the%20Django%20server%20using,app%20in%20the%20same%20server!)
- [Django Rest Framework documentation views tutorial](https://www.django-rest-framework.org/tutorial/3-class-based-views/)
- [Django Rest Framework Query Parameters](https://www.django-rest-framework.org/api-guide/filtering/)
- [Django Queryset Documentation](https://docs.djangoproject.com/en/4.1/ref/models/querysets/)
- [How to Serialize Data with Django Rest Framework](https://sweetcode.io/how-to-serialize-data-with-django-rest-framework/)
- [Django Log In and Registration System Medium article](https://python.plainenglish.io/how-to-build-your-own-login-and-registration-system-in-django-ae39a726cb8a)
- [Django Token Authentication with Custom User Model](https://python.plainenglish.io/django-token-authentication-with-custom-user-model-2d780237bc4)
# New York City Council Full Stack Coding Challenge
You will have **1 full week** to complete this challenge starting when you received the challenge from our office. You can submit your challenge using our [Google Form](https://forms.gle/HXCXFiVvFAJ3WzAc7).

## The Task
NYC’s 51 Council Members want a dashboard application that shows the complaints being made in their respective district. The backend will be a Django RESTful API and a React frontend that makes API calls to the backend endpoints.

## What we’re providing
We’ve set up some starter code for you to use. For this challenge you will be working with React as your frontend and Django as your backend API. Here’s what we’ve done to get you set up:
- The default React files generated by the `npx create-react-app` command.
- Django files generated by the `django-admin startproject` command.
- A SQLite3 database that’s already seeded with User data, UserProfile data, and Complaint data.
    - Each login follows this format:
        - Username: {first_name_initial}{last_name}
        - Password: {last_name}-{district_number}
        - (NOTE: Single digit district numbers do not have zero-padding) 
- Empty methods/views for the endpoints that you will use on the React side.

## Important things to know about the data
1. The fields `account` and `council_dist` both refer to a council district. However, `account` refers to the district in which the complaint is being made, and `council_dist` refers to the district in which the person who is making the complaint lives. *(i.e., John Doe is the Council Member for **District 1**, if a noise complaint labels `account` as `NYCC01` and `council_dist` as `NYCC34`, that means the complaint is being made in his district 1, by a person who lives in district 34).*
2. All of the data are string data types except for the open and close dates. In addition, the data is **NOT** entirely clean; some fields will be empty strings or NULL.
3. Single digit districts numbers are padded by a zero in the Complaint table, **BUT** single digit district numbers in the UserProfile table are **NOT** padded by a zero. You will need to take this into consideration when writing your code.

## How to Start
1. Start by **cloning** this [Github repository](https://github.com/NewYorkCityCouncil/fullstack-coding-challenge) to download the starter code.
2. Make sure your repository is **public** so the team can access and review the code.
3. Make sure you have python (**version 3.6 or greater**) and node installed.
4. Inside the main directory (`fullstack-coding-challenge/testApp`), run the following commands to install your dependencies and set up your database:
    - `pip install -r requirements.txt` (you can do this in a virtual environment like venv or anaconda if you’d like)
    - `python manage.py migrate`
    - `python manage.py populate_db`
    - `python manage.py createsuperuser` (If you want to access the django admin portal to view the data)
5. Inside of the React app (`fullstack-coding-challenge/testApp/frontend`), run `npm install` to get all of your frontend dependencies.
6. From there you should be able to start your frontend and backend using `npm start` and `python manage.py runserver`, respectively.

## The API endpoints
`localhost:8000`

| Route | Method | Description |
| ----- | ------ | ----------- |
| `/admin/` | GET | Log in for superusers into the Django admin portal |
| `/login/` | POST | Accepts username and password and returns a **token**. Use this **token** to authorize use of other endpoints. View the [documentation](https://www.django-rest-framework.org/api-guide/authentication/#basicauthentication) |
| `/api/complaints/` | GET | Returns **all complaints** |
| `/api/complaints/openCases/` | GET | Returns **all open complaints** |
| `/api/complaints/closedCases/` | GET | Returns **all closed complaints** |
| `/api/complaints/topComplaints/` | GET | Returns **top 3 complaint types** |

**NOTE**: All complain endpoints should return complaints that occur in the user's district. View the "[Important things to know about the data](https://github.com/NewYorkCityCouncil/fullstack-coding-challenge#important-things-to-know-about-the-data)" section for more clarification.

## MVP
### The Django Side ([Django Documentation](https://docs.djangoproject.com/en/2.2/))
1. Fill in the empty viewsets with database queries that the frontend is requesting (see React MVP #2) (`fullstack-coding-challenge/testApp/complaint_app/views.py`) ([Django REST framework viewset documentation](https://www.django-rest-framework.org/api-guide/viewsets/))<br>
[X]The number of open cases in their district (has an open date, but no closing date)<br>
[X]The number of closed cases in their district<br>
[]The top type of complaint being made in their district<br>
[]Tabular data of all complaints made in their district<br>

### The React Side ([React Documentation](https://reactjs.org/docs/getting-started.html))
1. Create a simple login page for Council members to input their credentials (see above in the ‘[What we’re providing](https://github.com/NewYorkCityCouncil/fullstack-coding-challenge#what-were-providing)’ section for the format)
2. Create simple dashboard page that displays the following information:<br>
[]The number of open cases in their district (has an open date, but no closing date)<br>
[]The number of closed cases in their district<br>
[] The top type of complaint being made in their district<br>
[]Tabular data of all complaints made in their district<br>

## BONUS POINTS
### The Django Side
1. Create new endpoint and viewset that should return all complaints that were made by constituents that live in the logged in council member’s district. *(i.e., John Doe is the Council Member for District 1, and he clicks on the new button. His dashboard table now only shows complaints where `conucil_dist` is `NYCC01`).*
2. Update the UserProfile serializer to flatten the User object to reduce calls to the database.

### The React Side
Create a button labelled “Complaints by My Constituents”. This button will trigger a GET request to a different endpoint than what you’ve been using for the MVP. The data return from this endpoint should replace the data in the table.
