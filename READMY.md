# Django Angular2 test project

Used: Django 1.10.2

Playground for experiment.

Contain blog rest api in djapp

##blog

Simple blog with REST interface

###Blog REST API

Used: Django REST framework 3.4.7

- user registration

    request: `POST`
    url: `/api/v1/user/reg/`
    fields: `email`, `password`, `first_name` and `last_name`

- user authentication

    request: `POST`
    url: `/api/v1/user/auth/`
    fields: `email_or_username` and `password`

    return: **`<token>`**

- user profile

    request: `GET`
    url: `/api/v1/user/`
    header: `Authorization: Token <token>`

- user posts list

    request: `GET`
    url: `/api/v1/user/posts/`
    header: `Authorization: Token <token>`

- all posts list with pagination

    request: `GET`
    url: `/blog/api/v1/post/`
    header: `Authorization: Token <token>`

- create new post

    request: `POST`
    url: `/api/v1/post/`
    header: `Authorization: Token <token>`
    fields: `title` and `text`

- search post by title

    request: `POST`
    url: `/api/v1/post/search/`
    header: `Authorization: Token <token>`
    fields: `query`
