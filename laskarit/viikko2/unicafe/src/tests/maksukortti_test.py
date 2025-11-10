import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(300)
    
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.0)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(3000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    
    def test_palauttaa_true_jos_rahat_riittivät(self):
        result = self.maksukortti.ota_rahaa(250)
        
        self.assertEqual(result, True)

    def test_palauttaa_false_jos_rahat_eivät_riittäneet(self):
        result = self.maksukortti.ota_rahaa(2500)

        self.assertEqual(result, False)
    
    def test_str_palauttaa_oikean_tekstin(self):

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")