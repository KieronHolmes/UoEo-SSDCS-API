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
* [4. Additional Endpoint Parameters]()
* [5. Testing]()
* [6. Contributors]()
* [7. External Packages and Modules Used]()

## 1. Installation

Once you have downloaded/cloned this repository, please set this folder as your current working directory and follow the
below instructions (
Windows, [Alternative Operating Systems](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)):

**Create a new Virtual Environment:**

```zsh
python -m venv venv
```

**Enter the Virtual Environment:**

```zsh
.\venv\Scripts\activate
```

**Install dependencies required by this application:**

```zsh
pip install -r requirements.txt
```

**Running the Django Server:**

```zsh
python manage.py runserver
```

## 2. Endpoints

All API endpoints for the CERN API application are available at the `/api/v1/{endpoint}` path of the domain Django is
listening on (In the case of localhost, this will likely be `http://127.0.0.1:8000/api/v1/`). With `{endpoint}`
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

Detailed instructions on how to execute specific actions within this CERN API have been included below. **Please Note:**
All instructions are based on using the HTTPie client on a development (localhost) copy of the application.

**`{access_token}`** is the access token provided by the `/authentication/token/`
or `/authentication/token/refresh/` endpoint. By default, access tokens have a **1** hour lifetime before they will need
to be refreshed using the `/authentication/token/refresh/` endpoint using the `{refresh_token}` value (**1 day
lifetime**).

**Please Note:** [Refresh Token Rotation](https://auth0.com/docs/security/tokens/refresh-tokens/refresh-token-rotation)
has been implemented in this application, therefore requesting a new access token using
the `/authentication/token/refresh/` endpoint will result in a new `{access_token}` value.

### 3.1 Registering a new user

**NOT YET IMPLEMENTED** - Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et
malesuada fames ac ante ipsum primis in faucibus.

```bash
http http://127.0.0.1:8000/api/v1/authentication/register/
```

### 3.2 Requesting Access/Refresh Tokens

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum
primis in faucibus.

```bash
http http://127.0.0.1:8000/api/v1/authentication/token/ username="{username}" password="{password}"
```

**`{username}`** is the username associated with the account you wish to use.
**`{password}`** is the password associated with the account you wish to use.
### 3.3 Refreshing Access Tokens
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum primis in faucibus.
```bash
http http://127.0.0.1:8000/api/v1/authentication/token/refresh/ refresh="{refresh_token}"
```

**`{refresh_token}`** is provided by the ``/api/v1/authentication/token/`` endpoint and is used to regenerate a new
access token. The refresh token value is valid for 1 day from the point of generation.
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

**`{document_id}`** is the version 4 UUID value associated with a particular document which has been created within the
API.
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

**`{PATCH/PUT}`** refers to the appropriate HTTP verb based on the data you wish to amend. ``PATCH`` should be used for
a partial update, whereas ``PUT`` should be used for a full update.
**`{document_id}`** is the version 4 UUID value associated with a particular document which has been created within the
API.

### 3.8 Deleting Documents

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras eget sem turpis. Interdum et malesuada fames ac ante ipsum
primis in faucibus.

```bash
http DELETE http://127.0.0.1:8000/api/v1/documents/{document_id} "Authorization: Bearer {access_token}"
```

**`{document_id}`** is the version 4 UUID value associated with a particular document which has been created within the
API.

## 4. Additional Endpoint Parameters

This solution contains **pagination** and **filter** functionalities, which can be used on all endpoints used to fetch
large volumes of data (For example `/api/v1/documents/`).

### 4.1. Pagination

The **pagination** parameter can be used to return a smaller dataset for endpoints which return large volumes of data.
This can assist consuming applications by reducing the overall load/processing time of an API request.

GET Parameter | Example | Description
-- | -- | --
`page` | `/api/v1/documents/?page=2` | The page number of the data you wish to fetch from the API. This value should be
numeric. If this parameter is not supplied, the default will be **1**.
`page_size` | `/api/v1/documents/?page_size=10` | The maximum number of items you wish the API to return in its
response. If not supplied, the API will default to returning **5** items, the maximum number which can be returned is **
25**.

### 4.2. Filtering

The filtering functionality can be used to isolate records that match a specific set of criteria (For example, only
documents created by John Doe). The filters can be applied by adding the required GET parameter to the end of the
endpoint URL (For example, `/api/v1/documents/?owner__username=Joe`). Filters can be combined to narrow a search down
even further, for example `/api/v1/documents/?owner__username=Kieron&title=hadron`.

#### 4.2.1 Documents

GET Parameter | Example | Search Method | Description
-- | -- | -- | --
`title` | `/api/v1/documents/?title=hadron` | `icontains` | The title filter will return any values which contain a
partial match to the title stored in the database. For example, the supplied example endpoint will return records that
contain the word hadron, such as "large hadron collider", "hadron research".
`document_content` | `/api/v1/documents/?document_content=lorem` | `iccontains` | The document content filter will
return any values which contain a partial match to the document content stored within the database.
`owner__username` | `/api/v1/documents/?owner__username=Joe` | `icontains` | The owner username filter will return any
records which contain a full match to the owner username stored within the database.

## 5. Testing

A comprehensive test suite has been built in accordance with
the [Django Rest Framework Documentation](https://www.django-rest-framework.org/api-guide/testing/). In order to execute
the supplied test suite, please execute the following command:

```zsh
python manage.py test
```

## 6. Contributors

* [Kieron Holmes](https://github.com/KieronHolmes) - MSc Computer Science, University of Essex Online
* [Sergio Zavarce](https://github.com/SerZav) - MSc Computer Science, University of Essex Online
* [Kikelomo Obayemi](https://github.com/kikeobayemi) - MSc Computer Science, University of Essex Online

## 7. External Packages and Modules Used
* [Django](https://github.com/django/django) - Web Framework providing ORM functionality.
* [Django REST Framework](https://github.com/encode/django-rest-framework) - REST Framework built upon the Django web framework.
* [Django Filter](https://github.com/carltongibson/django-filter/) - Module providing the ability to filter models when executing a query.
* [Django REST Framework - Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt/) - Module providing the facility to use JWT for user authentication.
* [HTTPie](https://github.com/httpie/httpie) - Simple CLI HTTP client used for testing.
