# Cross-site-scripting-page-injection
I wanted to test the security of the stuyvesant homework servers

### Vulnerabilities: 
* cross-site scripting
  * Solution: escaping and custom markup langauge for links
* cgi error throwing (invalid student name)
  * Solution: log errors into a file instead of showing them on the page

##### Simulation:
If you want to see how the attack would look, go [here](http://grabber-com.stackstaging.com/Grabber/test.html) and see the results [here](http://grabber-com.stackstaging.com/Grabber/passwords.txt), or copy-paste the code from script\_to\_inject into a homework comment and then view it to see the exploit in action.

Note: My free webhosting has expired
