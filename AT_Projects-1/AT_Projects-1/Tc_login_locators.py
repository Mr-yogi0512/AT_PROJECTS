# login button locators

class first_login:
    admin = "username"
    password_fail = "password"
    password_pass = "password"
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    username = 'username'
    invaild = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'


# TC LOGIN 3
class pim_page:
    pim_step = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    emp_click = '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    first_name = ('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div['
                  '1]/div[2]/input')
    last_name = ('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div['
                 '3]/div[2]/input')
    button_click = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    username_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    password_1 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    password_2 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    save_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    emp_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    search_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'

    record_found = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
    record_found_one = '(1) Record Found'
    id_code = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    employee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/h6'
    delete_id = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i'
    switch_alert = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'
    no_found_result = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/span'
