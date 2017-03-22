/**
 * Created by TirilMerethe on 22/02/2017.
 */
var acc = document.getElementsByClassName("accordion");
for (var i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.display === "block") {
            panel.style.display = "none";
        } else {
            panel.style.display = "block";
        }
    }
}

// Get the modal
var createModal = document.getElementById('myCreateModal');

// Get the button that opens the modal
var createBtn = document.getElementById("myCreateBtn");

// Get the <span> element that closes the modal
var createSpan = document.getElementsByClassName("close2")[0];

// When the user clicks on the button, open the modal
createBtn.onclick = function() {
    createModal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
createSpan.onclick = function() {
    createModal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == createModal) {
        createModal.style.display = "none";
    }
};

// Get the modal
var editModal = document.getElementById('myEditModal');

// Get the button that opens the modal
var editBtn = document.getElementById("myEditBtn");

// Get the <span> element that closes the modal
var editSpan = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal

function openModal(id) {
    console.log('123', id);
    var modal = document.getElementById('myEditModal');
    //$('#myEditModal-'+id).find('#id_title').val('title');
    modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
editSpan.onclick = function() {
    editModal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == editModal) {
        editModal.style.display = "none";
    }
};