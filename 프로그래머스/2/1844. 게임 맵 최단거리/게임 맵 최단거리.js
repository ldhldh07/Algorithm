const delta_i = [0, 1, 0, -1];
const delta_j = [1, 0, -1, 0];

function solution(maps) {
    var answer = 0;
    const rowLength = maps.length;
    const colLength = maps[0].length;
    
    const start = new Node(0, 0);
    const end = new Node(rowLength - 1, colLength - 1); 
    answer = bfs(maps, start, end, rowLength, colLength);
    
    return answer;
}

class Node {
    constructor(row, col) {
        this.row = row;
        this.col = col;
    }
}

function bfs(maps, start, end, rowLength, colLength) {
    const queue = [start];
    const visited = [];

    for (let i = 0; i < rowLength; i++) {
        const rowArray = [];
        for (let j = 0; j < colLength; j++) {
            rowArray.push(0);
        }
        visited.push(rowArray);
    }
    visited[start.row][start.col] = 1;

    while (queue.length) {
        const current_node = queue.shift();
        for (let i = 0; i < 4; i++) {
            const nextRow = current_node.row + delta_i[i];
            const nextCol = current_node.col + delta_j[i];
            if (nextRow >= 0 && nextRow < rowLength && nextCol >= 0 && nextCol < colLength) {
                if (maps[nextRow][nextCol] === 1 && visited[nextRow][nextCol] === 0) {
                    const nextNode = new Node(nextRow, nextCol);
                    queue.push(nextNode);
                    visited[nextRow][nextCol] = visited[current_node.row][current_node.col] + 1;
                    if (nextRow === end.row && nextCol === end.col) {
                        return visited[end.row][end.col];
                    }
                }
            }
        }
    }
    return -1;
}