import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)


    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")


    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo_euroina(), 7.5)


    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
        self.kortti.syo_maukkaasti()

        self.assertEqual(self.kortti.saldo_euroina(), 6.0)


    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)
    

    def test_kortille_voi_ladata_rahaa(self):
        self.kortti.lataa_rahaa(2500)

        self.assertEqual(self.kortti.saldo_euroina(), 35.0)


    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
        self.kortti.lataa_rahaa(20000)

        self.assertEqual(self.kortti.saldo_euroina(), 150.0)


    def test_maukkaan_lounaan_syominen_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 2.0)


    def test_negatiivisen_summan_lataaminen_ei_muuta_kortin_saldoa(self):
        self.kortti.lataa_rahaa(-200)

        self.assertEqual(self.kortti.saldo_euroina(), 10.0)


    def test_kortilla_pystyy_ostamaan_edulliseen_lounaan_kun_kortilla_rahaa_vain_edullisen_lounaan_verran(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)


    def test_kortilla_pystyy_ostamaan_maukkaan_lounaan_kun_kortilla_rahaa_vain_maukkaan_lounaan_verran(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(kortti.saldo_euroina(), 0.0)
    

    def test_tarkista_alussa_onko_kortin_saldo_oikein(self):
        self.assertEqual(self.kortti.saldo, 1000)


    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(300)

        self.assertEqual(self.kortti.saldo, 1300)


    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.kortti.syo_edullisesti()

        self.assertEqual(self.kortti.saldo, 750)


    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        kortti = Maksukortti(100)
        tulos = kortti.syo_edullisesti()

        self.assertEqual(kortti.saldo, 100)
        self.assertFalse(tulos)


    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        kortti = Maksukortti(150)
        tulos = kortti.syo_maukkaasti()

        self.assertFalse(tulos)
        self.assertEqual(kortti.saldo, 150)


    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        kortti = Maksukortti(500)
        tulos = kortti.syo_maukkaasti()

        self.assertTrue(tulos)
        self.assertEqual(kortti.saldo, 100)