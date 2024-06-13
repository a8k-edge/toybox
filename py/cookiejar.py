import requests
import http.cookiejar

# Create a CookieJar
cj = http.cookiejar.LWPCookieJar()

# Create a session with the CookieJar
s = requests.Session()
s.cookies = cj

# Send a request with cookies
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# Save the cookies to disk
cj.save(filename='cookiejar', ignore_discard=True)