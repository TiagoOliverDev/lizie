<h1 align="center">Django project</h1>


<hr/>

Login
![background](https://github.com/TiagoOliverDev/lizie/blob/main/static/images/login.png)

Task List
![background](https://github.com/TiagoOliverDev/lizie/blob/main/static/images/home.png)

Category List
![background](https://github.com/TiagoOliverDev/lizie/blob/main/static/images/categoryList.png)

Reports
![background](https://github.com/TiagoOliverDev/lizie/blob/main/static/images/reports.png)




<hr/>

# Features 

- Auth and register account
- Home page task list
- Category list
- Reports

<hr/>

# Technology

I used the following technologies:

- Python
- Django
- Django Rest Framework
- Unitest


<hr/>


# Steps for run project

## Step 1: Clone the repository

- Choose a folder in your local machine where you want this repository to be copied

- Clone this [repository](https://github.com/TiagoOliverDev/lizie.git) to your local machine 

   ```
  git clone https://github.com/TiagoOliverDev/lizie.git
  ```

- Navigate to `cd lizie`  directory.

## Step 2: Create env

# # windows

 python -m venv nome_da_env

 nome_da_env/Scripts/activate

 pip install -r requirements.txt


# # Linux

 python3 -m venv meu_venv

 source meu_venv/bin/activate

 pip install -r requirements.txt
  ```

## Step 3: 

Open folder project and open a terminal and run the following command:

  ```
  pip install -r requirements.txt
  ```
## Step 4: generate migrations

  ```
  python manage.py makemigrations

  python manage.py migrate

  ```

## Step 5: Run the project

  ```
  python manage.py runserver

  ```

## Step 5: Run the tests

- Go to settings.py and uncomment the code on line 95 (# DATABASES['default'] = DATABASES['test'])

- generate migrations for tests 

  ```  
  python manage.py migrate --database=test

  ```

- Run basics tests from "lizetest\accounts\tests.py"

  ```  
  python manage.py test

  ```


<hr/>


## Author

:man: **Tiago Oliveira**

- [GitHub](https://github.com/TiagoOliverDev/)
- [LinkedIn](https://www.linkedin.com/in/tiago-oliveira-49a2a6205/)

## 🤝 Contributing
- Contributions, issues, and feature requests are welcome!
- Feel free to check the [issues page](https://github.com/TiagoOliverDev/lizie/issues).

# Show your support
Give a ⭐ if you like this project!
