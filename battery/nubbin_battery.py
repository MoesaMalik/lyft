import battery
from datetime import datetime


class NubbingBattery(Battery):

    def __init(self, last_service_date, current_date):

        super().__init__(last_service_date)

        this.last_service_date = last_service_date
        this.current_date = current_date

    def needs_service(self):

        service_threshold = self.last_service_date.replace(
            year=self.last_service_date.year + 4)

        if service_threshold < datetime.today().date():
            return True

        else:

            return False
