function setIframeHeight(height) {
    var iframe = document.getElementById("your-iframe");
    iframe.style.height = height + "px";
}

// Function to handle messages received from the iframe
function handleMessage(event) {
    var data = event.data;
    if (data.type === "iframeHeight") {
        setIframeHeight(data.height);
    }
}

// Listen for messages from the iframe
window.addEventListener("load", function () {
    window.addEventListener("message", handleMessage);
});