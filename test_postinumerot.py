import postinumerot


def test_yksi_postinumero():
    korvatunturi = postinumerot.suorita('korvatunturi')

    assert len(korvatunturi) == 1


def test_useampi_postinumero():
    porvoo = postinumerot.suorita('porvoo')

    assert len(porvoo) == 9


def test_smart_post_final():
    smartpost = postinumerot.suorita('smartpost')

    # 'SMARTPOST' == 812
    # 'SMART POST' == 4
    # 'SMARTPSOT' == 3
    assert len(smartpost) == 819
