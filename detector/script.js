const canvas = document.getElementById('detector-canvas');
const ctx = canvas.getContext('2d');
const notesDiv = document.getElementById('notes');
const noteInput = document.getElementById('note-input');

let startX, startY, isDragging = false;
const notes = [];

const image = new Image();
image.src = 'LHCB.jpg'; // Use the path to your image
image.onload = () => {
  ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
};

canvas.addEventListener('mousedown', (e) => {
  const rect = canvas.getBoundingClientRect();
  startX = e.clientX - rect.left;
  startY = e.clientY - rect.top;
  isDragging = true;
});

canvas.addEventListener('mousemove', (e) => {
  if (isDragging) {
    const rect = canvas.getBoundingClientRect();
    const mouseX = e.clientX - rect.left;
    const mouseY = e.clientY - rect.top;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(image, 0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = 'red';
    ctx.strokeRect(startX, startY, mouseX - startX, mouseY - startY);
  }
});

canvas.addEventListener('mouseup', (e) => {
  if (isDragging) {
    const rect = canvas.getBoundingClientRect();
    const endX = e.clientX - rect.left;
    const endY = e.clientY - rect.top;
    isDragging = false;

    const note = {
      x: startX,
      y: startY,
      width: endX - startX,
      height: endY - startY,
      text: ''
    };
    notes.push(note);
    updateNotes();
  }
});

function updateNotes() {
  notesDiv.innerHTML = notes.map((note, index) => `
    <div>
      <strong>Note ${index + 1}:</strong>
      <div>${note.text}</div>
    </div>
  `).join('');
}

function saveNote() {
  if (notes.length > 0) {
    notes[notes.length - 1].text = noteInput.value;
    noteInput.value = '';
    updateNotes();
  }
}
