class MainController:

    @classmethod
    def sign_in(cls, username, password):
        cls._validate_password(password)
        password = cls._hash_password(password)
        current_user = User.find(username, password)
        return current_user

    @classmethod
    def sign_up(cls, username, password, second_password):
        cls._validate_password(password)
        cls._validate_password(second_password)

        hashed_pass1 = cls._hash_password(password)
        hassed_pass2 = cls._hash_password(second_password)
        cls._do_passwords_match(hashed_pass1, hassed_pass2)

        if UserGateway.find(username, password):
            raise UserAlreadyExistsError

        return User.create_new_user(username, hashed_pass1)

    @classmethod
    def show_members(cls, current_user):
        if current_user.is_doctor:
            return cls.show_patients(current_user)
            #  [Patient('Roza'), Patient('Mimi')]
        else:
            return cls.show_doctors(current_user)