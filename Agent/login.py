import bcrypt
import getpass

class LoginAgent:

    @staticmethod
    def hash_password(password):

        salt = bcrypt.gensalt()

        hashed = bcrypt.hashpw(
            password.encode(),
            salt
        )

        return hashed.decode()


    @staticmethod
    def verify_password(password, password_hash):

        return bcrypt.checkpw(
            password.encode(),
            password_hash.encode()
        )
    
    @classmethod
    def authenticate(cls, db):

        db.create_users_table()

        # First setup
        if db.count_users() == 0:

            print("First run setup")
            print("Create admin account")

            username = input("username: ")

            password = getpass.getpass(
                "password: "
            )

            password_hash = cls.hash_password(
                password
            )

            db.create_user(
                username,
                password_hash
            )

            print("Admin created.")
            return True

        # Login
        print("Login required")

        username = input("username: ")

        password = getpass.getpass(
            "password: "
        )

        user = db.get_user(username)

        if not user:
            print("User not found")
            return False

        stored_hash = user[1]

        if cls.verify_password(
            password,
            stored_hash
        ):
            print("Login successful")
            return True

        print("Wrong password")
        return False    