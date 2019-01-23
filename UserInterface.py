from URLLibrary import URLLibrary
class UserInterface:

    def __init__(self):
        self.urlLibObject = URLLibrary()


    def runSession(self):
        """

        :return: None
        """

        while True:

            print("\n##########################################################\n")

            url = input("Enter url to be queried: ", ).strip()
            response = None

            if self.urlLibObject.isURLSeen(url):
                print("This URL has been queried before ")
                response = self.urlLibObject.getURLSavedResponse(url)

            else:
                isURLValid = self.urlLibObject.isURLValid(url)
                if isURLValid:
                    print("URL is valid")
                    response = self.urlLibObject.queryWebPage(url)

                if not isURLValid:
                    print("Invalid URL entered")
                    if not self.urlLibObject.updateRetryCount():
                        print("Session Terminated")
                        break
                    continue
                if not response:
                    print("Unable to get response")
                    continue
                print("Response's status code ", response["status_code"])
            #Response object now has the required URL Data.
            #We can perform the required operations.


if __name__=="__main__":
    userinterface=UserInterface()
    userinterface.runSession()