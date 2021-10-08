# CERN API - University of Essex Online (Secure Software Development - Computer Science) ![CodeQL Analysis Badge](https://github.com/KieronHolmes/UoEo-SSDCS-API/workflows/CodeQL/badge.svg)

This GitHub repository contains code used in partial fufillment of the Secure Software Development (Computer Science)
module of the MSc Computer Science course delivered by the University of Essex Online. The code developed is intended to
fufil the weaknesses identified in the CERN case study supplied, regarding research materials collected as part of Large
Hadron Collider (LHC) experiments.

## Table of Contents

* [1. Installation]()
* [2. Endpoints]()
    - [2.1. Authentication]()
    - [2.2. Documents]()
* [3. Usage]()
    - [3.1. Registering a new user]()
    - [3.2. Requesting Access/Refresh Tokens]()
    - [3.3. Refreshing Access Tokens]()
    - [3.4. Fetching Documents (List)]()
    - [3.5. Fetching Documents (Specific)]()
    - [3.6. Creating Documents]()
    - [3.7. Updating Documents]()
    - [3.8. Deleting Documents]()
* [4. Testing]()
* [5. Contributors]()
* [6. External Packages and Modules Used]()

## 1. Installation

Once you have downloaded/cloned this repository, please set this folder as your current working directory and follow the
below instructions (Windows
- [Alternative Operating Systems](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)):

**Create a new Virtual Environment:**
```zsh
python -m venv venv
```

**Install dependencies required by this application:**
```zsh
pip install -r requirements.txt
```

## 2. Endpoints

All API endpoints for the CERN API application are available at the ``/api/v1/{endpoint}`` path of the domain Django is
listening on (In the case of localhost, this will likely be ``http://127.0.0.1:8000/api/v1/``). With ``{endpoint}``
representing one of the endpoints listed in the below tables.
### 2.1 Authentication
Endpoint | HTTP Method | Action
-- | -- | --
`authentication/register` | POST | Registers a new user with the provided login credentials.
`authentication/token` | GET | Fetches an access and refresh token for the user with the provided login credentials.
`authentication/token/refresh` | GET | Fetches a new access token for the user associated with the supplied refresh token.

### 2.2 Documents
Endpoint | HTTP Method | CRUD Method | Action | Authorization Method
-- | -- | -- | -- | --
`documents` | GET | READ | Returns all research documents the current user has access to. | BEARER token.
`documents/<str:id>` | GET | READ | Returns a single research document with the provided ID. | BEARER token.
`documents` | POST | CREATE | Creates an new research document. | BEARER token.
`documents/<str:id>` | PUT | UPDATE | Updates a research document with the provided ID. | BEARER token.
`documents/<str:id>` | DELETE | DELETE | Deletes the research document with the provided ID. | BEARER token.

## 3. Usage
Detailed instructions on how to execute specific actions within this CERN API have been included below. **Please Note:** All instructions are based on using the HTTPie client on a development (localhost) copy of the application.

**``{access_token}``** is the access token provided by the ``/authentication/token/`` or ``/authentication/token/refresh/`` endpoint. By default, access tokens have a **5** minute lifetime before they will need to be refreshed using the ``/authentication/token/refresh/`` endpoint using the ``{refresh_token}`` value (**1 day lifetime**).
### 3.1 Registering a new user
**NOT YET IMPLEMENTED** - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/authentication/register/
```
### 3.2 Requesting Access/Refresh Tokens
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/authentication/token/ username="{username}" password="{password}"
```
**``{username}``** is the username associated with the account you wish to use.
**``{password}``** is the password associated with the account you wish to use.
### 3.3 Refreshing Access Tokens
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/authentication/token/refresh/ refresh="{refresh_token}"
```
**``{refresh_token}``** is provided by the ``/api/v1/authentication/token/`` endpoint and is used to regenerate a new access token. The refresh token value is valid for 1 day from the point of generation.
### 3.4 Fetching Documents (List)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/documents/ "Authorization: Bearer {access_token}"
```
### 3.5 Fetching Documents (Specific)
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```
**``{document_id}``** is the version 4 UUID value associated with a particular document which has been created within the API.
### 3.6 Creating Documents
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http POST http://127.0.0.1:8000/api/v1/documents/ "Authorization: Bearer {access_token}"
```
### 3.7 Updating Documents
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http {PATCH/PUT} http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```
**``{PATCH/PUT}``** refers to the appropriate HTTP verb based on the data you wish to amend. ``PATCH`` should be used for a partial update, whereas ``PUT`` should be used for a full update.
**``{document_id}``** is the version 4 UUID value associated with a particular document which has been created within the API.

### 3.8 Deleting Documents
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http DELETE http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```
**``{document_id}``** is the version 4 UUID value associated with a particular document which has been created within the API.
## 4. Testing
A comprehensive test suite has been built in accordance with the [Django Rest Framework Documentation](https://www.django-rest-framework.org/api-guide/testing/). In order to execute the supplied test suite, please execute the following command:

```zsh
python manage.py test
```

## 5. Contributors
* [Kieron Holmes](https://github.com/KieronHolmes) - MSc Computer Science, University of Essex Online
* [Sergio Zavarce](https://github.com/SerZav) - MSc Computer Science, University of Essex Online
* [Kikelomo Obayemi](https://github.com/kikeobayemi) - MSc Computer Science, University of Essex Online

## 6. External Packages and Modules Used
* [Django](https://github.com/django/django) - Web Framework providing ORM functionality.
* [Django REST Framework](https://github.com/encode/django-rest-framework) - REST Framework built upon the Django web framework.
* [Django Filter](https://github.com/carltongibson/django-filter/) - Module providing the ability to filter models when executing a query.
* [Django REST Framework - Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt/) - Module providing the facility to use JWT for user authentication.
* [HTTPie](https://github.com/httpie/httpie) - Simple CLI HTTP client used for testing.
