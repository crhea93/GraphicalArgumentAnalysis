//------------------BASIC CONCEPT BLOCK DEFINITION------------------------//
function def_concept(x,y,ct){
    def_concept_ret = '<div class="block rgba-cyan-slight text-black ui-widget-content draggable ui-resizable rectangle rounded"'+
                     'id="block_'+ct+'"'+
                     //'title="'+ct+'"'+
                     'style="'+
                    'width:150px;'+
                    'height:100px;'+
                    'left:'+x+'px;' +
                    'top:'+y+'px;' +
                    'border: 3px solid black;'+
                    'text-align:center;position:absolute'+
                        ';z-index: 2;' +'">'+
                    '<button type="button" class="close" style="z-index: 2" id="delete_'+ct+'" aria-label="Close">\n' +
        '          <span class="float-right close-btn" style="font-size:1rem" aria-hidden="true" style="z-index: inherit">&times;</span>\n' +
        '        </button>'+
                    '<div id="block_form_'+ct+'" class="card-body block-form">'+
                      '<div class="form-row">'+
                          '<div class="form-group">'+
                            '<input class="col-md-10" type="text" id="title_'+ct+'" placeholder="text">'+
                          '</div>'+
                        '</div>'+
                     '</div>' +
                    '<div style="text-align:center;vertical-align:middle;z-index:3" id="success_block_'+ct+'"></div>'+
                    '</div>';
    return def_concept_ret
}