$(document).on('click', '#like', function(e){
    const artId = $(this).val()
    const btn = this
    e.preventDefault();
    $.ajax({
        headers: {"X-CSRFToken": '{{csrf_token}}'},
        type: 'POST',
        url: "{% url 'api_v1:post_like' %}",
        data: {
            postid: $(this).val(),
            csrfmiddlewaretoken: '{{ csrf_token }}',
            action: 'post'
        },
        success: function(json) {
            let c = `"${artId}"`
            btn.innerHTML = json['icon']
            let counter = document.querySelector(`[data-artId=${c}]`)
            counter.innerHTML = json['count']
        },
        error: function(xhr, errmsg, err){
        }
    })
})