function solution(n, s) {
    var answer = [];
    if (n>s) {
        return [-1];
    } 
    plusCount = s % n;
    const prevAnswer = new Array(n-plusCount).fill(Math.floor(s/n));
    const nextAnswer = new Array(plusCount).fill(Math.floor(s/n)+1);
    
    answer = prevAnswer.concat(nextAnswer);
    return answer;
}