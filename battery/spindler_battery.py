from datetime import datetime
from battery import Battery


class SpindlerBattery(Battery):

    def __init__(self, last_service_date):

        super().__init__(last_service_date)
        self.last_service_date = last_service_date

    def needs_service(self):
        service_threshold = self.last_service_date.replace(
            year=self.last_service_date.year + 3)

        return service_threshold < datetime.today().date()

