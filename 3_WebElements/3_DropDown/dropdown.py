from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


def select_dropdown():
    # Step 1: launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 2: Open Webpage
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Step 3: Find Dropdown
    dropdown = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown"))))

    # Step 4: Find the default option
    # Test 1: Verify Default option selected or not
    # Get the Selected option and check if it is selected
    default_selected_option = dropdown.first_selected_option

    try:
        assert default_selected_option.is_selected, "Please select an option"
        print("Default option selected.Test Passed.")
    except AssertionError:
        print("Default option not selected.Test Failed")

    # Step 5: Select an Option
    dropdown.select_by_visible_text("Option 1")

    # Test 2: Verify option 1 selected or not
    new_selected_option = dropdown.first_selected_option
    try:
        assert new_selected_option.is_selected, "Option 1"
        print("Option 1 selected.Test Passed.")
    except AssertionError:
        print("Option 1 not selected.Test Failed")

    # Test 3: Verify all options available
    expected_options_list = ["Please select an option", "Option 1", "Option 2"]

    actual_options_list = []

    # iterate over all options available
    for option in dropdown.options:
        option_text = option.text
        actual_options_list.append(option_text)

    # Compare the actual options list to the expected
    try:
        assert actual_options_list == expected_options_list
        print("All options available.Test Passed")
    except AssertionError:
        print("All options are not available.Test Failed")
        print(actual_options_list)

    driver.close()


select_dropdown()
