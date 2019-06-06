class MainMenu:
    OPTION_MENU_DOCTOR = 
    {
        '1' : show_patients,
        '2' : my_slots,
        '3' : available_slots,
        '4' : search_user_by_name 
        #on show users all info abput patient should be displayed
    }

    OPTION_MENU_PATIENT = 
    {
        '1': show_doctors,
        '2': search_doctor_by_name,
        '3': search_doctor_by_specialty,
        '4': make_reservation,
        '5': show_my_reservations
    }

    @classmethod
    def show_options(cls, current_user):
        pass