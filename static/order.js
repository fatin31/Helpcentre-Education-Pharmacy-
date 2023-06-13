// Get the CSRF token from the cookie
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
    }
});

var csrftoken = getCookie('YOUR_CSRF_COOKIE_NAME');
var xhr = new XMLHttpRequest();
xhr.open('POST', '/my-server/create-paypal-order/', true);
xhr.setRequestHeader('X-CSRFToken', csrftoken);
xhr.onreadystatechange = function () {
  if (xhr.readyState === 4 && xhr.status === 200) {
    // Handle success response
  } else {
    // Handle error response
  }
};
xhr.send();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split("; ");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].split("=");
            if (cookie[0] === name) {
                cookieValue = cookie[1];
                break;
            }
        }
    }
    return cookieValue;
}

// Include the CSRF token in the AJAX request headers
var csrftoken = getCookie("csrftoken");
$.ajax({
    url: "/my-server/create-paypal-order/",
    type: "POST",
    headers: { "X-CSRFToken": csrftoken },
    data: { /* Your POST data */ },
    success: function(response) {
        // Handle success response
    },
    error: function(xhr, textStatus, error) {
        // Handle error
    }
});
