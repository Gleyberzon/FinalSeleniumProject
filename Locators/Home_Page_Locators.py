from selenium.webdriver.common.by import By


class Personal:
    # Filld Personal Information
    fieldset_info = (By.XPATH, ".//fieldset[descendant::legend[.='Personal Information']]")
    # text inputs & selectors
    input_fname = (By.NAME, "fname")
    input_lname = (By.NAME, "lname")
    selector_city = (By.NAME, "City")
    input_email = (By.NAME, "email")
    selector_area_code = (By.NAME, "areaCode")
    input_tel = (By.NAME, "phone")
    # Radio
    radio_female = (By.CSS_SELECTOR, "td > input[type='radio'][value='F']")
    radio_mail = (By.CSS_SELECTOR, "td > input[type='radio'][value='M']")
    radio_other = (By.CSS_SELECTOR, "td > input[type='radio'][value='O']")
    # Checkboxes
    checkbox_math = (By.CSS_SELECTOR, "input[type='checkbox'][name='math']")
    checkbox_phisics = (By.CSS_SELECTOR, "input[type='checkbox'][name='pyhs']")
    checkbox_pop = (By.CSS_SELECTOR, "input[type='checkbox'][name='gender'][value='P']")
    checkbox_dud = (By.CSS_SELECTOR, "input[type='checkbox'][name='gender'][value='M']")
    checkbox_biology = (By.CSS_SELECTOR, "input[type='checkbox'][name='bio']")
    checkbox_chemistry = (By.CSS_SELECTOR, "input[type='checkbox'][name='chem']")
    checkbox_english = (By.CSS_SELECTOR, "input[type='checkbox'][name='eng']")

class HTML_Buttons:
    # Filld HTML buttons
    fieldset_html_btns = (By.XPATH, "//fieldset[descendant::legend[.='HTML Buttons']]")
    btn_clear = (By.ID, "CB")
    btn_send = (By.ID, "send")

class JS_Area:
    # Field JS Buttons
    fieldset_html_btns = (By.XPATH, "//fieldset[descendant::legend[.='JS Buttons']]")
    text_field = (By.ID, 'pbyuser')
    btn_set_text = (By.XPATH, ".//button[.='Set Text']")
    btn_start_loading = (By.XPATH, ".//button[.='Start loading']")
    text_status_loading = (By.ID, "startLoad")

class Links:
    # Field Links
    fieldset_html_btns = (By.XPATH, "//fieldset[descendant::legend[.='Links']]")
    link_next_page = (By.CSS_SELECTOR, "a[name='nextPage']")
    link_windy = (By.CSS_SELECTOR, "a[name='myLink']")
    link_tera_santa = (By.CSS_SELECTOR, "a[name='myLinkTS']")
    link_java_book = (By.XPATH, ".//a[.=Java Book]")
    link_youtube = (By.CSS_SELECTOR, ".//a[.=YouTube]")
