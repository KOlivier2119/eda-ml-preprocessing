from django.test import TestCase, Client
from .dashboard import pivot_table
import pandas as pd


class DashboardTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_pivot_table_function(self):
        # construct a small dataframe and ensure generated HTML includes expected headers
        df = pd.DataFrame({
            "manufacturer": ["A", "A", "B"],
            "body_type": ["sedan", "suv", "sedan"],
            "selling_price": [10, 20, 30],
        })
        html = pivot_table(df)
        # pivot table output should contain manufacturer, body_type and selling_price
        self.assertIn("manufacturer", html.lower())
        self.assertIn("body_type", html.lower())
        self.assertIn("selling_price", html.lower())

    def test_dashboard_view_has_pivot(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("pivot_table", response.context)
