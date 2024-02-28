import abc


class ElectricityMapsInterface(abc.ABC):
    @abc.abstractmethod
    def report(self) -> None:
        """
        time_interval == latest :
        ------------------
            Carbon intensity:
                    This endpoint retrieves the last known carbon intensity (in gCO2eq/kWh) of
                    electricity consumed in an area. It can either be queried by zone identifier or by geolocation.
        ------------------
            Power_breakdown:
                    This endpoint retrieves the last known data about the origin of electricity in an area.
        ==========================
        time_interval == history :
        ------------------
            Carbon intensity:
                    This endpoint retrieves the last 24 hours of carbon intensity (in gCO2eq/kWh) of an area.
                    It can either be queried by zone identifier or by geolocation.
                    The resolution is 60 minutes.
        ------------------
            Power_breakdown:
                    This endpoint retrieves the last 24 hours of power consumption
                    and production breakdown of an area, which represents the physical
                    origin of electricity broken down by production type. It can either
                    be queried by zone identifier or by geolocation.
                    The resolution is 60 minutes.
        """

    @abc.abstractmethod
    def present_report_humanly_readable(self) -> str:
        """
        This method represent data from report method in a readable way when applied.
        """
