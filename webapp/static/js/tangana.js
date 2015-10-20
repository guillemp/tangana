
$(document).ready(function() {
    
    // Vote click handler
    $('.vote-up').click(function() {
        var comment_id = $(this).data('commentId');
        if (comment_id > 0) {
            var url = '/comment/'+comment_id+'/vote/';
            $.post(url, {vote: 'up'}, function(data) {
                console.log(data);
                $('.comment-votes').html(data);
            });
        }
        return false;
    });
    
    $('.vote-down').click(function() {
        var comment_id = $(this).data('commentId');
        if (comment_id > 0) {
            var url = '/comment/'+comment_id+'/vote/';
            $.post(url, {vote: 'down'}, function(data) {
                console.log(data);
                $('.comment-votes').html(data);
            });
        }
        return false;
    });
    
    
    // prevent enters
    $('#form_content').keypress(function(event) {
        if (event.keyCode == '13') {
            event.preventDefault();
        }
    });
});

function saveVote(voteType) {
    if (voteType == 'up') {
        // +1
    } else if (voteType == 'down') {
        // -1
    }
}