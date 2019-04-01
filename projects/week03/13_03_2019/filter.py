def filter(filename, full_name=None, favourite_color=None, 
           company_name=None, email=None, phone_number=None,
           salary=None, full_name__startswith=None, email__contains=None, 
           salary__gt=None, salary__lt=None, order_by=None):
    file = open(filename, 'r')
    print(file.readline())


if __name__ == "__main__":
    filter('example_data.csv')