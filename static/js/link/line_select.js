
var DELAY_link = 200, clicks_link = 0, timer_link = null;
var ctrl_clicks_link = 0; //Number of control clicks



$(document).on("click", '.link',function(e){
    var target_el = $(this); //get link
    click_element = 'link';
    $('.block.Open').each(function(){
                    close_block_func(this);
                  });
    if (event.ctrlKey || event.metaKey) { //Control click
        if (target_el.hasClass('Selected-link')) {
            //$('#UpdateLinkModal').modal('show');
            ctrl_clicks_link -= 1;
        } else {
            target_el.addClass('Selected-link');

            //if (ctrl_clicks_link === 1){
        }// End adding class
        //Check if two elements are selected

    }//end control click
    else { //if normal click
        clicks_link++;  //count clicks
        if (clicks_link === 1) { //Single Click
            timer_link = setTimeout(function () {
                console.log('single click link');

                if (target_el.hasClass('Selected-link')) {
                    if (target_el.hasClass('Warrant')) {
                        target_el.removeClass('Warrant');
                    } else {
                        target_el.addClass('Warrant');
                    }
                    target_el.removeClass('Selected-link');
                    ctrl_clicks_link -= 1;
                } else {
                    target_el.addClass('Selected-link');
                    if (target_el.hasClass('Warrant')) {
                        target_el.removeClass('Warrant');
                    } else {
                        target_el.addClass('Warrant');
                    }
                }
                update_link_form();
                clicks_link = 0;             //after action performed, reset counter
            }, DELAY_link);// End Single Click
        } else { //Double Click
            clearTimeout(timer_link);    //prevent single-click action
            target_el.addClass('Selected-link');
            clicks_link = 0;             //after action performed, reset counter
        }//End Double Click
    }//End normal click

})
.on("dblclick", '.block',function(e){
    e.preventDefault();  //cancel system double-click event
});




