# Sovelluslogiikka

```mermaid
 classDiagram
      UserService "*" --> "1" User
      class User{
          username
          password
      }
      class UserService{
          file_path
          users
      }
```


