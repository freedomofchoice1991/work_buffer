import requests
from interface import ElectricityMapsInterface
from energy_response_models import CarbonIntensityResponse, \
    PowerBreakdownResponse, \
    PowerConsumptionBreakdown, \
    PowerProductionBreakdown, \
    PowerImportBreakdown, \
    PowerExportBreakdown
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


class ElectricityMaps(ElectricityMapsInterface):
    ZONE = "DE"
    LIST_OF_ALL_AVAILABLE_ZONES = "zones"
    API_BASE_URL = "https://api.electricitymap.org"
    LATEST_DATA = "latest"
    HISTORY_DATA = "history"
    POWER_BREAKDOWN_ENDPOINT = "power-breakdown"
    CARBON_INTENSITY_ENDPOINT = "carbon-intensity"

    def __init__(self,
                 authentication_token,
                 selected_time_endpoint,
                 endpoint_type,
                 db_url,
                 estimation=True):
        # If no zone is detected (or we don't have data for that area),
        # the API will attempt to use your current location based on IP of the caller
        self.zone = ElectricityMaps.ZONE
        self.auth_token = authentication_token
        self.all_available_zones = ElectricityMaps.LIST_OF_ALL_AVAILABLE_ZONES
        if selected_time_endpoint == "latest":
            self.selected_time_endpoint = ElectricityMaps.LATEST_DATA
        elif selected_time_endpoint == "history":
            self.selected_time_endpoint = ElectricityMaps.HISTORY_DATA

        if endpoint_type == "power-breakdown":
            self.endpoint_type = ElectricityMaps.POWER_BREAKDOWN_ENDPOINT
        elif endpoint_type == "carbon-intensity":
            self.endpoint_type = ElectricityMaps.CARBON_INTENSITY_ENDPOINT
        # To disable estimations in the returned JSON, the estimation parameter can be set to false
        self.estimation = estimation
        self.API_url = ElectricityMaps.API_BASE_URL
        self.json_response: dict = {}
        self.db_url = db_url

    @contextmanager
    def session_scope(self):
        connection_engine = create_engine(self.db_url)
        Session = sessionmaker(bind=connection_engine)
        transaction_session = Session()
        try:
            yield transaction_session
            transaction_session.commit()
        except KeyboardInterrupt:
            transaction_session.rollback()
            raise ValueError('Interruption happened while connecting to DB.')
        finally:
            transaction_session.close()
            connection_engine.dispose()

    def report(self, ):
        url = f'{self.API_url}/v3/{self.endpoint_type}/{self.selected_time_endpoint}?zone={self.zone}'
        url = self.disable_estimation(url)
        response = requests.get(url)
        # Parse JSON response
        self.json_response = response.json()
        self.store_data()

    def store_data(self, ):
        # create session
        with self.session_scope() as response_session:
            # ================================================  store carbon-intensity data to DB
            if self.selected_time_endpoint == "latest" and self.endpoint_type == "carbon-intensity":
                carbon_intensity_response = CarbonIntensityResponse(self.json_response)
                response_session.add(carbon_intensity_response)

            if self.selected_time_endpoint == "history" and self.endpoint_type == "carbon-intensity":
                for item in self.json_response['history']:
                    carbon_intensity_response = CarbonIntensityResponse(item)
                    response_session.add(carbon_intensity_response)
            # ================================================  store power-breakdown data to DB
            if self.selected_time_endpoint == "latest" and self.endpoint_type == "power-breakdown":
                power_breakdown_response = PowerBreakdownResponse(self.json_response)

                # Add power consumption breakdown
                for source, value in self.json_response['powerConsumptionBreakdown'].items():
                    power_consumption_breakdown = PowerConsumptionBreakdown(source=source, value=value)
                    power_breakdown_response.power_consumption_breakdown.append(power_consumption_breakdown)

                # Add power production breakdown
                for source, value in self.json_response['powerProductionBreakdown'].items():
                    power_production_breakdown = PowerProductionBreakdown(source=source, value=value)
                    power_breakdown_response.power_production_breakdown.append(power_production_breakdown)

                # Add power import breakdown
                for source, value in self.json_response['powerImportBreakdown'].items():
                    power_import_breakdown = PowerImportBreakdown(source=source, value=value)
                    power_breakdown_response.power_import_breakdown.append(power_import_breakdown)

                # Add power export breakdown
                for source, value in self.json_response['powerExportBreakdown'].items():
                    power_export_breakdown = PowerExportBreakdown(source=source, value=value)
                    power_breakdown_response.power_export_breakdown.append(power_export_breakdown)

                response_session.add(power_breakdown_response)

            if self.selected_time_endpoint == "history" and self.endpoint_type == "power-breakdown":
                for item in self.json_response['history']:
                    power_breakdown_response = PowerBreakdownResponse(item)

                    # Add power consumption breakdown
                    for source, value in item['powerConsumptionBreakdown'].items():
                        power_consumption_breakdown = PowerConsumptionBreakdown(source=source, value=value)
                        power_breakdown_response.power_consumption_breakdown.append(power_consumption_breakdown)

                    # Add power production breakdown
                    for source, value in item['powerProductionBreakdown'].items():
                        power_production_breakdown = PowerProductionBreakdown(source=source, value=value)
                        power_breakdown_response.power_production_breakdown.append(power_production_breakdown)

                    # Add power import breakdown
                    for source, value in item['powerImportBreakdown'].items():
                        power_import_breakdown = PowerImportBreakdown(source=source, value=value)
                        power_breakdown_response.power_import_breakdown.append(power_import_breakdown)

                    # Add power export breakdown
                    for source, value in item['powerExportBreakdown'].items():
                        power_export_breakdown = PowerExportBreakdown(source=source, value=value)
                        power_breakdown_response.power_export_breakdown.append(power_export_breakdown)

                    response_session.add(power_breakdown_response)

    def present_report_humanly_readable(self):
        if self.selected_time_endpoint == 'latest':
            for key, value in self.json_response.items():
                print(f"{key}: {value}")
        elif self.selected_time_endpoint == 'history':
            for item in self.json_response['history']:
                for key, value in item.items():
                    print(f"{key}: {value}")
                print('\n\n')
        if not bool(self.json_response):
            print('There was no response!')

    def disable_estimation(self, url: str):
        if not self.estimation:
            result = url + '&disableEstimations=true'
        else:
            result = url
        return result

    def report_list_of_zones(self):
        response = requests.get(f'https://api.electricitymap.org/v3/{self.all_available_zones}')
        json_response = response.json()
        for zone_abr, zone_data in json_response.items():
            print(f'{zone_abr}: {zone_data["zoneName"]}')

        return json_response
