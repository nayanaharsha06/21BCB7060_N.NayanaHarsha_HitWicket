document.getElementById('start-button').addEventListener('click', () => {
    fetch('/start_game', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'Game started') {
                alert('Game has started!');
                updateBoard();
            }
        });
});

document.getElementById('move-form').addEventListener('submit', (event) => {
    event.preventDefault();
    
    const player = document.getElementById('player').value;
    const figureName = document.getElementById('figure-name').value;
    const direction = document.getElementById('direction').value;
    
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player, figure_name: figureName, direction })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message === 'Move successful') {
            alert('Move successful!');
            updateBoard();
        } else {
            alert('Move failed');
        }
    });
});

function updateBoard() {
    fetch('/board_state')
        .then(response => response.json())
        .then(data => {
            const board = data.board_state;
            let boardHtml = '<table>';
            for (let row of board) {
                boardHtml += '<tr>';
                for (let cell of row) {
                    boardHtml += `<td>${cell || ''}</td>`;
                }
                boardHtml += '</tr>';
            }
            boardHtml += '</table>';
            document.getElementById('board').innerHTML = boardHtml;
        });
}
