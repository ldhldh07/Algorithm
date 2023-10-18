function solution(name, yearning, photo) {
    let nameMap = new Map();
    for (let i=0; i<name.length; i++) {
        nameMap.set(name[i], yearning[i]);
    }
    const answer = photo.map((p) => {
        return p.reduce((acc, n) => {
            return acc + (nameMap.get(n) || 0);
        }, 0)
    })
    return answer;
}