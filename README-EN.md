# API for Energens.

I will explain first, what is Energens. Energens, an engineering company, works with engineering services in general, installing photovoltaic energy. We have a problem involving solar systems, which is monitoring several plants, creating a huge database, with records, depending on the name, customer, size of the system, part of the data forecast. So I decided to create an API to help in the process of automating functions and automatic calculations, created by the front-end, which will be developed later.

## Files that make up the system for Resources and Models

### Explanation of the models used

These database fields will be located within the table. The "id" and "customer" will be the primary keys for searches made.
The method "__init __ ()" instance the database and its serialized resources, the method "json ()" creates the display of the data through JSON to facilitate the visualization of the API, which the API standard today is to use JSON to send the serial information.
So we enter the class methods which work the same in all models, they would be:

   - find
   - save
   - update
   - delete
  
These methods are basic to all models, a brief explanation of them will be covered.
"Find": Search method, it is used to search the database for an "id" or "city" and return the value or return nothing to JSON.
"Save": Method of saving to the database, it adds information and saves the information in the database.
"Update": Method of updating the database, passing information like which will be modified.
"Delete": Method of deleting information by "id" or "city" in the database.


### Explanation of features

#### Get

The "get" function is to return a specific "id" or "city" with the entire set of information.

#### Post

The "post" has the means of posting a new request in the system, following its parameters of "JSON", in this case without using the id again, as this goes through the serial method already included, if that id is already busy it sends the message to the customer, saying that the id already exists.

#### Put

The "put" has the function of updating an existing "id" or "city".

#### Delete
    
The "delete" function is to delete the selected "id" or "city".

1. [Access password template](models/accessPassword.py) and [Access password features](resources/accessPassword.py)

    #### Model
    
    The model, creates the database with the following fields:
  
       - id
       - customer
       - portal
       - user
       - password
   
   #### Resources
   
   

2. [Cleaning Model](models/cleanings.py) and [Cleaning Resources](resources/cleanings.py)

3. [Consolidated model](models/consolidated.py) and [Consolidated resources](resources/consolidated.py)

4. [Customer Registration Template](models/customerRegistration.py) and [Customer Registration Resources](resources/customerRegistration.py)

5. [Internet password record template](models/internetPasswords.py) and [Internet password record resource](resources/internetPasswords.py)

6. [Inverter registration model](models/inverter.py) and [Inverter registration resources](resources/inverter.py)

7. [Local irradiation model](models/localIrradiation.py) and [Local irradiation resources](resources/localIrradiation.py)

8. [Generation forecast model](models/predicted.py) and [Generation forecast resources](resources/predicted.py)