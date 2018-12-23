  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}//source of above: https://gist.github.com/hugollm/f51953cf66e4e7d0701fc187b0c3eeb6


   $(document).ready(function() {



       $("#confirm_guest").submit(function(event){
       event.preventDefault();
           var form = $('#confirm_guest');
           var formData = $(form).serialize();

            $.ajax({
                 type:"POST",
                 url:"post",
            data:
            formData,


                 success: function(){
                     $('#thanks').html("<h2>Dziękujemy za potwierdzenie i do zobaczenia! :)</h2>");
                     $('#confirm_guest').hide()
                     $('')
                    }

            });

       });
            return false;
    });
