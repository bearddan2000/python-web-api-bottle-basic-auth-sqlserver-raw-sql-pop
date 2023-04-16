# python-web-api-bottle-basic-auth-sqlserver-raw-sql-pop

## Description
Creates an api of `pop` by using raw sql for a bottle project.
Has the ability to query by parameters.

Remotely tested with *testify*.
Requires basic authentication for endpoints.

| username | password |
| -------- | -------- |
| *user* | *pass* |

## Tech stack
- python
  - bottle
  - sqlalchemy
  - testify
  - requests
- mssql

## Docker stack
- python:latest
- mcr.microsoft.com/mssql/server:2017-CU17-ubuntu

## To run
`sudo ./install.sh -u`
- Get all pops: http://localhost/pop
  - Schema id, name, and color
- CRUD opperations
  - Create: curl -i -X PUT localhost/pop/<id> -u 'user:pass'
  - Read: http://localhost/pop/<id> -u 'user:pass'
  - Update: curl -i -X POST localhost/pop/<id>/<name>/<color> -u 'user:pass'
  - Delete: curl -i -X DELETE localhost/pop/<id> -u 'user:pass'

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
