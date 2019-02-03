(function($) {
    $(function() {
        $('#id_type').on('change', () => {
            if ($('#id_type').val() === 'student')
                $('.field-professor').show();
            else
                $('.field-professor').hide();
        });

    });
})(django.jQuery);