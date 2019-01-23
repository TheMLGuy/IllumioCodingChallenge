# IllumioCodingChallenge
SDET Coding Assignment Back-end QA team

1. Code Structure
  There are two main classes: URLLibrary and UserInterface. 
  URLLibrary class is responsible for modules pertaining to 
     Validate an url, 
     Querying an url, 
     Check whether url has been seen before, 
     Return the response and status code for url that has been seen before, 
     Update retry count if invalid url is provided as input.
  
    UserInterface class is responsible for modules pertaining to handling user input and session. 
    To execute the program, open command line, invoke python UserInterface.py or python -m UserInterface. This will start the session and user is prompted to enter a url.
  
  
 2. Testing of solution: are
  I identified the following testcases:
     When user provi, es an empty url; 
     When user provides a valid url but it does not generate a response; 
     When user provides a valid url and it generates a response;
     When user  provides the same valid url that has been seen before; 
     When user provides an invalid url;
     When user provides an invalid url for the third time; 
     When user gives the same invalid url;
     Combinations of inputs for url like ftp/http/https, url with or without port, ip or localhost or domain and so on.
  A file called test.py is attached as part of the solution. This can be executed from command line in 
  the following manner:
      python test.py
  
  
 3. Design choices:
  I employed a dictionary to keep track of the urls seen so far. I made sure that once the basic structure of the program was built, I chose to modularize every component to improve code resuability and conciseness.
  
 4. Improvements:
I believe storing urls can be improved by using a trie data structure instead of a simple dictionary. The search of urls can be improved when a trie data structure is used. For example, if user queries are https://www.google.com/users and https://www.google.com/mail,  instead of creating two separate entries in dictionary, this can be improved by using a trie.
An additional feature could be setting a limit on the number of urls that can be remembered along with response data fields. Using a limit can ensure that the 'top n' number of results are remembered. The stale entries can be removed from the dictionary when limit is reached.
I would have wanted to use pytest and execute a series of tests.
 5. I am greatful to you for receiving this challenge and am keenly looking forward to hearing from you.

  
  
