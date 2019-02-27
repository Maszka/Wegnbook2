from datetime import datetime, timedelta

from django.test import TestCase
from mock import MagicMock

from app.models import Wegan


class WeganTestCase(TestCase):
    WEGAN_DATA = {"name": "From",
                  "not_eating_from": datetime.now(),
                  "weight": 74,
                  "height": 2.,
                  "sex": "M"}

    def setUp(self):
        self.wegan = Wegan.objects.create(**self.WEGAN_DATA)

    def test_physique_should_return_Underweight_for_bmi_lt_18_5(self):
        self.wegan.body_mass_index = MagicMock()
        self.wegan.body_mass_index.return_value = 11
        self.assertEqual(self.wegan.physique(), "Underweight")
        self.wegan.body_mass_index.return_value = 18.5
        self.assertNotEqual(self.wegan.physique(), "Underweight")

    def test_physique_should_return_Normal_for_bmi_ge_18_5_and_le_25(self):
        self.wegan.body_mass_index = MagicMock()
        self.wegan.body_mass_index.return_value = 18.5
        self.assertEqual(self.wegan.physique(), "Normal")
        self.wegan.body_mass_index.return_value = 25
        self.assertEqual(self.wegan.physique(), "Normal")

    def test_physique_should_return_Overweight_for_bmi_gt_25(self):
        self.wegan.body_mass_index = MagicMock()
        self.wegan.body_mass_index.return_value = 25.01
        self.assertEqual(self.wegan.physique(), "Overweight")

    def test_bmi_is_counted_correctly(self):
        self.assertAlmostEqual(self.wegan.body_mass_index(), 18.5, places=5)

    def test_should_return_Noob_for_one_who_has_not_eaten_meat_for_100_days_or_less(self):
        self.wegan.not_eating_from = datetime.now()
        self.assertEqual(self.wegan.status(), "Noob")
        self.wegan.not_eating_from = datetime.now() + timedelta(days=99, hours=23)
        self.assertEqual(self.wegan.status(), "Noob")

    def test_should_return_Herbivore_for_one_who_has_not_eaten_meat_for_200_days_or_less(self):
        self.wegan.not_eating_from = datetime.now() + timedelta(days=100)
        self.assertEqual(self.wegan.status(), "Herbivore")
        self.wegan.not_eating_from = datetime.now() + timedelta(days=199, hours=23)
        self.assertEqual(self.wegan.status(), "Herbivore")

    def test_should_return_TheOne_for_one_who_has_not_eaten_meat_for_2_years_and_more(self):
        self.wegan.not_eating_from = datetime.now() + timedelta(days=199, hours=23)
        self.assertEqual(self.wegan.status(), "Herbivore")

