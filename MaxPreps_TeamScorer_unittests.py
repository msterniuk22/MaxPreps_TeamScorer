import MaxPreps_TeamScorer_v1 as teamscorer


def test_HTML_response_headnode():
    assert teamscorer.raw_data.status_code == 200
    return 'PASSED HTML response for headnode PASSED'


def test_get_team_record_func():
    assert type(teamscorer.get_team_record(teamscorer.html_tree)) == str
    return "PASSED get_team_record func PASSED"


def test_get_team_winrate_func():
    assert type(teamscorer.get_team_winrate(teamscorer.html_tree)) == str
    return "PASSED get_team_winrate func PASSED"


def test_get_team_name_func():
    assert type(teamscorer.get_team_name(teamscorer.html_tree)) == str
    return "PASSED get_team_name func PASSED"


def test_get_opp_links_func():
    assert type(teamscorer.get_opponent_schedule_links(teamscorer.html_tree)) == list
    return "PASSED get_opp_links func PASSED "


def test_get_avg_opp_winrate_func():
    assert type(teamscorer.get_avg_opp_winrate()) == int or float
    return "PASSED get_avg_opp_winrate func PASSED"


def test_get_avg_opp_games_played_func():
    assert type(teamscorer.get_avg_opp_games_played()) == int or float
    return "PASSED get_avg_opp_games_played func PASSED"


def teamscorer_unit_test():
    print(test_HTML_response_headnode())
    print(test_get_team_record_func())
    print(test_get_team_winrate_func())
    print(test_get_team_name_func())
    print(test_get_opp_links_func())
    print(test_get_avg_opp_games_played_func())
    print(test_get_avg_opp_winrate_func())

    return "ALL TESTS PASSED"

print(teamscorer_unit_test())