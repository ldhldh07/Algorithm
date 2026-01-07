function solution(friends, gifts) {
  const giftAdj = new Map(); // Map<giver, Map<receiver, count>>

  for (const gift of gifts) {
    const [giver, receiver] = gift.split(" ");
    if (!giftAdj.has(giver)) giftAdj.set(giver, new Map());
    const inner = giftAdj.get(giver);
    inner.set(receiver, (inner.get(receiver) ?? 0) + 1);
  }

  const giftIndex = new Map();
  for (const f of friends) giftIndex.set(f, 0);

  for (const giver of friends) {
    const inner = giftAdj.get(giver);
    if (!inner) continue;
    for (const [receiver, cnt] of inner) {
      giftIndex.set(giver, giftIndex.get(giver) + cnt);       
      giftIndex.set(receiver, giftIndex.get(receiver) - cnt); 
    }
  }

  const nextReceive = new Map();
  for (const f of friends) nextReceive.set(f, 0);

  for (let i = 0; i < friends.length; i++) {
    for (let j = i + 1; j < friends.length; j++) {
      const a = friends[i];
      const b = friends[j];

      const aToB = giftAdj.get(a)?.get(b) ?? 0;
      const bToA = giftAdj.get(b)?.get(a) ?? 0;

      if (aToB > bToA) {
        nextReceive.set(a, nextReceive.get(a) + 1);
      } else if (bToA > aToB) {
        nextReceive.set(b, nextReceive.get(b) + 1);
      } else {
        const ai = giftIndex.get(a);
        const bi = giftIndex.get(b);

        if (ai > bi) nextReceive.set(a, nextReceive.get(a) + 1);
        else if (bi > ai) nextReceive.set(b, nextReceive.get(b) + 1);
      }
    }
  }

  let ans = 0;
  for (const v of nextReceive.values()) ans = Math.max(ans, v);
  return ans;
}