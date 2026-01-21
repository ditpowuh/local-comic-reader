let updateInProgress = false;

function update(process) {
  if (updateInProgress) {
    return;
  }
  updateInProgress = true;
  fetch("/" + process).then((response) => {
    if (!response.ok) {
      throw new Error("Request failed");
    }
    return response.json();
  }).then((data) => {
    document.getElementById("info").innerHTML = data.info;
    document.getElementById("images").innerHTML = data.images;
  }).catch((error) => {
    console.error(error);
  }).finally(() => {
    updateInProgress = false;
  });
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("previouspage").addEventListener("click", () => {
    update("previousPage")
  });

  document.getElementById("changset").addEventListener("click", () => {
    update("setChange")
  });

  document.getElementById("nextpage").addEventListener("click", () => {
    update("nextPage")
  });
});
