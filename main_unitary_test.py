from unittest import TestCase

from control_formset_validation import check_formset_validation


class TestControl(TestCase):

    def test_happy_path(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 2, 'sap_renault': 1, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': '20-10-2021'},
            1: {'resp_control': 1, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '10-10-2021'}
        }
        self.assertEqual(6, check_formset_validation(forms))

    def test_duplicate_resp_control(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 2, 'sap_renault': 1, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': '20-10-2021'},
            1: {'resp_control': 2, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '10-10-2021'}
        }
        self.assertEqual(1, check_formset_validation(forms))

    def test_resp_out_control(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 5, 'sap_renault': 1, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': '20-10-2021'},
            1: {'resp_control': 1, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '10-10-2021'}
        }
        self.assertEqual(2, check_formset_validation(forms))

    def test_duplicate_date_control(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 2, 'sap_renault': 1, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': '20-10-2021'},
            1: {'resp_control': 1, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '20-10-2021'}
        }
        self.assertEqual(3, check_formset_validation(forms))

    def test_duplicate_sapeur_in_control(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 2, 'sap_renault': 3, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': '20-10-2021'},
            1: {'resp_control': 1, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '10-10-2021'}
        }
        self.assertEqual(4, check_formset_validation(forms))

    def test_wrong_input_date(self):
        forms = {
            0: {'resp_control': 2, 'sap_tonne': 2, 'sap_renault': 5, 'sap_mercedes': 3,
                'sap_mitsubishi': 4, 'date': 'banane'},
            1: {'resp_control': 1, 'sap_tonne': 1, 'sap_renault': 4, 'sap_mercedes': 3,
                'sap_mitsubishi': 2, 'date': '10-10-2021'}
        }
        self.assertEqual(5, check_formset_validation(forms))
