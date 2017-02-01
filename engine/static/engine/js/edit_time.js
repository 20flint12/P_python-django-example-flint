$(document).ready(function () {

    $(function () {
        $('#datetimepicker12').datetimepicker({
            inline: true,
            sideBySide: true,
            // locale: 'ru',
            // format: 'DD.MM.YYYY 11:44:22'
            format: 'YYYY-MM-DD'
        });

        $('#datetimepicker13').datetimepicker({
            inline: true,
            sideBySide: true,
            // locale: 'ru',
            // format: 'DD.MM.YYYY 11:44:22'
            format: 'YYYY-MM-DD 11:44:22'
        });
    });

});
