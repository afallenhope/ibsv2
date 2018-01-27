from fallen.models.user import User


class UserManager:
    __user = None

    def __init__(self, dbpath=None):
        self.dbpath = dbpath
        self.__user = User

    def install(self) -> None:
        self.__user.db.create_all()

    def uninstall(self) -> None:
        self.__user.db.drop_all()

    def create(self, name, username, email, password, active=False) -> str:
        found_user = User.query.filter_by(email=email, username=username).first()
        if found_user is None:
            user = User(id=None, name=name, username=username, email=email, password=password, active=active,
                        create_date=None, last_login=None)
            self.__user.db.session.add(user)
            self.__user.db.commit()
        else:
            return "I'm sorry there's already an account with that username or email"

    def remove(self, username) -> None:
        found_user = User.query.filter_by(username=username).first()
        if found_user is not None:
            self.__user.db.session.delete(found_user)
            self.__user.db.session.commit()
