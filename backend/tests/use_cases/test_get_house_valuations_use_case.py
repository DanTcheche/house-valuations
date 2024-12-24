import json

import pytest
from unittest.mock import patch
from app.adapters.property_adapters.base_property_adapter import BasePropertyAdapter
from app.schemas.properties.property_schema import PropertySchema
from app.use_cases.get_house_valuations_use_case import (
    GetHouseValuationUseCase,
)


class TestGetHouseValuationsUseCase:
    @pytest.fixture
    def mock_provider_1_data(self):
        with open("tests/mocks/provider_1_response.json", "r") as f:
            return json.load(f)

    @pytest.fixture
    def mock_provider_2_data(self):
        with open("tests/mocks/provider_2_response.json", "r") as f:
            return json.load(f)

    @patch.object(BasePropertyAdapter, '_get_data_from_provider')
    def test_get_house_valuation(
        self,
        mock_get_data_from_provider,
        mock_provider_1_data,
        mock_provider_2_data,
    ):
        def mock_side_effect(address, provider_name):
            if provider_name == 'Provider 1':
                return  mock_provider_1_data
            elif provider_name == 'Provider 2':
                return mock_provider_2_data
            return {}

        mock_get_data_from_provider.side_effect = mock_side_effect
        result = GetHouseValuationUseCase().execute("1180 6th Avenue, New York, NY 10036")

        assert len(result) == 2
        assert isinstance(result[0], PropertySchema)
        assert isinstance(result[1], PropertySchema)
        assert result[0] == PropertySchema(
            id="1180-6Th-Avenue-New-York-NY-10036",
            provider="Provider 1",
            address="1180 6Th Avenue New York NY 10036",
            square_footage=3968,
            lot_size_acres=0.14,
            year_built=1946,
            property_type="Single Family",
            bedrooms=1,
            bathrooms=2,
            room_count=9,
            septic_system=False,
            sale_price=204716,
        )
        
        assert result[1] == PropertySchema(
            id="1180-6Th-Avenue-New-York-NY-10036",
            provider="Provider 2",
            address="1180 6Th Avenue New York NY 10036",
            square_footage=3968,
            lot_size_acres=0.14,
            year_built=1946,
            property_type="Single Family",
            bedrooms=1,
            bathrooms=2,
            room_count=9,
            septic_system=False,
            sale_price=204716,
        )
