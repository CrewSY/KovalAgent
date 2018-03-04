function initStatusButtons(){
    $('.btn-status').click(function(e){
        e.preventDefault();
        var post_status_id = $(this).data("post_status_id");

        var btns = $('#btns-status');
        var iteam_id= btns.data("iteam_id");
        var url = btns.data("url");

        statusUpdating(iteam_id, url, post_status_id);
    });
}


function statusUpdating(iteam_id, url, post_status_id){
    var data = {};
    var csrf_token = $('#btns-status [name="csrfmiddlewaretoken"]').val();

    data["csrfmiddlewaretoken"] = csrf_token;
    data.iteam_id = iteam_id;
    data.post_status_id = post_status_id;

    var indicator = $('#ajax-progress-indicator');

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        'beforeSend': function(xhr, settings){
            indicator.show();
        },
        'success': function(data, status, xhr){
            indicator.hide();
            location.reload();
        }
    });
}


function changeIcons() {
  $('.change-icon').click(function(){
    var button = $(this);
    button.prop("disabled", "disabled");
  });
}

function initDisabledButton(){
    var id = $('#iteam-status').data("status_id");
    var btn1 = $('#btn1');
    var btnid1 = btn1.data("post_status_id");
    if(btnid1==id){
        btn1.prop("disabled", "disabled");
    }
    var btn2 = $('#btn2');
    var btnid2 = btn2.data("post_status_id");
    if(btnid2==id){
        btn2.prop("disabled", "disabled");
    }
    var btn3 = $('#btn3');
    var btnid3 = btn3.data("post_status_id");
    if(btnid3==id){
        btn3.prop("disabled", "disabled");
    }
    var btn4 = $('#btn4');
    var btnid4 = btn4.data("post_status_id");
    if(btnid4==id){
        btn4.prop("disabled", "disabled");
    }
}


$(document).ready(function(){
    initStatusButtons();
    changeIcons();
    initDisabledButton();
});
