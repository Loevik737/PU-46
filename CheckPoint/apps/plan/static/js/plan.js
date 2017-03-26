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

//Function for opening modal and closing if click outside of modal
function openModal(counter) {
    // Get the modal
    var modal = document.getElementById('myCreateModal-'+counter);
    // Show the modal
    modal.style.display = "block";
    // Close if click outside of modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
}

//Function for closeing modal through close button
function closeModal(counter){
    //Get modal to close
    var modal = document.getElementById('myCreateModal-'+counter);
    //Close modal
    modal.style.display = "none";
}