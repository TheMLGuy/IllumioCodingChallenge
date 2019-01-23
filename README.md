# IllumioCodingChallenge
SDET Coding Assignment Back-end QA team

1.Code Structure
  There are two main classes: URLLibrary and UserInterface
  URLLibrary class is responsible for modules pertaining to 
    a. Validate an url
    b. Querying an url
    c. Check whether url has been seen before
    d. Return the response and status code for url that has been seen before
    e. Update retry count if invalid url is provided as input
  
  UserInterface class is responsible for modules pertaining to handling user input and session
  To execute the program, open command line, invoke python userinterface.py. This will start the session and user is prompted to enter a url.
  
  
2. Testing of solution:
  I identified the following testcases:
    a. When user provides an empty url
    b. When user provides a valid url but it does not generate a response
    c. When user provides a valid url and it generates a response
    d. When user  provides the same valid url that has been seen before
    e. When user provides an invalid url
    f. When user provides an invalid url for the third time
    g. When user gives the same invalid url 
    h. Combinations of inputs for url like ftp/http/https, url with or without port, ip or localhost or domain and so on
  A file called test.py is attached as part of the solution. This can be executed using pytest from command line in 
  the following manner:
  
  
  
3. Design choices:
  I employed a dictionary to keep track of the urls seen so far. I made sure that once the basic structure of the program was built, I chose to modularize every component to improve code resuability and conciseness.
  
4. Improvements:
I believe storing urls can be improved by using a trie data structure instead of a simple dictionary. The search of urls can be improved when a trie data structure is used. For example, if user queries https://www.google.com/users and https://www.google.com/mail. Instead of creating two separate entries in dictionary, this can be improved by using a trie.
An additional feature could be setting a limit on the number of urls that can be remembered along with response data fields. Using a limit can ensure that the 'top n' number of results are remembered.

5. I am greatful to you for receiving this challenge and am keenly looking forward to hearing from you.

  
  
