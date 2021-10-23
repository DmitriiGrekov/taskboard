$('#add_task_button').click(function(){
    $('#content').children().css('display', 'none')
    $('.task_add_form').slideToggle('slow')
})


$('#register_button').click(function(){
    $('#content').children().css('display', 'none')
    $('.register_form').slideToggle()
    return false
})



$("#login_button").click(function(){
    $('#content').children().css('display', 'none')
    $('.login_form').slideToggle()
    return false
})





$(document).ready(function(){
    $( document ).delegate( ".task_card", "click", show_full_task);
})


function show_full_task(){
    console.log($(this).attr('task_id'))
    return false
}