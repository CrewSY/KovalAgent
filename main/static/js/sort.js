function initSortMenu(){
    $('#group-selector select').change(function(event){
    event.preventDefault();
    var sort_by = $(this).val();
    console.log(sort_by);

    updateContent(sort_by);
  });
}


function updateContent(sort_by) {
  var url = "/update_content/" + sort_by;
    $('#equipment_content').load(url);
}


$(document).ready(function(){
  initSortMenu();
});
