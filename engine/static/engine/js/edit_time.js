$(document).ready(function () {

    $(function () {
        $('#datetimepicker14').datetimepicker({
            inline: true,
            sideBySide: true,
            // locale: 'ru',
            // format: 'DD.MM.YYYY 11:44:22'
            format: 'YYYY-MM-DD',
            icons: {
                    time: "fa fa-clock-o",
                    date: "fa fa-calendar",
                    up: "fa fa-arrow-up",
                    down: "fa fa-arrow-down"
                },
            // viewMode: 'years'
        });

        $('#datetimepicker15').datetimepicker({
            inline: true,
            sideBySide: true,
            // locale: 'ru',
            // format: 'DD.MM.YYYY 11:44:22'
            format: 'YYYY-MM-DD 11:44:22',
            icons: {
                    time: "fa fa-clock-o",
                    date: "fa fa-calendar",
                    up: "fa fa-arrow-up",
                    down: "fa fa-arrow-down"
                }
        });
    });

});
