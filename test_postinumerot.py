import postinumerot


def test_yksi_postinumero():
    korvatunturi = postinumerot.suorita('korvatunturi')

    assert len(korvatunturi) == 1


def test_useampi_postinumero():
    porvoo = postinumerot.suorita('porvoo')

    assert len(porvoo) == 9


def test_smart_post_no_fix():
    smartpost = postinumerot.suorita('smartpost')
    smart_post = postinumerot.suorita('smart post')
    smartpsot = postinumerot.suorita('smartpsot')

    # total 812+4+3 = 819
    assert len(smartpost) == 812 and len(
        smart_post) == 4 and len(smartpsot) == 3


def test_smart_post_final():
    smartpost = postinumerot.suorita('smartpost')

    # 'SMARTPOST' == 812
    # 'SMART POST' == 4
    # 'SMARTPSOT' == 3
    assert len(smartpost) == 819
