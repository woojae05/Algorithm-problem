const n1 = 5;
const lost1 = [4, 3];
const reserve1 = [3, 2];

function solution(n, lost, reserve) {
  const students = {};
  let answer = 0;
  for (let i = 1; i <= n; i++) {
    students[i] = 1;
  }
  lost.forEach((number) => (students[number] -= 1));
  reserve.forEach((number) => (students[number] += 1));

  for (let i = 1; i <= n; i++) {
    if (students[i] === 2 && students[i - 1] === 0) {
      students[i - 1]++;
      students[i]--;
    } else if (students[i] === 2 && students[i + 1] === 0) {
      students[i + 1]++;
      students[i]--;
    }
  }
  for (let key in students) {
    if (students[key] >= 1) {
      answer++;
    }
  }
  return answer;
}

console.log(solution(n1, lost1, reserve1));
