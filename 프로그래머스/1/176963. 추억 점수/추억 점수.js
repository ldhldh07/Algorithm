function solution(name, yearning, photo) {
    var answer = [];
    let nameMap = new Map();
    for (let i=0; i<name.length; i++) {
        nameMap.set(name[i], yearning[i]);
    }
    photo.forEach((p) => {
        const score = p.reduce((acc, n) => {
            return acc + (nameMap.get(n) || 0);
        }, 0)
        answer.push(score);
    })
    return answer;
}