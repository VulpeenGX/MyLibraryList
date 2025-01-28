// Cuadro emergente de guardado
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("cGuardar").addEventListener("click", function () {
    sessionStorage.setItem("showSaveAlert", "true");
    sessionStorage.removeItem("showEditAlert"); 
    sessionStorage.removeItem("showDeleteAlert"); 
    window.location.href = "{{ url_for('library.index') }}";
  });
});

document.addEventListener("DOMContentLoaded", function () {
  if (sessionStorage.getItem("showSaveAlert") === "true") {
    var alertBox = document.getElementById("customAlert");
    alertBox.style.display = "block";
    setTimeout(function () {
      alertBox.style.display = "none";
      sessionStorage.removeItem("showSaveAlert");
    }, 1000);
  }
});

// Cuadro emergente de editado
document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("uEditar").addEventListener("click", function () {
    console.log('Botón eliminar clickeado');
    sessionStorage.setItem("showEditAlert", "true");
    sessionStorage.removeItem("showSaveAlert"); 
    sessionStorage.removeItem("showDeleteAlert"); 
    window.location.href = "{{ url_for('library.index') }}";
  });
});

document.addEventListener("DOMContentLoaded", function () {
  if (sessionStorage.getItem("showEditAlert") === "true") {
    var alertBox = document.getElementById("customAlert2");
    alertBox.style.display = "block";
    setTimeout(function () {
      alertBox.style.display = "none";
      sessionStorage.removeItem("showEditAlert");
    }, 1000);
  }
});