import Testing_Codep

api_url = "https://restcountries.com/v3.1/all"

def test_getresponse():
    ret  = Testing_Codep.get_response(api_url)
    assert ret.status_code== 200

def test_sum():
    assert 3==3