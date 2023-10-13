function deleteNote(noteID) {
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.strinngify({noteId: noteId}),
    }).then((_res) => {
        window.location.href = "/";
    });
}