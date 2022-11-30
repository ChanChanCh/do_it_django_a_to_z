from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_post_list(self):
        self.assertEqual(2, 2)
        # 2와3이 같은지 알아보는 테스트
