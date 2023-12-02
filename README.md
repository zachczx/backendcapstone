# backendcapstone

Admin is user: admin, password: password123


Backend MySQL
>       'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reservations',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'django',
        'PASSWORD' : 'password123',

Menu and table booking
> http://127.0.0.1:8000/menu/
> http://127.0.0.1:8000/book/

Menu and table booking APIs
> http://127.0.0.1:8000/menu-api/
> http://127.0.0.1:8000/booking-api/

User registration and authentication
> http://127.0.0.1:8000/api/users/
> http://127.0.0.1:8000/api/users/set_username/

Application unit test
> test.py (tests for Menu view and BookingForm)

Insomnia API (GET)
> http://127.0.0.1:8000/menu-api/
> http://127.0.0.1:8000/booking-api/