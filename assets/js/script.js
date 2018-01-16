
$(document).ready(function(){
    if ($(this).width() >= 575) {
      $("#collapseMenu").collapse('show')
    }
    $(".navigation_link").hover(function(){
        $(this).toggleClass('hovered_link');
        $(this).parent().find('div').toggleClass("active_link");
    });
    $(".active").parent().find('div').addClass("activated_link");
    $("span:contains('Browse')").replaceWith('<span class="d-none d-sm-inline-block">Выбрать...</span>');
    $("i.glyphicon").replaceWith('<i class="far fa-folder-open"></i>');

    $(window).resize(function() {
      if ($(this).width() >= 575) {
        $("#collapseMenu").collapse('show')
      }
      else if ($(this).width() < 575) {
        $("#collapseMenu").collapse('hide')
      }
    });
});
