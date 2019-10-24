function existing_concept_init(title,x,y,num,id) {
    num = parseInt(num);
    //Create concept already in user's bank
    var def_created_concept = '<div class="block draggable rgba-cyan-slight text-black ui-widget-content ui-resizable rectangle rounded"' +
        'id="block_' + num + '"' +
        'style="' +
        'width:150px;' +
        'height:100px;' +
        'left:' + x + 'px;' +
        'top:' + y + 'px;' +
        'border: 3px solid black;'+
        'text-align:center;position:absolute'+
        ';z-index: 2;"' +
        'title="' + id + '">' +
        '<button type="button" class="close" id="delete_' + num + '" aria-label="Close">\n' +
        '          <span class="float-right" style="font-size:1rem" aria-hidden="true">&times;</span>\n' +
        '        </button>' +
        '<div id="block_form_' + num + '" class="card-body block-form" hidden>' +
            '<div class="form-row">' +
                '<div class="form-group">' +
                '<input class="col-md-10" type="text" style="z-index: 2" id="title_' + num + '" value="'+title+'" placeholder="text">'+
                '</div>' +
            '</div>' +
        '</div>' +
        '<div class="text-align:center;vertical-align:middle" style="z-index: 3" id="success_block_' + num + '"></div>' +
        '</div>';
    return def_created_concept
}