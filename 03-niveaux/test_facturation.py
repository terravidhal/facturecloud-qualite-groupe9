from facturation import total_ht, calculer_remise, calculer_tva, creer_facture


def test_total_ht_deux_lignes():
    assert total_ht([(2, 5000), (1, 3000)]) == 13000


def test_total_ht_liste_vide():
    assert total_ht([]) == 0


def test_remise_client_fidele():
    assert calculer_remise(13000, True) == 1300


def test_remise_client_non_fidele():
    assert calculer_remise(13000, False) == 0


def test_tva_200():
    assert calculer_tva(200) == 39


def test_tva_11700():
    assert calculer_tva(11700) == 2252


def test_facture_client_fidele():
    facture = creer_facture([(2, 5000), (1, 3000)], True)
    assert facture["ht"] == 13000
    assert facture["remise"] == 1300
    assert facture["net"] == 11700
    assert facture["tva"] == 2252
    assert facture["ttc"] == 13952


def test_facture_client_non_fidele():
    facture = creer_facture([(2, 5000), (1, 3000)], False)
    assert facture["ht"] == 13000
    assert facture["remise"] == 0
    assert facture["net"] == 13000
    assert facture["tva"] == 2503
    assert facture["ttc"] == 15503
