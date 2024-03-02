# data-privacy-vault
A flask service functioning as a Data Privacy Vault to keep sensitive information safe. The vault stores the data and controls who can access it, ensuring it's managed, watched, and used carefully. 

This service provides HTTP-based APIs to send sensitive data to be stored in the vault, receiving back a token that can later be used to retrieve the sensitive data by an authorized user/service.

The tokens and the corresponding data are stored on MongoDB on the backend. All the data stored on the backend is encrypted using a format-preserving FF3 algorithm. Using format-preserving encryption makes integrating the data vault into an existing application easier. 
<br />Using encryption alone is a possible but undesirable alternative to using such data vaults.  

To keep the information safe, the vault supports data access only to authenticated users. 

### Project Support Features
* Endpoints for new user signup and user login.
* Public (non-authenticated) users are restricted from accessing data from the vault.
* Encryption of the data on the backend.  
* Format-preserving encryption to make the integration with the application easier.
* Persistent storage using MongoDB

### Installation Guide
* Clone this repository [here](https://github.com/kushkul/data-privacy-vault.git).
* ```cd data-privacy-vault```
* Install dependencies from requirements.txt
* Setup and start MongoDB database on local.
* Export environment file location by exporting ENV_FILE_LOCATION variable to ./.env
* Create an .env file in your project root folder and add your variables. See .env for assistance.
* Launch: ```python run.py``` 

### Usage
* Follow the above instructions to start the application.
* Connect to the API using Postman on port 8000.

### API Endpoints
| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| POST | /api/user/signup | To sign up a new user account |
| POST | /api/user/login | To login an existing user account |
| POST | /api/causes | To create a new cause |
| GET | /api/causes | To retrieve all causes on the platform |
| GET | /api/causes/:causeId | To retrieve details of a single cause |
| PATCH | /api/causes/:causeId | To edit the details of a single cause |
| DELETE | /api/causes/:causeId | To delete a single cause |
