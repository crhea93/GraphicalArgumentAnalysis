$('#btn_ZoomIn').click(
    function () {
        if (currentZoom < 1.5) {
            $('#CAM_items').animate({'zoom': currentZoom += .1});
            $('#zoom_lev').html('Zoom: '+currentZoom.toFixed(1));
            $('#CAM_items').css('width',cam_width_max)
            //$('#CAM_items').animate({width: currentZoom*this.width});
        }
    });
$('#btn_ZoomOut').click(
    function () {
        if (currentZoom > 0.6) {
            $('#CAM_items').animate({'zoom': currentZoom -= .1});
            $('#CAM_items').css('width',cam_width_max);
            //$('#CAM_items').css('width', $('#primary_card').width()+scroll_left);
            //$('#CAM_items').css('height', $('#primary_card').height());
            $('#zoom_lev').html('Zoom: '+currentZoom.toFixed(1));
            //drag_width = drag_width/currentZoom
        }
    });
$('#btn_ZoomReset').click(
    function () {
        currentZoom = 1.0;
        $('#CAM_items').animate({ 'zoom': 1 }, 'slow');
        $('#zoom_lev').html('Zoom: '+currentZoom.toFixed(1));
    });
