class MainMenu:


    OPTION_MENU = {
        '1': show_members,
        '2': available_slots
    }

    @classmethod
    def default_method(cls, *args, **kwargs):
        print('HELP MENU')

    @classmethod
    def show_options(cls,  current_user):
        option = input()
        method_name = cls.OPTION_MENU.get(option, cls.default_method)
        method_name(**{})
        # TODO decide what you want in this dict

        # if option == '1':
        #     members = MainController.show_members(current_user)
        #     cls._pretty_print_members(members)

    @classmethod
    def  _pretty_print_members(cls, members):
        for member in members:
            print('{status} {username}'.format(
                status=getattr(member, 'status', ''),
                username=member.username
            ))