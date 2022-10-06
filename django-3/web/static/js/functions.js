function message_error(obj){
    var html = '';
    if(typeof (obj) === 'object'){
        html = '<ul style="text-align: center" >';
        $.each(obj, function(key, value) {
            html+='<li>'+key+': '+value+'</li>';
        });
        html+='</ul>';
    }
    else{
        html = '<p>'+obj+'</p>'        
    }
    Swal.fire({
        titleText: 'Error al guardar',
        html: html,
        icon: 'error',
        confirmButtonText: 'OK',
    });
}