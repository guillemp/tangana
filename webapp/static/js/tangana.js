
$(document).ready(function() {
    
    // Vote click handler
    $('.vote-up').click(function() {
        var comment_id = $(this).data('commentId');
        if (comment_id > 0) {
            var url = '/comments/'+comment_id+'/vote/';
            $.post(url, function(data) {
                console.log(data);
                $('.comment-votes').html('9');
            });
        }
        return false;
    });
});

function saveVote(voteType) {
    if (voteType == 'up') {
        // +1
    } else if (voteType == 'down') {
        // -1
    }
}