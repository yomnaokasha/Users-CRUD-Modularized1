from flask_app.config.mysqlconnection import connectToMySQL


class User:
    def __init__(self, data):
        print(data)
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "select * from users;"
        results = connectToMySQL('mydb').query_db(query)
        users = []
        for row in results:
            users.append(User(row))
        return users

    @classmethod
    def add(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        # data = {
        #     "first_name": first_name,
        #     "last_name": last_name,
        #     "email": email,
        # }
        result = connectToMySQL('mydb').query_db(query, data)

        return result

    @ classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users where id = %(id)s;"
        result = connectToMySQL('mydb').query_db(query, data)
        return (cls(result[0]))

    @ classmethod
    def update_info(cls, data):
        query = "update users  set first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at = Now() where users.id = %(id)s;"
        return connectToMySQL('mydb').query_db(query, data)

    @ classmethod
    def delete(cls, data):
        query = "Delete FROM users where users.id = %(id)s;"
        return connectToMySQL('mydb').query_db(query, data)
