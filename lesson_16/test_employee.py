from lesson_16.d_temlead import TeamLead
from lesson_16.data_for_test import expected_mark_attrs, expected_failed_mark_attrs
from assertpy import assert_that
import pytest

class TestEmployee:

    def setup_method(self):
        self.aqa_team_lead = TeamLead('Bogdan', 4000, "Test_department", 10)

    def test_employee_attrs(self):
        actual_attrs = {
            "name": self.aqa_team_lead.name,
            "salary": self.aqa_team_lead.salary,
            "department": self.aqa_team_lead.department,
            "team_size": self.aqa_team_lead.team_size
        }

        print(f"\n{actual_attrs}")
        (assert_that(actual_attrs,
                     "The desired user attributes do not match the test dictionary attributes")
         .is_equal_to(expected_mark_attrs))

        (assert_that(actual_attrs,
                     "The desired user attributes do not match the test dictionary attributes")
         .is_equal_to(expected_failed_mark_attrs))


    def test_employee_invalid_attrs(self):
        invalid_attrs = {
            "name": 123,
            "salary": "four thousand",
            "department": None,
            "team_size": -5
        }

        with pytest.raises(AssertionError):
            assert_that({
                "name": self.aqa_team_lead.name,
                "salary": self.aqa_team_lead.salary,
                "department": self.aqa_team_lead.department,
                "team_size": self.aqa_team_lead.team_size
            }).is_equal_to(invalid_attrs)


    def test_employee_negative_attrs_value(self):
        actual_attrs = {
            "name": self.aqa_team_lead.name,
            "salary": self.aqa_team_lead.salary,
            "department": self.aqa_team_lead.department,
            "team_size": self.aqa_team_lead.team_size
        }

        (assert_that(actual_attrs,
                     "The actual employee attributes do not match the expected attributes in the test")
         .is_equal_to(expected_failed_mark_attrs))
