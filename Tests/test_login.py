from datetime import datetime

from PAT_Task_15.Utilities import excel_utilities
from PAT_Task_15.Utilities.excel_utilities import *
from PAT_Task_15.Pages.login_page import LoginPage

class TestOrangeHRMLogin:

    file_path= "PAT_Task_15/TestData/Testdata.xlsx"
    sheet = "Sheet1"

    def test_login_ddt(self,setup):
        driver = setup
        login_page = LoginPage(driver)

        rows = excel_utilities.get_row_count(self.file_path, self.sheet)

        for row in range(2, rows + 1):
            user_name = excel_utilities.read_data(self.file_path, self.sheet, row, 2)
            password = excel_utilities.read_data(self.file_path, self.sheet, row, 3)

            current_date = datetime.now().strftime("%d/%m/%Y")
            current_time = datetime.now().strftime("%H:%M:%S")

            login_page.login(user_name, password)

            if login_page.is_successful_login():
                excel_utilities.write_data(self.file_path, self.sheet, row, 4, current_date)
                excel_utilities.write_data(self.file_path, self.sheet, row, 5, current_time)
                excel_utilities.write_data(self.file_path, self.sheet, row, 7, "passed")

                login_page.logout()

            else:
                excel_utilities.write_data(self.file_path, self.sheet, row, 4, current_date)
                excel_utilities.write_data(self.file_path, self.sheet, row, 5, current_time)
                excel_utilities.write_data(self.file_path, self.sheet, row, 7, "failed")

            driver.refresh()


