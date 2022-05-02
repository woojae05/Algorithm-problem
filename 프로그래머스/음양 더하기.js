const absolutes1 = [4, 7, 12];
const signs = [true, false, true];

function solution(absolutes, signs) {
  let answer = 0;
  absolutes.map((num, idx) => {
    signs[idx] ? (answer += num) : (answer -= num);
  });
  return answer;
}

console.log(solution(absolutes1, signs));

// 다른 사람의 코드(reduce 함수)
// function solution(absolutes, signs) {

//     return absolutes.reduce((acc, val, i) => acc + (val * (signs[i] ? 1 : -1)), 0);
// }
