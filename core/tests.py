from django.test import TestCase
from django.test.client import RequestFactory

from core.models import Commission
from core.views import index, reservation, commissions


class TestView(TestCase):

    def test_index_view_success(self):
        with open('Reservations.csv', 'rb') as f:
            resp = self.client.post('/', {'myfile': f})
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Commission.objects.exists())

    def test_reservation_view_contains_commissions(self):
        self.test_index_view_success()
        resp = self.client.get('/reservations/?month=2021-05')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['commissions'].exists())
        self.assertContains(resp, resp.context['commissions'][0].reservation)
        self.assertContains(resp, resp.context['commissions'][0].city)
        self.assertContains(resp, resp.context['commissions'][0].flat)
        self.assertContains(resp, resp.context['commissions'][0].net_incoming)

    def test_reservation_view_contains_not_contains_commissions(self):
        self.test_index_view_success()
        resp = self.client.get('/reservations/?month=2021-0523434343443434')
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['commissions'].exists())

    def test_commissions_view_city(self):
        self.test_index_view_success()
        resp = self.client.get('/commissions/?city=PORTO')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['commissions'].exists())
        self.assertContains(resp, resp.context['commissions'][0].reservation)
        self.assertContains(resp, resp.context['commissions'][0].city)
        self.assertContains(resp, resp.context['commissions'][0].flat)
        self.assertContains(resp, resp.context['commissions'][0].net_incoming)

    def test_commissions_view_no_city(self):
        self.test_index_view_success()
        resp = self.client.get('/commissions/?city=city_not_exists')
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(resp.context['commissions'].exists())


