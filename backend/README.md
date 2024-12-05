## **MongoDB Installation & Setup**

### **Step 1: Install MongoDB**

#### For macOS:
1. Install MongoDB Community Edition using Homebrew:
   ```
    brew install mongodb-community@8.0
   ```
2. Start MongoDB as a background service:
```
brew services start mongodb-community@8.0
```
3. Command to Stop MongoDB as a background service:
```
brew services stop mongodb-community@8.0
```
#### For Windows :
Check documentation here : https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

### **Step 2: Set Up MongoDB Database and Collection**
```
mongosh
```
Create a new database called user_db:
```
use user_db
```
Check if db is created:
```
show dbs
```
Create the users collection:
```
db.createCollection("users")
```
(Optional) Insert a sample document to verify:
```
db.users.insertOne({
    first_name: "Test",
    last_name: "User",
    email: "test@example.com",
    phone: "1234567890",
    password: "password123"
})
```

Verify the collection and document:
```
db.users.find().pretty()
```

## **Project Setup**
Set up a virtual environment:
```
python -m venv myvenv
source myvenv/bin/activate    # On macOS/Linux
myvenv\Scripts\activate       # On Windows
```
Install dependencies:
```
pip install -r requirements.txt
```
To check the APIs from postman:

### Register User API:

   Method: POST
   URL: http://localhost:5000/api/register

   Body(raw):
  ```
   {
    "first_name": "Test",
    "last_name": "Test",
    "email": "test@example.com",
    "password": "password123"
   }

  ```

### Login API:

   Method: POST
   URL:  http://localhost:5000/api/login

   Body(raw):
   ```
   {
       "email": "test@example.com",
    "password": "password123"
   }

   ```

