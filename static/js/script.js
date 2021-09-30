$(document).ready(function () {
    $("#search-box").keyup(function () {
        var value = this.value.toLowerCase().trim();
            $("table tr").each(function (index) {
                if (!index) return;
                $(this).find("td").each(function () {
                    var id = $(this).text().toLowerCase().trim();
                    var not_found = (id.indexOf(value) == -1);
                    $(this).closest('tr').toggle(!not_found);
                    return not_found;
                });
            });
    });
    function addLightTheme() {
        $('#theme').removeClass('bi-moon-fill text-light').addClass('bi-sun-fill text-dark');
        $("#heading").removeClass('heading-dark-theme').addClass('heading');
        $('body').css('background-color', 'white');
        $('#table').removeClass('table-dark').addClass('table-light');
    }
    function addDarkTheme() {
        $('#theme').removeClass('bi-sun-fill text-dark').addClass('bi-moon-fill text-light');
        $("#heading").removeClass('heading').addClass('heading-dark-theme');
        $('body').css('background-color', '#212529');
        $('#table').removeClass('table-light').addClass('table-dark');
    }
    $("#mode").change(function () { 
        if($(this).prop("checked") == true){
            addDarkTheme();
        }else{
            addLightTheme();
        }
    });
});