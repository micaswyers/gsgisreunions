function makeNewImgTags(urls_list) {
    for (var i =0; i < urls_list.length; i++) {
        $(".main_container").append("<img src='" + urls_list[i] + "'>")
    }
}
$(".button_container").append('<button type="button" id="more">More</button>');


$("#more").click (function(e) {
    e.preventDefault();
    console.log("User clicked");

    $.ajax({
        url: "/next",
    }).done(function(response) {
        var returned_dict = $.parseJSON(response);
        var new_urls_list = returned_dict['urls'];
        var is_next = returned_dict['is_next'];
        console.log("Data is back");
        makeNewImgTags(new_urls_list);
        if ( is_next == false) {
            $("#more").hide();
        };

    })
});
