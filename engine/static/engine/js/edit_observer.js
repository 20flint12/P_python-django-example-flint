$(document).ready(function () {


    // to "remember" selected tab
    $("a[data-toggle='tab']").on("shown.bs.tab", function (e) {
        var hash = $(e.target).attr("href");
        if (hash.substr(0, 1) == "#") {
            location.replace("#!" + hash.substr(1));
        }
    });


    // to "restore" selected tab
    if (location.hash.substr(0, 2) == "#!") {
        $("a[href='#" + location.hash.substr(2) + "']").tab("show");
    }



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
