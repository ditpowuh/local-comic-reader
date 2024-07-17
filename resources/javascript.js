updateInProgress = false;

function update(process) {
  if (updateInProgress === true) {
    return;
  }
  updateInProgress = true;
  $.ajax({
    url: "/" + process,
    type: "GET",
    success: function(response) {
      document.getElementById("info").innerHTML = response.info;
      document.getElementById("images").innerHTML = response.images;
      updateInProgress = false;
    },
    error: function(error) {
      console.log(error);
      updateInProgress = false;
    }
  });
}

$(document).ready(function() {
  $("#previouspage").click(function() {
    update("previousPage");
  });
  $("#changset").click(function() {
    update("setChange");
  });
  $("#nextpage").click(function() {
    update("nextPage");
  });
});
