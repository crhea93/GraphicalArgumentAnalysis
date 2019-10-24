function createLine(line_num,name,point_array,drag_height,drag_width,start_block_id,end_block_id){
    console.log(start_block_id)
  x1 = point_array[0]; x2 = point_array[2];
  x1 = parseFloat(x1); x2 = parseFloat(x2);
  y1 = point_array[1]; y2 = point_array[3];
  y1 = parseFloat(y1); y2 = parseFloat(y2);
  var width = drag_width;
  var height=  drag_height;
  if (x2 < x1) {
        var temp = x1;
        x1 = x2;
        x2 = temp;
        temp = y1;
        y1 = y2;
        y2 = temp;
    }
  //double line width
  //line_width *= 2;
  var length = Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ;
  var angle = Math.atan((y2 - y1) / (x2 - x1));
  var left_ = x1 + 1.5*width  - 0.5 * (length ) * (1 - Math.cos(angle));
  var top_ = y1 - 0.5*height  + 0.5 * (length) * Math.sin(angle) ;
  var transform = 'rotate('+angle+'rad)';
    var line = '<div class="link ui-widget-content" id="' + name + '"'+
      'style="position:absolute;transform:'+transform+';' +
      'width:'+(length)+ 'px;'+
      'left:'+(left_)+'px;'+
      'top:'+(top_)+'px;'+
      'border:2px black solid'+
        ';z-index: 0;"'+
      //'background:'+line_color+'"'+
        ' data-right="'+x2+'"'+
        ' data-bottom="'+y2+'"'+
        ' data-start_id="'+start_block_id+'"'+
        ' data-end_id="'+end_block_id+'"'+
        '>'+
        '</div>'//+

    //'<input type="range" class="slider col-md-1 mx-auto" min="0" max="3" id="link_slide_'+name+'" style="margin-top: 10px">';

    return line;
}