# CERN API - University of Essex Online (Secure Software Development - Computer Science) 
![CodeQL Analysis Badge](https://github.com/KieronHolmes/UoEo-SSDCS-API/workflows/CodeQL/badge.svg)
![Django Test Status](https://github.com/KieronHolmes/UoEo-SSDCS-API/workflows/Django%20Tests/badge.svg)

This GitHub repository contains code used in partial fulfilment of the Secure Software Development (Computer Science) module of the MSc Computer Science course at the University of Essex Online. This project aims to develop an API that enables researchers at CERN to safely store and access documents relating to the Large Hadron Collider experiments. The Django REST framework has been chosen to develop this project because of its security advantages over other common alternatives. This framework handles many common security issues, such as permission and user authentication and offers protection against OWASP 10 vulnerabilities such as cross-site scripting and SQL injection (Veracode, 2018).

## Table of Contents

- [1. Installation](#1-installation)
- [2. Endpoints](#2-endpoints)
  * [2.1. Authentication](#21-authentication)
  * [2.2. Registration](#22-registration)
  * [2.3. Documents](#23-documents)
  * [2.4. GDPR](#24-gdpr)
  * [2.5. Microservices](#25-microservices)
- [3. File Structure](#3-file-structure)
- [4. Usage](#4-usage)
  * [4.1. Registering a new user](#41-registering-a-new-user)
  * [4.2. Requesting Access/Refresh Tokens](#42-requesting-accessrefresh-tokens)
  * [4.3. Refreshing Access Tokens](#43-refreshing-access-tokens)
  * [4.4. Documents](#44-documents)
  * [4.4.1. Fetching Documents (List)](#441-fetching-documents-list)
  * [4.4.2. Fetching Documents (Specific)](#442-fetching-documents-specific)
  * [4.4.3. Creating Docuemnets](#443-creating-docuemnets)
  * [4.4.4. Updating Documents](#444-updating-documents)
  * [4.4.5. Deleting Documents](#445-deleting-documents)
- [5. Additional Endpoint Parameters](#5-additional-endpoint-parameters)
- [6. GDPR](#6-gdpr)
- [6.1 Making a Data Access Request](#61-making-a-data-access-request)
- [6.2 Making a Data Erasure Request](#62-making-a-data-erasure-request)
- [7. Microservice](#7-microservice)
- [8. Other Features](#8-other-features)
  * [8.1. Cross Origin Request Sharing (CORS)](#81-cross-origin-request-sharing-cors)
  * [8.2. Request Throttling](#82-request-throttling)
  * [8.3. Password Validation](#83-password-validation)
  * [8.4. Field Encryption](#84-field-encryption)
- [9. Testing](#9-testing)
- [10. Contributors](#10-contributors)
- [11. External Packages and Modules Used](#11-external-packages-and-modules-used)
- [12. References](#12-references)

## 1. Installation

Once you have downloaded/cloned this repository, please set this folder as your current working directory and follow the below instructions ( Windows, [Alternative Operating Systems](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)):

**Create a new Virtual Environment:**

```zsh
python -m venv env
```

**Enter the Virtual Environment:**

```zsh
.\env\Scripts\activate
```

**Install dependencies required by this application:**

```zsh
pip install -r requirements.txt
```
**Apply migrations:**

```zsh
python manage.py migrate
```
**Running the Django Server:**

```zsh
python manage.py runserver
```

## 2. Endpoints

All API endpoints for the CERN API application are available at the `/api/v1/{endpoint}` path of the domain Django is listening on (In the case of localhost, this will likely be `http://127.0.0.1:8000/api/v1/`). With `{endpoint}` representing one of the endpoints listed in the below tables.

### 2.1. Authentication

Endpoint | HTTP Method | Action | Validity
-- | -- | -- | --
`authentication/token` | POST | Fetches access and refresh tokens for the user with the provided login credentials. | 1 hour
`authentication/token/refresh` | POST | Fetches a new access token for the user associated with the supplied refresh token. | 1 day

### 2.2. Registration

Endpoint | HTTP Method | Action 
-- | -- | --
`authentication/register` | POST | Registers a new user with the provided login credentials.

### 2.3. Documents
Endpoint | HTTP Method | CRUD Method | Action | Authorization Method
-- | -- | -- | -- | --
`documents` | GET | READ | Returns all research documents the current user has access to. | BEARER token.
`documents/<str:id>` | GET | READ | Returns a single research document with the provided ID. | BEARER token.
`documents` | POST | CREATE | Creates a new research document. | BEARER token.
`documents/<str:id>` | PUT | UPDATE | Updates a research document with the provided ID. | BEARER token.
`documents/<str:id>` | DELETE | DELETE | Deletes the research document with the provided ID. | BEARER token.

### 2.4. GDPR

Endpoint | HTTP Method | Action 
-- | -- | --
`gdpr/access-request` | GET | Returns all data held on user.
`gdpr/erasure-request` | DELETE | Deletes all user data.

### 2.5. Microservices

Endpoint | HTTP Method | Action 
-- | -- | --
 `microservices/<str:query>` | GET | Returns a list for a search string.

## 3. File Structure

```
├── CernAPI
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── LICENSE
├── README.md
├── authentication
│   ├── __init__.py
│   ├── apps.py
│   ├── lists
│   │   └── 10k-most-common.txt
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── documents
│   ├── __init__.py
│   ├── apps.py
│   ├── filters.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── pagination.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── gdpr
│   ├── __init__.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── microservice
│   ├── __init__.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── schema.yml
└── welcome
    ├── __init__.py
    ├── admin.py
    ├── static
    │   └── assets
    │       └── dist
    │           └── css
    │               ├── bootstrap.min.css
    │               └── cover.css
    ├── templates
    │   └── welcome
    │       └── welcome.html
    └── views.py
```

## 4. Usage


Detailed instructions on how to execute specific actions within this CERN API have been included below. 

**Please Note:** Instructions are provided for the Swagger User Interface and the Command Line Interface.

The HTTP client has been included in the 'requirements.txt' file (earlier installed) to enable testing from the command line.

To access the Swagger user interface, navigate to http://127.0.0.1:8000 or localhost:8000, then click API documentation. 

### 4.1. Registering a new user

**Please Note:** Defined roles are "admin", "researcher" and "employee". A researcher can create a new document 
as well as read, update and delete their own documents while an admin or employee has higher privileges to perform all functions on 
all documents in the system.

**From the Swagger User Interface**

Scroll to the register section, click try it out at the right corner, then enter username, password, email address and role. 

**From the Command Line Interface**

```bash
http POST http://127.0.0.1:8000/api/v1/authentication/register/ username="{username}" password="{password}" email="{email}"
```

### 4.2. Requesting Access/Refresh Tokens
**`{access_token}`** is the access token provided by the `/authentication/token/` or `/authentication/token/refresh/` endpoint. By default, access tokens have a **1** hour lifetime before they will need to be refreshed using the `/authentication/token/refresh/` endpoint using the `{refresh_token}` value (**1 day lifetime**).

**Please Note:** [Refresh Token Rotation](https://auth0.com/docs/security/tokens/refresh-tokens/refresh-token-rotation) has been implemented in this application; therefore requesting a new access token using the `/authentication/token/refresh/` endpoint will result in a new `{access_token}` value.


**STEPS:**
First, you have to log in with the newly created username and password.

**From the Swagger User Interface**

Enter details under the API section, then click execute.

**From the Command Line Interface**
```bash
http POST http://127.0.0.1:8000/api/v1/authentication/token/ username="{username}" password="{password}"
```
**`{username}`** is the username associated with the account you wish to use.
**`{password}`** is the password associated with the account you wish to use.

After successful login, access and refresh tokens are generated.

### 4.3. Refreshing Access Tokens

**From the Swagger User Interface**

Scroll to token refresh under the API section, click "Try it out" on the right corner.
Enter the refresh token generated in the previous section.
Click Execute

**From the Command Line Interface**
```bash
http POST http://127.0.0.1:8000/api/v1/authentication/token/refresh/ refresh="{refresh_token}"
```

**`{refresh_token}`** is provided by the ``/api/v1/authentication/token/refresh`` endpoint and is used to regenerate a new access token when 1 hour period has elapsed on the original token. The refresh token value is valid for 1 day from the point of generation.

### 4.4. Documents
The user must be authorised using the access token before any CRUD functionalities can be carried out from the document endpoint.

**From the Swagger User Interface**

Copy access token from the API section.
Click "Authorise" at the top right corner of the page.
Enter access token and click log in. 

### 4.4.1. Fetching Documents (List)

**From the Swagger User Interface**

Scroll to Document Section, then click "Try it out" on the right corner.
Click execute to return all documents created by the logged-on user.

**From the Command Line Interface**
```bash
http http://127.0.0.1:8000/api/v1/documents/ "Authorization: Bearer {access_token}"
```
### 4.4.2. Fetching Documents (Specific)

**From the Swagger User Interface**

Scroll to the relevant section under the Document heading, then click "Try it out" on the right corner.
Enter Document id.
Click execute to return the document that matches the id entered.

**From the Command Line Interface**
```bash
http http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```

**`{document_id}`** is the version 4 UUID value associated with a particular document that has been created within the API.

### 4.4.3. Creating Documents

**From the Swagger User Interface**

Scroll to the relevant section, then click "Try it out" on the right corner.
Enter document title and document content.
Click execute to create a new document.

**Please Note: A unique document id, date and time of creation is automatically generated for every document created**

**From the Command Line Interface**

```bash
http POST http://127.0.0.1:8000/api/v1/documents/ "Authorization: Bearer {access_token}"
```

### 4.4.4. Updating Documents

**From the Swagger User Interface**

Scroll to the relevant section, then click "Try it out" on the right corner.
Enter document id.
Make changes to the "document title" and "document content" fields as desired.
Click execute to display changes to the document.

**From the Command Line Interface**

```bash
http {PATCH/PUT} http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```

**`{PATCH/PUT}`** refers to the appropriate HTTP verb based on the data you wish to amend. ``PATCH`` should be used for a partial update, whereas ``PUT`` should be used for a full update.
**`{document_id}`** is the version 4 UUID value associated with a particular document that has been created within the API.

### 4.4.5. Deleting Documents

**From the Swagger User Interface**

Scroll to the relevant section, then click "Try it out" on the right corner.
Enter document id, then click execute

**From the Command Line Interface**
```bash
http DELETE http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```

**`{document_id}`** is the version 4 UUID value associated with a particular document that has been created within the API.

## 5. Additional Endpoint Parameters

This solution contains **pagination** and **filter** functionalities, which can be used on all endpoints used to fetch large volumes of data (For example `/api/v1/documents/`).

**Pagination**

The **pagination** parameter can be used to return a smaller dataset for endpoints that return large data volumes. This can assist consuming applications by reducing the overall load/processing time of an API request.

GET Parameter | Example | Description
-- | -- | --
`page` | `/api/v1/documents/?page=2` | The page number of the data you wish to fetch from the API. This value should be numeric. If this parameter is not supplied, the default will be **1**.
`page_size` | `/api/v1/documents/?page_size=10` | The maximum number of items you wish the API to return in its response. If not supplied, the API will default to returning **5** items; the maximum number which can be returned is **25**.

**Filtering**

The filtering functionality can be used to isolate records that match a specific set of criteria (For example, only documents created by John Doe). The filters can be applied by adding the required GET parameter to the end of the endpoint URL (For example, `/api/v1/documents/?owner__username=Joe`). Filters can be combined to narrow a search down  even further, for example `/api/v1/documents/?owner__username=Kieron&title=hadron`. As `document_content` is an encrypted field, this is not usable within the filter query.

**Examples**

GET Parameter | Example | Search Method | Description
-- | -- | -- | --
`title` | `/api/v1/documents/?title=hadron` | `icontains` | The title filter will return any values which contain a partial match to the title stored in the database. For example, the supplied example endpoint will return records containing the word hadron, such as "large hadron collider" and "hadron research".
`owner__username` | `/api/v1/documents/?owner__username=Joe` | `icontains` | The owner username filter will return any records which contain a full match to the owner username stored within the database.

## 6. GDPR
A user can request for all of their personal data held by the CERN API through a data access request. This will return all users personal details and the documents owned by the user.  A user could also request for their data to be deleted, including their account. 

## 6.1 Making a Data Access Request

**From the Swagger User Interface**

Scroll to the relevant section under GDPR, then click "Try it out" on the right corner.
Click execute to return all data held on the logged-on user.

**From the Command Line Interface**
```bash
http GET http://127.0.0.1:8000/api/v1/gdpr/access-request/ "Authorization: Bearer {access_token}"
```

## 6.2 Making a Data Erasure Request

**From the Swagger User Interface**

Scroll to the relevant section under GDPR, then click "Try it out" on the right corner.
Click execute to delete all data held on the logged-on user.
**Please Note:** the user account will be deleted and the user will be automatically logged out.

**From the Command Line Interface**
```bash
http DELETE http://127.0.0.1:8000/api/v1/gdpr/erasure-request/ "Authorization: Bearer {access_token}"
```

## 7. Microservice
The CERN API has a feature that can query an external CERN document server using a search string.
**From the Swagger User Interface**

Scroll to the Microservice section, then click "Try it out" on the right corner
Enter search string
Click execute to return a list of documents on CERN document server matching the search string entered.

**From the Command Line Interface**
```bash
http GET http://127.0.0.1:8000/api/v1/microservice/{query}/ "Authorization: Bearer {access_token}"
```
**`{query}`** represents the search term you wish to search for within the remote CERN Document Repository.

## 8. Other Features
This application includes a variety of additional security functions/features, all of which are listed within this section.

### 8.1. Cross-Origin Request Sharing (CORS)
CORS headers are automatically added to responses from this application through Django middleware. By default, only two origins are allowed:

```
'http://127.0.0.1:8000',
'http://localhost:8000',
```

To add additional origins, you should add the root URL to the `CORS_ALLOWED_ORIGINS` directive within the `settings.py` file.

### 8.2. Request Throttling

To prevent brute force attacks, this application enforces request throttling to ensure long-term availability and prevent abuse of resources. By default, Authenticated users are restricted to **100 requests per hour**, whereas non-authenticated users are restricted to **50 requests per hour**.

This value can be changed by editing the `DEFAULT_THROTTLE_RATES` attribute of the `REST_FRAMEWORK` directive within the `settings.py` file.

### 8.3. Password Validation

To prevent users from supplying commonly used passwords, upon registering for an account, the provided password is checked against a list of [10k of the most commonly used passwords](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10k-most-common.txt). In the event the user's password is contained on this list, the register function will throw a ValidationError and display the appropriate output to the user.

In addition, the password field has been implemented with a regex such that it must be between 8 and 18 characters; A mixture of both uppercase and lowercase letters; A mixture of letters and numbers; and at least one special character (@$!%*#?&) is required

### 8.4. Field Encryption

In order to protect the sensitive research information provided by CERN researchers, the `document_content` field within the `documents` table is stored in an encrypted format. This is decrypted on runtime to fulfil API requests requiring such information.

A new value should be supplied for the `FIELD_ENCRYPTION_KEY` attribute within the `settings.py` file in a production environment. This is comprised of a Base64 encoded random 32 digit string, which can be generated using the following Python code:

```python
import os,base64

print(base64.urlsafe_b64encode(os.urandom(32))
```

This function uses a form of **Symmetric Encryption** provided by the **Fernet** module of the Python **cryptography** library. In order for an attacker to gain access to the content, they would need to know/crack the encryption key.

## 9. Testing

A comprehensive test suite has been built in accordance with the [Django Rest Framework Documentation](https://www.django-rest-framework.org/api-guide/testing/). In order to execute the supplied test suite, please execute the following command:

```zsh
python manage.py test
```

**Please Note:** This repository uses GitHub workflows to manage automated testing on various operating systems and Python versions. All Pull Requests will only be approved if the Django tests are passing on all environments.

Python Version | Operating System
-- | --
Python 3.7 (x64) | `ubuntu-latest`, `macos-latest`, `windows-latest`
Python 3.8 (x64) | `ubuntu-latest`, `macos-latest`, `windows-latest`
Python 3.9 (x64) | `ubuntu-latest`, `macos-latest`, `windows-latest`
Python 3.10 (x64) | `ubuntu-latest`, `macos-latest`, `windows-latest`

## 10. Contributors

* [Kieron Holmes](https://github.com/KieronHolmes) - MSc Computer Science, University of Essex Online
* [Sergio Zavarce](https://github.com/SerZav) - MSc Computer Science, University of Essex Online
* [Kikelomo Obayemi](https://github.com/kikeobayemi) - MSc Computer Science, University of Essex Online

## 11. External Packages and Modules Used
* [Django](https://github.com/django/django) - Web Framework providing ORM functionality.
* [Django REST Framework](https://github.com/encode/django-rest-framework) - REST Framework built upon the Django web framework.
* [Django Filter](https://github.com/carltongibson/django-filter/) - Module providing the ability to filter models when executing a query.
* [Django REST Framework - Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt/) - Module providing the facility to use JWT for user authentication.
* [HTTPie](https://github.com/httpie/httpie) - Simple CLI HTTP client used for testing.
* [DRF-Spectacular](https://github.com/tfranzel/drf-spectacular) - Utility to provide the Swagger interface to the API.
* [Faker](https://github.com/joke2k/faker) - Provides the facility to quickly get random data in a certain format (Emails, Phone Numbers etc.)
* [Factory Boy](https://github.com/FactoryBoy/factory_boy) - Provides the facility to implement Model Factories for testing.
* [Django Encrypted Fields](https://gitlab.com/lansharkconsulting/django/django-encrypted-model-fields/) - Provides the ability to have encrypted fields within a Django model.

## 12. References
* Veracode (2018) How Secure Are Popular Web Frameworks? Here Is a Comparison. Available from:https://www.veracode.com/blog/secure-development/how-secure-are-popular-web-frameworks-here-comparison [Accessed 14 October 2021]
