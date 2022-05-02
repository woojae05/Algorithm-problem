const a1 = [1, 2, 3, 4];
const b1 = [-3, -1, 0, 2];

function solution(a, b) {
  let answer = 0;
  a.map((num, idx) => {
    answer += num * b[idx];
  });
  return answer;
}

console.log(solution(a1, b1));
