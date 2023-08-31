from ..base import BasePlaywrightTestCase, expect

from model_bakery import baker


class TestCashflows(BasePlaywrightTestCase):
    def setUp(self):
        """
        Add any setUp functions here
        This will run beforeEach other method
        eg baker.make()
        """
        # self.page.goto(f"{self.live_server_url}/admin")
        pass

    def test_method(self):
        """
        Main test assertions in here
        eg expect()
        """
        # expect(self.page.get_by_text("Django")).to_contain_text("Django")
        pass
