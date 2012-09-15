var editor;
var re_params = /:([a-zA-Z0-9_]+)/g;

function show_params(){
    var params = [];
    django.jQuery('#id_text').html(editor.getValue());
    while(find_param = re_params.exec(editor.getValue())){
        for(var i = 0; i < params.length; i++){
            if(find_param[1] == params[i]){
                django.jQuery('#find_params').html('PLEASE, DO NOT REPEAT PARAMS NAMES');
                return;
            }
        }
        params.push(find_param[1]);
    }
    django.jQuery('#find_params').html(params.join(', '));
}


django.jQuery(function(){
    django.jQuery('<div/>', {
        id: 'syntax_text',
        text: django.jQuery('#id_text').val()
    }).insertAfter('#id_text');

    django.jQuery('<div/>', {
        id: 'find_params'
    }).insertAfter('#syntax_text');

    editor = ace.edit("syntax_text");
    editor.setTheme("ace/theme/textmate");
    editor.getSession().setMode("ace/mode/sql");
    show_params();
    editor.on("change", show_params);
});