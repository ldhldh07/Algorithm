function solution(number, k) {
    let queue = [];
    let count = k;
    
    for (let n of number) {
        while (queue.length && queue[queue.length - 1] < n && count > 0) {
            queue.pop();
            count--;
        }
        queue.push(n);
    }
    while (count > 0) {
        queue.pop();
        count--;
    }

    return queue.join('');
}
