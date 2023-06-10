window.onload = function() {
    const url_1 = 'http://127.0.0.1:5001/api';

    // Function to delete project
    function ProjectDelete(element) {
        const d = $(element).data('id');
        console.log(d);
        $.ajax({
            url: url_1 + '/projects/' + d,
            method: 'DELETE',
            success: function() {
                location.reload();
            },
            error: function() {
                alert("The project cannot be deleted.");
            }
        });
    }

    // Usage
    $('.del').click(function() {
        ProjectDelete(this);
    });
};
