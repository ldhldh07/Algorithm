function solution(players, callings) {
    const playerIndex = new Map();
    
    for (let i = 0; i < players.length; i++) {
        playerIndex.set(players[i], i);
    }

    for (let calling of callings) {
        const idx = playerIndex.get(calling);
        if (idx > 0) {
            const frontPlayer = players[idx - 1];
            players[idx - 1] = calling;
            players[idx] = frontPlayer;
            playerIndex.set(calling, idx - 1);
            playerIndex.set(frontPlayer, idx);
        }
    }

    return players;
}