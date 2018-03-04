function initStatusButtons(){
    $('.btn-status').click(function(e){
        e.preventDefault();
        var post_status_id = $(this).data("post_status_id");

        var btns = $('#btns-status');
        var iteam_id= btns.data("iteam_id");
        var url = btns.data("url");
        console.log(url, iteam_id, post_status_id)

        statusUpdating(iteam_id, url, post_status_id);
    });
}


function statusUpdating(iteam_id, url, post_status_id){
    var data = {};
    var csrf_token = $('#btns-status [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;
    data.iteam_id = iteam_id;
    data.post_status_id = post_status_id;

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
    });
}


$(document).ready(function(){
    initStatusButtons();
    // changeIcons();
});





function changeIcons() {
  $('.change-icon').click(function(){
    var button = $(this);
    button.prop("disabled", "disabled");
    var icon = button.find('i').removeClass('fa-cart-plus').addClass('fa-check-circle');
  });
}
