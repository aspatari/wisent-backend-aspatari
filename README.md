## WISENT BACKEND ASPATARI
---

This is a  interview homework for Wisent.

Author: artur.spatari@gmail.com



## Scope

- [v] To Create a async CRUD for an Entity with data validation
- [v] To Retrieve data from a fakeapi with posts
  - List in async way
  - Post by Id in sync way 
- [v] To use stack Tornado + asyncio + uvloop
- [v] To Receive message via WebSocket and to store it in DB
- [v] To use git 
- [v] To provide DockerCompose



## Result

#### Core module 

Represent a bunch of files vitals for application working like ,settings, application it self and database connection

#### Common module

Represent a bunch a files used for abstractions ori mixins to respect DRY


##### Apps

List of domains 





### Endpoints

#### Post

HTTP GET `/v1/posts`

HTTP GET /v1/posts/<post_id:int>

#### Client

HTTP GET `/v1/clients`

HTTP POST `/v1/clients`

HTTP GET /v1/clients/<client_id:int>

HTTP PATCH /v1/clients/<client_id:int

HTTP DELETE /v1/clients/<client_id:int

#### Socket

WS /ws.



#### TODO

- [] Add Cache layer for post module
- [] Add logging
- [] Improve abstractions for endpoints
- [] Make a router based on route and method
- [] Implement mixins for CRUD operations
- [] Add error handler on top of
- [] Add way to build OpenApi documentation by code
- [] Add pagination and filter backend



### Develop
#### Local
```
cp env.template .env
poetry install
tmuxp load .
```
### Docker 
```
cp env.template .env
docker build -t wisent-backend .
```
