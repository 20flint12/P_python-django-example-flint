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

        $('#dtp_unaware_local').datetimepicker({
            // inline: true,
            sideBySide: true,
            locale: 'ru',
            // format: 'DD.MM.YYYY 11:44:22'
            // format: 'YYYY-MM-DD 11:44:22',
            format: 'YYYY-MM-DD HH:mm:ss',
            // format: 'HH:ii',
            icons: {
                    time: "fa fa-clock-o",
                    date: "fa fa-calendar",
                    up: "fa fa-arrow-up",
                    down: "fa fa-arrow-down"
                },

            defaultDate: "11/1/2013",
            // useCurrent: true,

            // disabledDates: [
            //     moment("12/25/2013"),
            //     new Date(2013, 11 - 1, 21),
            //     "11/22/2013 00:53"
            // ],

            // autoclose: true,

            // pickTime: false,

        });
    });

});
