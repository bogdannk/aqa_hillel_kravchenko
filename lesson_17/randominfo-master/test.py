import randominfo
from assertpy import assert_that

person = randominfo.Person()
print(person.full_name, person.gender, person.country, person.address)


class TestRandominfo:

    def test_full_name_is_not_empty(self):
        result = person.full_name
        assert_that(result).is_not_equal_to(None), "Error: full_name field is empty"

    def test_gender_is_not_empty(self):
        result = person.gender
        assert_that(result).is_not_equal_to(None), "Error: gender field is empty"

    def test_gender_is_valid(self):
        result = person.gender
        assert_that(result).is_in("male", "famale"), "Error: gender field contains an invalid value"

    def test_country_is_not_empty(self):
        result = person.country
        assert_that(result).is_not_equal_to(None), "Error: country field is empty"

    def test_address_is_not_empty(self):
        result = person.address
        assert_that(result).is_not_equal_to(None), "Error: address field is empty"

    def test_address_has_required_fields(self):
        address = person.address
        required_fields = ['street', 'landmark', 'area', 'city', 'state', 'pincode']
        for field in required_fields:
            assert_that(address).contains_key(field), f"Error: address is missing field '{field}'"
