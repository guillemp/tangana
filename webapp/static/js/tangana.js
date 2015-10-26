
$(document).ready(function() {
    

    $('.vote-action').click(function() {
        var vote_type = $(this).data('vote');
        var comment_id = $(this).data('commentId');
        if (comment_id > 0 && vote_type) {
            var url = '/comment/'+comment_id+'/vote/';
            $.post(url, {vote: vote_type}, function(data) {
                if (data > 0) {
                    var content = '<span class="vote-up"><i class="fa fa-arrow-circle-up"></i> '+data+'</span>';
                } else {
                    var content = '<span class="vote-down"><i class="fa fa-arrow-circle-down"></i> '+data+'</span>';
                }
                $('#comment-'+comment_id+'-votes').html(content);
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
    
    
    $('.reply-comment').click(function() {
        var comment_id = $(this).data('commentId');
        $('#comment-'+comment_id+'-reply').toggle();
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