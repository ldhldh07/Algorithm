function solution(n, times) {
    let start = 1;
    let end = n * Math.max(...times);
    
    while (start <= end) {
        let mid = Math.floor((start + end) / 2);
        let count = getCount(mid, times);
        
        if (count < n) {
            start = mid + 1;
        } else {
            end = mid - 1;
        }
    }
    
    return start;
}

function getCount(time, times) {
    let count = 0;
    
    times.forEach((t) => {
        count += Math.floor(time / t);
    });
    
    return count;
}
