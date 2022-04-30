const numbers1 = [1, 2, 3, 4, 6, 7, 8, 0];

function solution(numbers) {
  let total = 0;
  for (let i = 1; i < 10; i++) {
    total += i;
  }
  numbers1.map((num) => {
    total -= num;
  });
  var answer = total;
  return answer;
}

console.log(solution(numbers1));
