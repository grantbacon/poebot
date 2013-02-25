$(document).ready(function() {

    (function ($){
        $.fn.serializeJSON=function(){
            var json = {};
            jQuery.map($(this).serializeArray(), function(n, i) {
                if (n['value'] !== '') {
                    json[n['name']] = n['value']
                }
            });
            return JSON.stringify(json);
        };
    })(jQuery);


    $('#form').submit(function(){
        $.ajax({
            url: '/speak',
            type: 'POST',
            data: $('#form').serializeJSON(),
            dataType: 'text'
        }).success(function(data) {
            $('#success_message').html('<span style="color: ' + data + '">' + 'message sent!' + '</span>');
            $('#success_message').fadeIn(1000).delay(3000).fadeOut(2000);
        });
        return false;
    });
});
