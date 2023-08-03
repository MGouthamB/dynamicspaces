window.addEventListener('message', function(event) {
  if (event.data && event.data.type === 'iframeHeight') {
    var iframe = document.getElementById('your-iframe-id');
    if (iframe) {
      iframe.style.height = event.data.height+'px';
      alert(event.data.height);
    }
  }
});