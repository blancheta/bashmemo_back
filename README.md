## Init DB

```
CREATE DATABASE bashmemo;
CREATE USER adminbu with PASSWORD 'password';
ALTER ROLE "adminbu" WITH LOGIN;
GRANT ALL PRIVILEGES ON DATABASE bashmemo TO adminbu;
```