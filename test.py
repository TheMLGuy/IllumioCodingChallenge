import pytest
from URLLibrary import URLLibrary

class TestLibrary:

    def test_EmptyURL(self):
        obj=URLLibrary()
        print("checking empty url")
        assert obj.isURLValid("")==False

    def test_NormalURL(self, url):
        obj = URLLibrary()
        print("Checking normal url", url)
        assert obj.isURLValid(url)==True

    def test_ValidURLNoResponse(self, url):
        obj=URLLibrary()
        print("Checking valid url with no response", url)
        assert not obj.queryWebPage(url)



test=TestLibrary()
test.test_EmptyURL()
test.test_NormalURL("https://www.google.com")
test.test_NormalURL("https://www.google.com:80")
test.test_NormalURL("http://dummy.restapiexample.com/api/v1/employees")
test.test_ValidURLNoResponse("www.goog.com")
test.test_NormalURL("https://www.google*.com")