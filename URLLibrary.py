import re
import requests


class URLLibrary:
    def __init__(self):
        self.queryDictionary = {}
        self.retryCount = 0

    def queryWebPage(self, url):
        """

        :param url: Use requests module to query url
        :return: response object with status code and body of the url
        """
        try:
            print("Querying for URL : ", url)

            response = requests.get(url)

            self.queryDictionary[url] = {
                "status_code": response.status_code,
                "body": response.content
            }

        except Exception as e:
            print("Error when trying to access website", str(e))

            self.queryDictionary[url] = None

        queryResponse = self.queryDictionary[url]

        return queryResponse

    def isURLValid(self, url):
        """

        :param url: check whether url is valid
        :return: boolean to indicate whether the url is valid
        """
        isValid = False

        try:
            validURLRegex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)

            if url != None and validURLRegex.search(url):
                isValid = True

        except Exception as e:
            #print the exception msg
            pass

        return isValid

    def isURLSeen(self, url):
        """

        :param url: Has the url been so far
        :return: boolean indicating whether the url has been seen before
        """
        return url in self.queryDictionary

    def getURLSavedResponse(self, url):
        """

        :param url: Retrieve response stored for the corresponding url
        :return: return the response
        """
        return self.queryDictionary[url]

    def updateRetryCount(self):
        """

        :return: boolean whether limit has been reached
        """
        self.retryCount += 1
        return self.retryCount != 3

