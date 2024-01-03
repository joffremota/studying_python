// static/script_file_upload.js
function uploadFiles() {
    var filesInput = document.getElementById('fileInput');
    var files = filesInput.files;
    var fileTableBody = document.getElementById('fileInfoBody');

    // Limpar a tabela antes de adicionar novas informações
    fileTableBody.innerHTML = '';

    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        if (file.name) {
            var filename, file_extension;
            [filename, file_extension] = file.name.split('.');

            var row = fileTableBody.insertRow(-1);
            var cell1 = row.insertCell(0);
            var cell2 = row.insertCell(1);
            var cell3 = row.insertCell(2);

            cell1.innerHTML = filename;
            cell2.innerHTML = file.size;
            cell3.innerHTML = file_extension;
        }
    }

    // Enviar formulário após adicionar informações à tabela
    document.getElementById('fileForm').submit();
}
