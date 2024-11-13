var isdataread=false;
window.addEventListener('message', function(event) {
  if (event.data.height) {
    var iframe = document.getElementById('DSiframe');
    if (iframe) {
      iframe.style.height = event.data.height+'px';
      isdataread=true;

    }
  }
});
