import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassan_rahamaara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lounaiden_maara_alussa(self): 
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #kateiselle
    def test_edullinen_lounas_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(vaihtoraha, 760)

    def test_maukas_lounas_kateisella_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(vaihtoraha, 600)

    def test_edullinen_lounas_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 240)

    def test_maukas_lounas_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 400)

    def test_edullinen_lounas_kateisella_myydyt_lounaat_lkm(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kateisella_myydyt_lounaat_lkm(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_edullinen_lounas_kateisella_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_lounas_kateisella_maksu_ei_riita(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #kortilla
    def test_edullinen_lounas_kortilla_veloitetaan_oikein(self):
        result = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertTrue(result)
        self.assertEqual(self.maksukortti.saldo, 1000 - 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_kortilla_veloitetaan_oikein(self):
        result = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertTrue(result)
        self.assertEqual(self.maksukortti.saldo, 1000 - 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_lounas_kortilla_myydyt_lounaat_lkm(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kortilla_myydyt_lounaat_lkm(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_kortilla_maksu_ei_riita(self):
        maksukortti = Maksukortti(200)
        result = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertFalse(result)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_kortilla_maksu_ei_riita(self):
        maksukortti = Maksukortti(200)
        result = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertFalse(result)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_lataus_muuttaa_saldoa_ja_kassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 600)
        self.assertEqual(self.maksukortti.saldo, 1000 + 600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 600)

    def test_kortille_lataus_negatiivinen_summa_ei_muuta_saldoa_tai_kassaa(self):
        saldo_alussa = self.maksukortti.saldo
        kassa_alussa = self.kassapaate.kassassa_rahaa
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, saldo_alussa)
        self.assertEqual(self.kassapaate.kassassa_rahaa, kassa_alussa)

    def test_kassassa_rahaa_euroina_palautus(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)